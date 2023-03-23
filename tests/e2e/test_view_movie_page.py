# TODO: Feature 4
from src.repositories.movie_repository import get_movie_repository

def test_view_movie_page(test_app):
    movie_repository = get_movie_repository()
    movie = movie_repository.create_movie('movie_name', 'director_name', 5)
    movie_id = movie.movie_id

    response = test_app.get(f"/movies/{movie_id}")

    assert response.status_code == 200

    data = response.data.decode('utf-8')

    assert '<h1 class="mb-5">movie_name</h1>' in data
    assert '<p>Director: director_name</p>' in data
    assert '<p>Rating: 5</p>' in data