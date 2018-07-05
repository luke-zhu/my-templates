import flask

import webservice


# TODO: This may require setup/teardown of the sqlite database
def test_user():
    client = webservice.app.test_client()
    response: flask.Response = client.get('/user/1')
    assert response.json == {'id': 1, 'username': 'luke'}


def test_users():
    client = webservice.app.test_client()
    response: flask.Response = client.get('/users')
    assert response.json == [
        {'id': 1, 'username': 'luke'},
        {'id': 2, 'username': 'bob'},
    ]


def test_graphql():
    client = webservice.app.test_client()
    query = """
        query {
            allUsers {
                edges {
                    node {
                        username
                    }
                }
            }
        }
    """

    response: flask.Response = client.get('/graphql?query={}'.format(query))

    expected = {
        'data': {
            'allUsers': {
                'edges': [
                    {'node': {'username': 'luke'}},
                    {'node': {'username': 'bob'}}]
            }
        }
    }
    assert response.json == expected
