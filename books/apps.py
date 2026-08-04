from django.apps import AppConfig


class BooksConfig(AppConfig):
    name = 'books'

    def ready(self):
        # register signal after django setup is done.
        import books.signals
