# qa_python
Тесты покрывают следующие методы класса `BooksCollector`:
 `add_new_book_valid_names`  добавление одной или нескольких книг, 
 `add_new_book_invalid_names` игнорирование пустого имени, игнорирование имени длиннее 40 символов 
 `test_set_book_genre_existing_book`  установка жанра существующей книге, установка только допустимых жанров 
 `test_set_book_genre_non_existing_book` поведение при несуществующей книге
 `test_get_book_genre_existing_with_genre` получение жанра существующей книги
 `test_get_book_genre_existing_without_genre` пустой жанр
 `test_get_book_genre_non_existing` возврат `None` для несуществующей книги 
 `test_get_books_with_specific_genre_found`  поиск книг по указанному жанру, позитивный тест, есть книги с нужным жанром
 `test_get_books_with_specific_genre_not_found` писк книг по указанному жанру, негативный тест, нету книг с нужным жанром
 `get_books_genre`  получение словаря со всеми книгами и их жанрами 
 `get_books_for_children`  получение списка книг, подходящих для детей 
 `add_book_in_favorites`  добавление книги в избранное, игнорирование несуществующих книг, отсутствие дубликатов 
 `delete_book_from_favorites`  удаление книги из избранного, игнорирование несуществующих книг 
 `get_list_of_favorites_books`  получение актуального списка избранных книг 