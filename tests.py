import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    @pytest.mark.parametrize(
        "names,expected_books_genre",
        [
            (
                ("Книга 1", "Книга 2"),
                {"Книга 1": "", "Книга 2": ""},
            ),
            (
                ("Книга",),
                {"Книга": ""},
            ),
            (
                ("a" * 40,),
                {"a" * 40: ""},
            ),
            (
                ("",),
                {},
            ),
            (
                ("a" * 41,),
                {},
            ),
            (
                ("Книга", "", "a" * 41),
                {"Книга": ""},
            ),
        ],
    )
    def test_add_new_book(self, names, expected_books_genre):
        collector = BooksCollector()

        for name in names:
            collector.add_new_book(name)

        assert collector.books_genre == expected_books_genre

        for name in expected_books_genre:
            assert collector.get_book_genre(name) == ""

    @pytest.mark.parametrize(
        "book_exists,genre,expected_books_genre",
        [
            (True, "Фантастика", {"Книга": "Фантастика"}),
            (True, "Ужасы", {"Книга": "Ужасы"}),
            (True, "Роман", {"Книга": ""}),
            (True, "", {"Книга": ""}),
            (False, "Фантастика", {}),
        ],
    )
    def test_set_book_genre(self, book_exists, genre, expected_books_genre):
        collector = BooksCollector()
        name = "Книга"

        if book_exists:
            collector.add_new_book(name)

        collector.set_book_genre(name, genre)

        assert collector.books_genre == expected_books_genre

    @pytest.mark.parametrize(
        "book_exists,setup_genre,expected",
        [
            (True, "Фантастика", "Фантастика"),
            (True, "", ""),
            (False, None, None),
        ],
    )
    def test_get_book_genre(self, book_exists, setup_genre, expected):
        collector = BooksCollector()
        name = "Книга"

        if book_exists:
            collector.add_new_book(name)

            if setup_genre:
                collector.set_book_genre(name, setup_genre)

        assert collector.get_book_genre(name) == expected

    @pytest.mark.parametrize(
        "books,genre,expected",
        [
            (
                (("А", "Фантастика"), ("Б", "Ужасы"), ("В", "Фантастика")),
                "Фантастика",
                ["А", "В"],
            ),
            (
                (("А", "Ужасы"),),
                "Фантастика",
                [],
            ),
            (
                (),
                "Фантастика",
                [],
            ),
            (
                (("А", "Фантастика"),),
                "Роман",
                [],
            ),
        ],
    )
    def test_get_books_with_specific_genre(self, books, genre, expected):
        collector = BooksCollector()

        for name, book_genre in books:
            collector.add_new_book(name)

            if book_genre:
                collector.set_book_genre(name, book_genre)

        assert sorted(collector.get_books_with_specific_genre(genre)) == expected

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