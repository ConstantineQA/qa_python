from main import BooksCollector
import pytest
# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        # проверяем, что добавилось именно две
        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize(
            'positive_name',
            [
                'книга стандартная',
                'Сказочная история путешествия во времени',
                '1'
            ]
    )
    #позитивные проверки для добавления книги по длине ее названия
    def test_add_new_book_boundary_values_add_positive_values_name(self, positive_name):
        collector = BooksCollector()
        collector.add_new_book(positive_name)
        assert positive_name in collector.books_genre

    @pytest.mark.parametrize(
            'negative_name',
            [
                '',
                'История длинного путешествия по вселенной',
            ]
    )
    #негативные проверки для добавления книги по длине ее названия
    def test_add_new_book_boundary_no_add_negative_values_name(self, negative_name):
        collector = BooksCollector()
        collector.add_new_book(negative_name)
        assert negative_name not in collector.books_genre

    # проверяю, что метод устанавливает жанр из списка существующих
    def test_set_book_genre_set_existing_genre(self):
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.set_book_genre('1984', 'Детективы')
        assert collector.books_genre == {'1984':'Детективы'}

    # проверяю, что жанр получен по названию книги
    def test_get_book_genre_returns_genre_for_book_exists(self):
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.set_book_genre('1984', 'Детективы')
        assert collector.get_book_genre('1984') == 'Детективы'  

    #проверка, что по названию жанра выводятся только наименования книг с этим жанром
    def test_get_books_with_specific_genre_returns_books_specified_genre(self):
        collector = BooksCollector()
        collector.books_genre = {'1984': 'Комедии','Приключения кота': 'Детективы', 'Колобок': 'Детективы'}
        assert collector.get_books_with_specific_genre('Детективы') == ['Приключения кота', 'Колобок']

    #проверяю, что метод возвращает заполненный словарь books_genre
    #шаг collector.set_book_genre('1984', 'Детективы') оставлен намеренно, 
    #хотя можно было обойтись без него assert collector.get_books_genre() == {'1984': ''}
    #проверяю именно заполненный словарь
    def test_get_books_genre_return_dict(self):
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.set_book_genre('1984', 'Детективы')
        assert collector.get_books_genre() == {'1984': 'Детективы'}

    #проверяю, что метод возвращает наименования книг, которые имеют детский жанр
    def test_get_books_for_children_return_only_kids_books(self):
        collector = BooksCollector()
        collector.books_genre = {
            'книга1':'Комедии',
            'книга2': 'Ужасы',
            'книга3': 'Фантастика',
            'книга4': 'Детективы',
            'книга5': 'Мультфильмы'
        }
        assert collector.get_books_for_children() == ['книга1','книга3', 'книга5']

    def test_add_book_in_favorites_book_from_books_genre_added_in_favorites(self):
        collector = BooksCollector()
        collector.favorites = []
        collector.books_genre = {'книга1': 'Комедия'}
        collector.add_book_in_favorites('книга1')
        assert 'книга1' in collector.favorites

    def test_add_book_in_favorites_no_added_book_no_from_books_genre(self):
        collector = BooksCollector()
        collector.favorites = []
        collector.books_genre ={}
        collector.add_book_in_favorites('книга1')
        assert 'книга1' not in collector.favorites

    #проверяю, что в избранное добавлены книги без дублирования
    def test_add_book_in_favorites_no_duplicate_books_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('книга1')
        collector.add_book_in_favorites('книга1')
        collector.add_book_in_favorites('книга1')
        assert len(collector.favorites) == 1 

    #проверка что наименование удалено из избранного
    def test_delete_book_from_favorites_deleted_book_not_in_favorites(self):
        collector = BooksCollector()
        collector.favorites = ['книга1','книга3', 'книга5']
        collector.delete_book_from_favorites('книга1')
        assert 'книга1' not in collector.favorites

    #проверка что метод возвращает список избранных книг
    def test_get_list_of_favorites_books_return_favorites_books(self):
        collector = BooksCollector()
        collector.favorites = ['книга1','книга3', 'книга5']
        assert collector.get_list_of_favorites_books() == ['книга1','книга3', 'книга5']
