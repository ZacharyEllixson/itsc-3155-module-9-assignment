# TODO: Feature 1
from app import app
from src.repositories.movie_repository import get_movie_repository

def test_all_movies_page(test_app):

    response = test_app.get('/movies')
    assert response.status_code == 200
    assert b'<h1>There are currently no movies listed.</h1>' in response.data

    get_movie_repository().create_movie('Movie Name', 'Director', 1)
    response = test_app.get('/movies')
    assert response.status_code == 200
    assert b'<td>Movie Name</td>'