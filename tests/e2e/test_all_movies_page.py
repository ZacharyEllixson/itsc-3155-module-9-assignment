# TODO: Feature 1

def test_all_movies_page(test_app):

    response = test_app.get('/movies')
    assert response.status_code == 200
    assert b'<h1>There are currently no movies listed.</h1>' in response.data

   
