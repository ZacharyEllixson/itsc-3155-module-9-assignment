
# create our test function


def test_edit_unit(test_app):
    test_app = app.test_client
    response = test_app.get('/movies/<int:movie_id>')
    assert response.status_coude == 200

# Resources
# https://www.youtube.com/watch?v=bToSg1TSpMA
