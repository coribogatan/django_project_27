import pytest
from django.contrib.auth import get_user_model
from django.test.client import Client
from django.urls import reverse

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
    assert user.check_password("password123")

# fixture

@pytest.fixture
def user(db) -> User:
    u = User.objects.create_user(
        username="test123",
        password="password123"
    )
    return u

@pytest.fixture
def logged_in_client(user, client: Client) -> Client:
    # vom crea un browser simulat, logat, care poate face request-uri HTTP:
    client.login(
        username="test123",
        password="password123"
    )

    return client

@pytest.fixture
def book(user):
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


def test_user_book_count(user):
    book1 = Book.objects.create(title="book1", author="author1", user=user)
    book2 = Book.objects.create(title="book2", author="author2", user=user)
    books = list(Book.objects.filter(user_id=user.pk))
    assert len(books) == 2

def test_user_book_count_html(user, client):
    book1 = Book.objects.create(title="book1", author="author1", user=user)
    book2 = Book.objects.create(title="book2", author="author2", user=user)
    book3 = Book.objects.create(title="book3", author="author3", user=user)

    response = client.get("/")
    assert response.status_code == 200
    main_page_text = str(response.content)
    assert main_page_text.count(f"/user/{user.pk}/books") == 3

def test_delete_book(user, book, logged_in_client: Client):
    #conceptual:
    #HTTP POST request pe url /delete_book/{book.id}/
    response = logged_in_client.post(f"/delete_book/{book.pk}/")
    assert response.status_code == 302

    response = logged_in_client.post(f"/delete_book/{book.pk}/")
    assert response.status_code == 404


def test_api_get_books(book, logged_in_client: Client):
    url_1 = "/api/v1/books/"
    response = logged_in_client.get(url_1)
    json_response = response.json()
    assert response.status_code == 200
    assert json_response[0]["id"] == book.pk


def test_api_get_individual_book(book, logged_in_client: Client):
    # "api/v1/books/<int:pk>/"
    url_1 = f"/api/v1/books/{book.pk}/"
    url_2 = reverse("api_book_detail", kwargs={"pk": book.pk})
    response = logged_in_client.get(url_2)
    json_response = response.json()
    assert response.status_code == 200
    assert json_response["id"] == book.pk

























