import os
import requests
from collections import Counter
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from app import db
from app.models import Movie

main = Blueprint('main', __name__)

FALLBACK_POSTER = "https://via.placeholder.com/300x450/141824/e50914?text=No+Poster+Available"


@main.route('/')
def index():
    search_query = request.args.get('q', '').strip()
    genre_filter = request.args.get('genre', '').strip()
    sort_by = request.args.get('sort', 'newest')

    query = Movie.query
    if search_query:
        query = query.filter(
            (Movie.title.ilike(f'%{search_query}%')) |
            (Movie.actors.ilike(f'%{search_query}%')) |
            (Movie.director.ilike(f'%{search_query}%')) |
            (Movie.language.ilike(f'%{search_query}%'))
        )
    if genre_filter:
        query = query.filter(Movie.genre.ilike(f'%{genre_filter}%'))

    if sort_by == 'rating':
        movies = query.order_by(Movie.imdb_rating.desc()).all()
    elif sort_by == 'year':
        movies = query.order_by(Movie.year.desc()).all()
    else:
        movies = query.order_by(Movie.created_at.desc()).all()

    featured_movie = Movie.query.filter_by(is_favorite=True).first() or Movie.query.first()
    total_movies = Movie.query.count()

    return render_template(
        'index.html',
        movies=movies,
        featured_movie=featured_movie,
        search_query=search_query,
        genre_filter=genre_filter,
        sort_by=sort_by,
        total_movies=total_movies
    )


@main.route('/watchlist')
def watchlist():
    tab = request.args.get('tab', 'watchlist')
    if tab == 'favorites':
        movies = Movie.query.filter_by(is_favorite=True).order_by(Movie.created_at.desc()).all()
    else:
        movies = Movie.query.filter_by(is_watchlist=True).order_by(Movie.created_at.desc()).all()

    watchlist_count = Movie.query.filter_by(is_watchlist=True).count()
    favorites_count = Movie.query.filter_by(is_favorite=True).count()

    return render_template(
        'watchlist.html',
        movies=movies,
        tab=tab,
        watchlist_count=watchlist_count,
        favorites_count=favorites_count
    )


@main.route('/add-movie', methods=['GET', 'POST'])
def add_movie():
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        year = request.form.get('year', '').strip()
        released = request.form.get('released', '').strip() or year
        runtime = request.form.get('runtime', '').strip() or "140 min"
        language = request.form.get('language', '').strip() or "Hindi / English"
        genre = request.form.get('genre', '').strip() or "Drama"
        director = request.form.get('director', '').strip() or "Unknown"
        actors = request.form.get('actors', '').strip() or "N/A"
        plot = request.form.get('plot', '').strip() or "No description provided."
        poster = request.form.get('poster', '').strip() or FALLBACK_POSTER
        imdb_rating = request.form.get('imdb_rating', '').strip() or "8.0"
        is_watchlist = True if request.form.get('is_watchlist') else False
        is_favorite = True if request.form.get('is_favorite') else False

        if not title:
            flash("Movie title is required!", "danger")
            return redirect(url_for('main.add_movie'))

        new_movie = Movie(
            title=title, year=year, released=released, runtime=runtime,
            language=language, genre=genre, director=director, actors=actors,
            plot=plot, poster=poster, imdb_rating=imdb_rating,
            is_watchlist=is_watchlist, is_favorite=is_favorite
        )
        db.session.add(new_movie)
        db.session.commit()
        flash(f"'{title}' has been added to CineVerse!", "success")
        return redirect(url_for('main.movie_detail', movie_id=new_movie.id))

    return render_template('add_movie.html')


@main.route('/dashboard')
def dashboard():
    movies = Movie.query.all()
    total_movies = len(movies)
    watchlist_count = sum(1 for m in movies if m.is_watchlist)
    favorites_count = sum(1 for m in movies if m.is_favorite)

    ratings = []
    for m in movies:
        try:
            ratings.append(float(m.imdb_rating))
        except (ValueError, TypeError):
            pass
    avg_rating = round(sum(ratings) / len(ratings), 2) if ratings else 0.0

    # Genre breakdown count
    genre_counter = Counter()
    for m in movies:
        if m.genre:
            for g in m.genre.split(','):
                genre_counter[g.strip()] += 1
    top_genres = genre_counter.most_common(6)

    top_rated_movies = sorted(
        movies,
        key=lambda x: float(x.imdb_rating) if x.imdb_rating and x.imdb_rating != 'N/A' else 0,
        reverse=True
    )[:5]

    return render_template(
        'dashboard.html',
        total_movies=total_movies,
        watchlist_count=watchlist_count,
        favorites_count=favorites_count,
        avg_rating=avg_rating,
        top_genres=top_genres,
        top_rated_movies=top_rated_movies
    )


