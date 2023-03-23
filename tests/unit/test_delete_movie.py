from src.repositories.movie_repository import get_movie_repository

# TODO: Feature 6

def test_delete_movie_page():
    movie_repository = get_movie_repository()
    movie1 = movie_repository.create_movie('Start Wars', 'Director1', 4)
    movie2 = movie_repository.create_movie('Forrest Gump', 'Director2', 5)
    movie_repository.delete_movie(movie2.movie_id)
    movies = movie_repository.get_all_movies()

    assert movie2.movie_id not in movies
    assert movie1.movie_id in movies