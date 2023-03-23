from src.repositories.movie_repository import get_movie_repository

# TODO: Feature 6

def test_delete_movie_page(test_app):
    movie_repository = get_movie_repository()
    movie1 = movie_repository.create_movie('Start Wars', 'Director1', 4)
    movie2 = movie_repository.create_movie('Forrest Gump', 'Director2', 5)
    response = test_app.post(f"/movies/{movie2.movie_id}/delete", follow_redirects=True)
    data = response.data.decode('utf-8')

    assert response.status_code == 200
    assert f'<td>{movie2.movie_id}</td>' not in data
    assert f'<td>{movie1.movie_id}</td>' in data