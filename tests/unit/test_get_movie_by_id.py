# TODO: Feature 4
from src.repositories.movie_repository import get_movie_repository

def test_get_movie_by_id():
    movie_repository = get_movie_repository()
    movie = movie_repository.create_movie('movie_name', 'director_name', 5)
    movie_id = movie.movie_id

    get_by_id_movie = movie_repository.get_movie_by_id(movie_id)

    assert get_by_id_movie.movie_id == movie_id
    assert get_by_id_movie.title == 'movie_name'
    assert get_by_id_movie.director == 'director_name'
    assert get_by_id_movie.rating == 5