from django.http import HttpRequest, HttpResponse
import random

def home(request: HttpRequest):
    return HttpResponse("""
        <h1>Tema Books</h1>

        <a href="/tema_books/ordered_names/">
            <button>Ordered Names Ascending</button>
        </a>

        <a href="/tema_books/ordered_numbers/">
            <button>Ordered Numbers Descending</button>
        </a>

        <a href="/tema_books/paired_names/">
            <button>Paired Names</button>
        </a>
    """)


def ordered_names(request: HttpRequest):
    names = [
        "Andrei", "Maria", "Ion", "Elena", "Alexandru", "Ana",
        "Vasile", "Ioana", "George", "Gabriela", "Florin", "Mihai",
        "Diana", "Radu", "Laura", "Cristian", "Raluca",
        "Bianca",
    ]
    names = sorted(names)
    return HttpResponse("[" + ", ".join(f'"{name}"' for name in names) + "]")


def ordered_numbers(request: HttpRequest):
    numbers = [73, 28, 95, 14, 61, 39, 87, 5, 46, 32, 345, 232, 12, 33, 99, 96, 35, 1, 9, 10]
    numbers = sorted(numbers, reverse=True)
    return HttpResponse("[" + ", ".join(map(str, numbers)) + "]")


def paired_names(request: HttpRequest):
    names = [
        "Andrei", "Maria", "Ion", "Elena", "Alexandru", "Ana",
        "Vasile", "Ioana", "George", "Gabriela", "Florin", "Mihai",
        "Diana", "Radu", "Laura", "Cristian", "Raluca",
        "Bianca",
    ]

    numbers = [73, 28, 95, 14, 61, 39, 87, 5, 46, 32, 345, 232, 12, 33, 99, 96, 35, 1, 9, 10]

    data = [
        f'{{"name": "{name}", "count": {random.choice(numbers)}}}'
        for name in names
    ]

    return HttpResponse("[" + ", ".join(data) + "]")