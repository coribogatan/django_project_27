import pytest
from django.contrib.auth import get_user_model
from django.test.client import Client
from books.models import Book
User = get_user_model()


def test_is_it_working():
    assert True == 1

# def test_should_fail():
#     assert True == False


def test_even_number():
    number = 10
    assert number%2 == 0


@pytest.mark.django_db
def test_create_user():
    user = User.objects.create_user(
        username="test123",
        password="password123"
    )
    assert user.username == "test123"

# fixture
@pytest.fixture
def logged_in_client(db, client: Client) -> Client:
    user = User.objects.create_user(
        username="test123",
        password="password123"
    )
    # vom crea un browser simulat, logat, care poate face request-uri HTTP:
    client.login(
        username="test123",
        password="password123"
    )

    return client

@pytest.fixture
def book(db):
    user = User.objects.create_user(
        username="useruser",
        password="password123"
    )
    b = Book.objects.create(title="testbook", author="Rowling", user=user)
    return b

def test_list_all_books(logged_in_client):
    # facem HTTP GET request:
    response = logged_in_client.get("/")

    assert response.status_code == 200


def test_does_book_exist(logged_in_client, book):
    # facem HTTP GET request:
    response = logged_in_client.get("/")

    assert response.status_code == 200
    assert "testbook" in str(response.content)
