@main.route('/search-live', methods=['GET', 'POST'])
def search_live():
    movie_title = request.values.get('title', '').strip()
    api_key = os.getenv('OMDB_API_KEY')

    if not movie_title:
        flash("Please enter a movie name to search!", "warning")
        return redirect(url_for('main.index'))

    if not api_key or api_key == "yahan_apni_omdb_api_key_paste_karein":
        flash("OMDb API Key missing in .env file! You can still add movies via 'Add Movie' page.", "warning")
        return redirect(url_for('main.add_movie'))

    try:
        response = requests.get(
            "http://www.omdbapi.com/",
            params={"t": movie_title, "plot": "full", "apikey": api_key},
            timeout=8
        )
        data = response.json()

        if data.get("Response") == "True":
            existing = Movie.query.filter_by(imdb_id=data.get("imdbID")).first()
            if existing:
                flash(f"'{existing.title}' is already in your collection!", "info")
                return redirect(url_for('main.movie_detail', movie_id=existing.id))

            new_movie = Movie(
                imdb_id=data.get("imdbID"),
                title=data.get("Title"),
                year=data.get("Year"),
                released=data.get("Released"),
                runtime=data.get("Runtime", "N/A"),
                language=data.get("Language", "English"),
                genre=data.get("Genre"),
                director=data.get("Director"),
                actors=data.get("Actors"),
                plot=data.get("Plot"),
                poster=data.get("Poster") if data.get("Poster") != "N/A" else FALLBACK_POSTER,
                imdb_rating=data.get("imdbRating", "N/A"),
                is_watchlist=True
            )
            db.session.add(new_movie)
            db.session.commit()
            flash(f"'{new_movie.title}' fetched from OMDb and saved to your database!", "success")
            return redirect(url_for('main.movie_detail', movie_id=new_movie.id))
        else:
            flash(f"No movie found for '{movie_title}'. Try another title or add it manually!", "warning")
    except requests.RequestException:
        flash("Network error while connecting to OMDb API.", "danger")

    return redirect(url_for('main.index'))


@main.route('/movie/<int:movie_id>')
def movie_detail(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    related_movies = Movie.query.filter(Movie.id != movie.id).limit(4).all()
    return render_template('movie_detail.html', movie=movie, related_movies=related_movies)


@main.route('/movie/<int:movie_id>/toggle-favorite', methods=['POST'])
def toggle_favorite(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    movie.is_favorite = not movie.is_favorite
    db.session.commit()
    status = "added to Favorites ❤️" if movie.is_favorite else "removed from Favorites"
    flash(f"'{movie.title}' {status}!", "success")
    return redirect(request.referrer or url_for('main.index'))


@main.route('/movie/<int:movie_id>/toggle-watchlist', methods=['POST'])
def toggle_watchlist(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    movie.is_watchlist = not movie.is_watchlist
    db.session.commit()
    status = "added to Watchlist 📌" if movie.is_watchlist else "removed from Watchlist"
    flash(f"'{movie.title}' {status}!", "info")
    return redirect(request.referrer or url_for('main.index'))


@main.route('/movie/<int:movie_id>/review', methods=['POST'])
def update_review(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    movie.user_rating = int(request.form.get('user_rating', 0))
    movie.user_review = request.form.get('user_review', '').strip()
    db.session.commit()
    flash("Your rating and review have been saved!", "success")
    return redirect(url_for('main.movie_detail', movie_id=movie.id))


@main.route('/movie/<int:movie_id>/delete', methods=['POST'])
def delete_movie(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    title = movie.title
    db.session.delete(movie)
    db.session.commit()
    flash(f"'{title}' removed from your database.", "info")
    return redirect(url_for('main.index'))


@main.route('/api/movies', methods=['GET'])
def api_movies():
    movies = Movie.query.order_by(Movie.created_at.desc()).all()
    return jsonify({
        "status": "success",
        "count": len(movies),
        "movies": [m.to_dict() for m in movies]
    })