from datetime import datetime
from app import db

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    imdb_id = db.Column(db.String(30), unique=True, nullable=True)
    title = db.Column(db.String(200), nullable=False)
    year = db.Column(db.String(20), nullable=True)
    released = db.Column(db.String(50), nullable=True)
    runtime = db.Column(db.String(30), default="140 min")
    language = db.Column(db.String(100), default="English")
    genre = db.Column(db.String(150), nullable=True)
    director = db.Column(db.String(150), nullable=True)
    actors = db.Column(db.String(300), nullable=True)
    plot = db.Column(db.Text, nullable=True)
    poster = db.Column(db.String(500), nullable=True)
    imdb_rating = db.Column(db.String(10), default="8.0")
    user_rating = db.Column(db.Integer, default=0)
    user_review = db.Column(db.Text, default="")
    is_watchlist = db.Column(db.Boolean, default=True)
    is_favorite = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "imdb_id": self.imdb_id,
            "title": self.title,
            "year": self.year,
            "released": self.released,
            "runtime": self.runtime,
            "language": self.language,
            "genre": self.genre,
            "director": self.director,
            "actors": self.actors,
            "plot": self.plot,
            "poster": self.poster,
            "imdb_rating": self.imdb_rating,
            "user_rating": self.user_rating,
            "user_review": self.user_review,
            "is_watchlist": self.is_watchlist,
            "is_favorite": self.is_favorite
        }