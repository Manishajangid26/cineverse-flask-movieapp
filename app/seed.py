from app import db
from app.models import Movie

def seed_initial_movies():
    if Movie.query.first():
        return

    famous_movies = [
        {
            "imdb_id": "tt1375666", "title": "Inception", "year": "2010", "released": "16 Jul 2010",
            "runtime": "148 min", "language": "English", "genre": "Action, Adventure, Sci-Fi",
            "director": "Christopher Nolan", "actors": "Leonardo DiCaprio, Joseph Gordon-Levitt, Elliot Page",
            "plot": "A thief who steals corporate secrets through dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O.",
            "poster": "https://m.media-amazon.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_SX300.jpg",
            "imdb_rating": "8.8", "user_rating": 5, "user_review": "Mind-bending masterpiece with unforgettable visuals.",
            "is_watchlist": True, "is_favorite": True
        },
        {
            "imdb_id": "tt0816692", "title": "Interstellar", "year": "2014", "released": "07 Nov 2014",
            "runtime": "169 min", "language": "English", "genre": "Adventure, Drama, Sci-Fi",
            "director": "Christopher Nolan", "actors": "Matthew McConaughey, Anne Hathaway, Jessica Chastain",
            "plot": "When Earth becomes uninhabitable in the future, a farmer and ex-NASA pilot is tasked to pilot a spacecraft to find a new planet for humans.",
            "poster": "https://m.media-amazon.com/images/M/MV5BYzdjMDAxZGItMjI2My00ODA1LTlkNzItOWFjMDU5ZDJlYWY3XkEyXkFqcGc@._V1_SX300.jpg",
            "imdb_rating": "8.7", "user_rating": 5, "user_review": "Emotional sci-fi epic about time, gravity, and survival.",
            "is_watchlist": True, "is_favorite": True
        },
        {
            "imdb_id": "tt0468569", "title": "The Dark Knight", "year": "2008", "released": "18 Jul 2008",
            "runtime": "152 min", "language": "English", "genre": "Action, Crime, Drama",
            "director": "Christopher Nolan", "actors": "Christian Bale, Heath Ledger, Aaron Eckhart",
            "plot": "When the menace known as the Joker wreaks havoc and chaos on Gotham, Batman must accept one of the greatest psychological tests to fight injustice.",
            "poster": "https://m.media-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_SX300.jpg",
            "imdb_rating": "9.0", "user_rating": 5, "user_review": "Greatest superhero crime thriller ever made.",
            "is_watchlist": True, "is_favorite": True
        },
        {
            "imdb_id": "tt1187043", "title": "3 Idiots", "year": "2009", "released": "25 Dec 2009",
            "runtime": "170 min", "language": "Hindi", "genre": "Comedy, Drama",
            "director": "Rajkumar Hirani", "actors": "Aamir Khan, Madhavan, Mona Singh, Sharman Joshi",
            "plot": "Two friends search for their long lost companion and recall their college days with the friend who inspired them to think differently.",
            "poster": "https://m.media-amazon.com/images/M/MV5BNTkyOGVjMGEtNmQzZi00NzFlLTlhOWQtODYyMDc2ZGJmYzFhXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SX300.jpg",
            "imdb_rating": "8.4", "user_rating": 5, "user_review": "Timeless Indian classic inspiring passion over rote learning.",
            "is_watchlist": True, "is_favorite": True
        },
        {
            "imdb_id": "tt4154796", "title": "Avengers: Endgame", "year": "2019", "released": "26 Apr 2019",
            "runtime": "181 min", "language": "English", "genre": "Action, Adventure, Drama",
            "director": "Anthony Russo, Joe Russo", "actors": "Robert Downey Jr., Chris Evans, Mark Ruffalo, Scarlett Johansson",
            "plot": "After the devastating events of Infinity War, the Avengers assemble once more to reverse Thanos' actions and restore balance to the universe.",
            "poster": "https://m.media-amazon.com/images/M/MV5BMTc5MDE2ODcwNV5BMl5BanBnXkFtZTgwMzI2NzQ2NzM@._V1_SX300.jpg",
            "imdb_rating": "8.4", "user_rating": 4, "user_review": "Unforgettable conclusion to a decade-long saga.",
            "is_watchlist": True, "is_favorite": False
        },
        {
            "imdb_id": "tt5074352", "title": "Dangal", "year": "2016", "released": "21 Dec 2016",
            "runtime": "161 min", "language": "Hindi", "genre": "Action, Biography, Drama",
            "director": "Nitesh Tiwari", "actors": "Aamir Khan, Sakshi Tanwar, Fatima Sana Shaikh, Sanya Malhotra",
            "plot": "Former wrestler Mahavir Singh Phogat and his two wrestler daughters struggle towards glory at the Commonwealth Games.",
            "poster": "https://m.media-amazon.com/images/M/MV5BMTQ4MzQzMzM2Nl5BMl5BanBnXkFtZTgwMTQ1NzU3MDI@._V1_SX300.jpg",
            "imdb_rating": "8.3", "user_rating": 5, "user_review": "Powerful biographical sports drama.",
            "is_watchlist": True, "is_favorite": True
        },
        {
            "imdb_id": "tt0111161", "title": "The Shawshank Redemption", "year": "1994", "released": "14 Oct 1994",
            "runtime": "142 min", "language": "English", "genre": "Drama",
            "director": "Frank Darabont", "actors": "Tim Robbins, Morgan Freeman, Bob Gunton",
            "plot": "Over the course of several years, two convicts form a friendship, seeking consolation and eventual redemption through basic compassion.",
            "poster": "https://m.media-amazon.com/images/M/MV5BMDAyY2FhYjctNDc5OS00MDNlLThiMGUtY2UxYWVkNGY2ZjljXkEyXkFqcGc@._V1_SX300.jpg",
            "imdb_rating": "9.3", "user_rating": 5, "user_review": "Hope is a good thing, maybe the best of things.",
            "is_watchlist": True, "is_favorite": True
        },
        {
            "imdb_id": "tt15398776", "title": "Oppenheimer", "year": "2023", "released": "21 Jul 2023",
            "runtime": "180 min", "language": "English", "genre": "Biography, Drama, History",
            "director": "Christopher Nolan", "actors": "Cillian Murphy, Emily Blunt, Matt Damon, Robert Downey Jr.",
            "plot": "The story of American scientist J. Robert Oppenheimer and his role in the development of the atomic bomb during World War II.",
            "poster": "https://m.media-amazon.com/images/M/MV5BMDBmYTZjNjUtN2M1MS00MTQ2LTk2ODgtNzc2M2QyZGE5NTVjXkEyXkFqcGdeQXVyNzAwMjU2MTY@._V1_SX300.jpg",
            "imdb_rating": "8.3", "user_rating": 5, "user_review": "Gripping historical drama with Oscar-winning acting.",
            "is_watchlist": True, "is_favorite": False
        },
        {
            "imdb_id": "tt8178634", "title": "RRR", "year": "2022", "released": "25 Mar 2022",
            "runtime": "187 min", "language": "Telugu, Hindi", "genre": "Action, Drama",
            "director": "S.S. Rajamouli", "actors": "N.T. Rama Rao Jr., Ram Charan, Ajay Devgn, Alia Bhatt",
            "plot": "A fictitious story about two legendary revolutionaries and their journey away from home before they started fighting for their country in the 1920s.",
            "poster": "https://m.media-amazon.com/images/M/MV5BODUwNDNjYzctODUxNy00ZTA2LWIyYTEtMDc5Y2E5ZjBmNTMzXkEyXkFqcGdeQXVyODE5NzE3OTE@._V1_SX300.jpg",
            "imdb_rating": "7.8", "user_rating": 5, "user_review": "High-octane action spectacle with iconic Naatu Naatu.",
            "is_watchlist": True, "is_favorite": True
        },
        {
            "imdb_id": "tt15239678", "title": "Dune: Part Two", "year": "2024", "released": "01 Mar 2024",
            "runtime": "166 min", "language": "English", "genre": "Action, Adventure, Drama",
            "director": "Denis Villeneuve", "actors": "Timothée Chalamet, Zendaya, Rebecca Ferguson, Javier Bardem",
            "plot": "Paul Atreides unites with Chani and the Fremen while seeking revenge against the conspirators who destroyed his family.",
            "poster": "https://m.media-amazon.com/images/M/MV5BN2QyZGU4ZDctOWMzMy00NTc5LThlOGQtODhmNDI1NmY5YzAwXkEyXkFqcGdeQXVyMDM2NDM2MQ@@._V1_SX300.jpg",
            "imdb_rating": "8.5", "user_rating": 4, "user_review": "Breathtaking cinematography and sound design.",
            "is_watchlist": True, "is_favorite": False
        },
        {
            "imdb_id": "tt23849204", "title": "12th Fail", "year": "2023", "released": "27 Oct 2023",
            "runtime": "147 min", "language": "Hindi", "genre": "Biography, Drama",
            "director": "Vidhu Vinod Chopra", "actors": "Vikrant Massey, Medha Shankr, Anant V Joshi",
            "plot": "The real-life story of IPS Officer Manoj Kumar Sharma and IRS Officer Shraddha Joshi who fearlessly embraced the idea of restarting their academic journey.",
            "poster": "https://upload.wikimedia.org/wikipedia/en/f/f2/12th_Fail_poster.jpeg",
            "imdb_rating": "8.8", "user_rating": 5, "user_review": "Deeply inspiring story of grit, honesty, and perseverance.",
            "is_watchlist": True, "is_favorite": True
        },
        {
            "imdb_id": "tt6751668", "title": "Parasite", "year": "2019", "released": "08 Nov 2019",
            "runtime": "132 min", "language": "Korean", "genre": "Drama, Thriller",
            "director": "Bong Joon Ho", "actors": "Song Kang-ho, Lee Sun-kyun, Cho Yeo-jeong",
            "plot": "Greed and class discrimination threaten the newly formed symbiotic relationship between the wealthy Park family and the destitute Kim clan.",
            "poster": "https://m.media-amazon.com/images/M/MV5BYWZjMjk3ZTItODQ2ZC00NTY5LWE0ZDYtZTI3MjcwN2Q5NTVkXkEyXkFqcGdeQXVyODk4OTc3MTY@._V1_SX300.jpg",
            "imdb_rating": "8.5", "user_rating": 5, "user_review": "Brilliant Oscar-winning thriller with sharp social commentary.",
            "is_watchlist": False, "is_favorite": True
        },
        {
            "imdb_id": "tt2631186", "title": "Baahubali: The Beginning", "year": "2015", "released": "10 Jul 2015",
            "runtime": "159 min", "language": "Telugu, Hindi", "genre": "Action, Drama",
            "director": "S.S. Rajamouli", "actors": "Prabhas, Rana Daggubati, Anushka Shetty, Tamannaah",
            "plot": "In ancient India, an adventurous and daring man becomes involved in a decades-old feud between two warring peoples.",
            "poster": "https://m.media-amazon.com/images/M/MV5BYWVlMjVhZWYtNWViNC00ODFkLTk1MmItYjU1MDY5ZDdhMTU3XkEyXkFqcGdeQXVyODIwMDI1NjM@._V1_SX300.jpg",
            "imdb_rating": "8.0", "user_rating": 4, "user_review": "Grand Indian epic cinema at its finest.",
            "is_watchlist": True, "is_favorite": False
        },
        {
            "imdb_id": "tt0133093", "title": "The Matrix", "year": "1999", "released": "31 Mar 1999",
            "runtime": "136 min", "language": "English", "genre": "Action, Sci-Fi",
            "director": "Lana Wachowski, Lilly Wachowski", "actors": "Keanu Reeves, Laurence Fishburne, Carrie-Anne Moss",
            "plot": "When a beautiful stranger leads computer hacker Neo to a forbidding underworld, he discovers the shocking truth about reality.",
            "poster": "https://m.media-amazon.com/images/M/MV5BNzQzOTk3OTAtNDQ0Zi00ZTVkLWI0MTEtMDllZjNkYzNjNTc4L2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SX300.jpg",
            "imdb_rating": "8.7", "user_rating": 5, "user_review": "Revolutionary sci-fi action classic.",
            "is_watchlist": False, "is_favorite": True
        },
        {
            "imdb_id": "tt10872600", "title": "Spider-Man: No Way Home", "year": "2021", "released": "17 Dec 2021",
            "runtime": "148 min", "language": "English", "genre": "Action, Adventure, Fantasy",
            "director": "Jon Watts", "actors": "Tom Holland, Zendaya, Benedict Cumberbatch",
            "plot": "With Spider-Man's identity now revealed, Peter asks Doctor Strange for help. When a spell goes wrong, dangerous foes from other worlds appear.",
            "poster": "https://m.media-amazon.com/images/M/MV5BZWMyYzFjYTYtNTRjYi00OGExLWE2YzgtOGRmYjAxZTU3NzBiXkEyXkFqcGdeQXVyMzQ0MzA0NTM@._V1_SX300.jpg",
            "imdb_rating": "8.2", "user_rating": 4, "user_review": "Pure nostalgia and thrilling multiverse action.",
            "is_watchlist": True, "is_favorite": False
        },
        {
            "imdb_id": "tt0454921", "title": "The Pursuit of Happyness", "year": "2006", "released": "15 Dec 2006",
            "runtime": "117 min", "language": "English", "genre": "Biography, Drama",
            "director": "Gabriele Muccino", "actors": "Will Smith, Thandiwe Newton, Jaden Smith",
            "plot": "A struggling salesman takes custody of his son as he's poised to begin a life-changing professional career.",
            "poster": "https://m.media-amazon.com/images/M/MV5BMTQ5NjQ0NDI3NF5BMl5BanBnXkFtZTcwNDI0MjEzMw@@._V1_SX300.jpg",
            "imdb_rating": "8.0", "user_rating": 5, "user_review": "Heart-touching true story of never giving up.",
            "is_watchlist": True, "is_favorite": True
        }
    ]

    for item in famous_movies:
        movie = Movie(**item)
        db.session.add(movie)

    db.session.commit()