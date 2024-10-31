import pytest
from app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_greet_default(client):
    response = client.get('/api/greet')
    assert response.status_code == 200
    assert response.json['message'] == 'Hello, World!'


def test_greet_name(client):
    response = client.get('/api/greet?name=John')
    assert response.status_code == 200
    assert response.json['message'] == 'Hello, John!'
