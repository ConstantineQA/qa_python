# Sprint_4

## Методы класса BooksCollector и юнит-тесты для них
### add_new_book()
1. **test_add_new_book_add_two_books**  - Проверяем, что добавлено именно 2 книги в словарь books_genre
2. **test_add_new_book_boundary_values_add_positive_values_name** - Проверяем, что книги с названием состоящими из символов в кол-ве от 1 до 40 включительно можно добавить в словарь books_genre
3. **test_add_new_book_boundary_no_add_negative_values_name** - Проверяем, что книги с названием из 0 символов(пустая строка) или с названием состоящим из 41 символа добавить в словарь books_genre нельзя
### set_book_genre()
1. **test_set_book_genre_set_existing_genre** - Проверка, что метод устанавливает жанр книге из списка существующих жанров в genre
### get_book_genre()
1. **test_get_book_genre_returns_genre_for_book_exists** - Проверка, что метод возвращает жанр по названию книги
### get_books_with_specific_genre()
1. **test_get_books_with_specific_genre_returns_books_specified_genre** - Проверка, что по названию жанра метод возвращает только наименования книг с этим жанром
### get_books_genre()
1. **test_get_books_genre_return_dict** - Проверка, что метод возвращает словарь 
### test_get_books_for_children()
1. **test_get_books_for_children_return_only_kids_books** - Проверка, что метод возвращает наименования книг, которым присвоен детский жанр(не входящий в genre_age_rating)
### test_add_book_in_favorites()
1. **test_add_book_in_favorites_book_from_books_genre_added_in_favorites** - проверка, что метод добавляет в избранное книгу, если она есть в словаре books_genre
2. **test_add_book_in_favorites_no_added_book_no_from_books_genre** - Проверка, что нельзя добавить в избранное книгу, котрую ранее не добавили в books_genre
3. **def test_add_book_in_favorites_no_duplicate_books_in_favorites** - Проверка, что в избранное одну и ту же книгу можно добавить один раз
### delete_book_from_favorites()
1. **test_delete_book_from_favorites_deleted_book_not_in_favorites** - проверка, что метод удаляет наименование книги из избранного
2. **test_delete_book_from_favorites_one_book_was_deleted** - Проверка, что длина списка уменьшается именно на 1 после удаления книги из избранного
### get_list_of_favorites()
1. **test_get_list_of_favorites_books_return_favorites_books** - проверка, что метод возвращает список названий книг из избранного
