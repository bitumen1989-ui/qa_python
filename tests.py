import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    # Тесты add_new_book
    @pytest.mark.parametrize(
        "names,expected_books_genre",
        [
            (("Книга 1", "Книга 2"), {"Книга 1": "", "Книга 2": ""}),
            (("Книга",), {"Книга": ""}),
            (("a" * 40,), {"a" * 40: ""}),      
        ],
    )
    def test_add_new_book_valid_names(self, names, expected_books_genre):
        collector = BooksCollector()

        for name in names:
            collector.add_new_book(name)

        assert collector.books_genre == expected_books_genre

        for name in expected_books_genre:
            assert collector.get_book_genre(name) == ""

    @pytest.mark.parametrize(
        "names",
        [
            ("",),
            ("a" * 41,),
        ],
    )
    def test_add_new_book_invalid_names(self, names):
        collector = BooksCollector()

        for name in names:
            collector.add_new_book(name)

        assert collector.books_genre == {}


    # Тесты set_book_genre
    @pytest.mark.parametrize(
        "genre,expected_genre",
        [
            ("Фантастика", "Фантастика"),
            ("Ужасы", "Ужасы"),
            ("Роман", ""),
            ("", ""),
        ],
    )
    def test_set_book_genre_existing_book(self, genre, expected_genre):
        collector = BooksCollector()
        name = "Книга"
        collector.add_new_book(name)

        collector.set_book_genre(name, genre)

        assert collector.books_genre[name] == expected_genre


    def test_set_book_genre_non_existing_book(self):
        collector = BooksCollector()
        name = "Книга"

        collector.set_book_genre(name, "Фантастика")

        assert collector.books_genre == {}

    # Тесты get_book_genre 
    def test_get_book_genre_existing_with_genre(self):
        collector = BooksCollector()
        name = "Книга"
        collector.add_new_book(name)
        collector.set_book_genre(name, "Фантастика")

        assert collector.get_book_genre(name) == "Фантастика"


    def test_get_book_genre_existing_without_genre(self):
        collector = BooksCollector()
        name = "Книга"
        collector.add_new_book(name)

        assert collector.get_book_genre(name) == ""


    def test_get_book_genre_non_existing(self):
        collector = BooksCollector()
        name = "Книга"

        assert collector.get_book_genre(name) is None


    # Тесты get_books_with_specific_genre
    def test_get_books_with_specific_genre_found(self):
        collector = BooksCollector()
        collector.add_new_book("А")
        collector.set_book_genre("А", "Фантастика")
        collector.add_new_book("Б")
        collector.set_book_genre("Б", "Ужасы")
        collector.add_new_book("В")
        collector.set_book_genre("В", "Фантастика")

        result = collector.get_books_with_specific_genre("Фантастика")

        assert sorted(result) == ["А", "В"]

    @pytest.mark.parametrize(
        "setup_books,genre",
        [
            ({"А": "Ужасы"}, "Фантастика"),  # книги есть, но с другим жанром
            ({}, "Фантастика"),               # книг вообще нет
            ({"А": "Фантастика"}, "Роман"),   # жанр фильтрации не существует
        ],
    )
    def test_get_books_with_specific_genre_not_found(self, setup_books, genre):
        collector = BooksCollector()

        for name, book_genre in setup_books.items():
            collector.add_new_book(name)
            collector.set_book_genre(name, book_genre)

        assert collector.get_books_with_specific_genre(genre) == []

    def test_get_books_genre(self):
        collector = BooksCollector()

        collector.add_new_book("Книга")
        collector.set_book_genre("Книга", "Фантастика")

        collector.add_new_book("Без жанра")

        assert collector.get_books_genre() == {
            "Книга": "Фантастика",
            "Без жанра": "",
        }


    def test_get_books_for_children(self):
        collector = BooksCollector()

        collector.add_new_book("Детская")
        collector.set_book_genre("Детская", "Мультфильмы")

        collector.add_new_book("Ужасы")
        collector.set_book_genre("Ужасы", "Ужасы")

        collector.add_new_book("Детектив")
        collector.set_book_genre("Детектив", "Детективы")

        collector.add_new_book("Без жанра")

        children_books = collector.get_books_for_children()

        assert children_books == ["Детская"]
        assert "Ужасы" not in children_books
        assert "Детектив" not in children_books

    def test_add_book_in_favorites(self):
        collector = BooksCollector()

        collector.add_new_book("Книга")

        collector.add_book_in_favorites("Несуществующая книга")
        collector.add_book_in_favorites("Книга")
        collector.add_book_in_favorites("Книга")

        assert collector.get_list_of_favorites_books() == ["Книга"]

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()

        collector.add_new_book("Книга")
        collector.add_book_in_favorites("Книга")

        collector.delete_book_from_favorites("Несуществующая книга")
        collector.delete_book_from_favorites("Книга")

        assert collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()

        collector.add_new_book("Книга 1")
        collector.add_new_book("Книга 2")

        collector.add_book_in_favorites("Книга 1")
        collector.add_book_in_favorites("Книга 2")

        collector.delete_book_from_favorites("Книга 1")

        assert collector.get_list_of_favorites_books() == ["Книга 2"]    