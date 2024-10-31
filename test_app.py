import pytest
from app import app as flask_app


@pytest.fixture
def app():
    app = flask_app
    app.config['TESTING'] = True
    yield app


@pytest.fixture
def client(app):
    return app.test_client()


def test_registration_page(client):
    response = client.get('/')
    assert b'Регистрация' in response.data
    assert b'Имя пользователя:' in response.data
    assert b'Пароль:' in response.data


def test_successful_registration(client):
    response = client.post('/', data={'username': 'testuser', 'password': 'password'})
    assert response.status_code == 302  # Проверяем редирект
    assert b'Регистрация прошла успешно!' in response.data


def test_failed_registration(client):
    response = client.post('/', data={'username': '', 'password': ''})
    assert response.status_code == 200  # Проверяем, что страница не редиректит
    assert b'Пожалуйста, заполните все поля.' in response.data
