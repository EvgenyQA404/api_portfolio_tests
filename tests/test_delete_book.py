import random
import pytest
import requests
import allure
from data.helpers import headers_for_get_books
from data.urls import books_url
from data.variables import ok, bad_request


@pytest.fixture
def random_book_id():
    # вернуть значение id книги от 1 до 100
    return random.randint(1, 100)


@allure.parent_suite("Автоматизация API")
@allure.suite("Примеры тестов API")
@allure.sub_suite("Проверка удаления книги")
class TestDeleteBook:
    @allure.description('Проверка соответсвия статуса')
    @allure.title('Удалить книгу - корректные значения')
    def test_delete_correctly_book(self, random_book_id):
        response = requests.delete(books_url + '/' + str(random_book_id), headers=headers_for_get_books)

        assert ok == response.status_code

    @allure.description('Проверка соответсвия статуса')
    @allure.title('Удалить книгу - некорректные значения')
    def test_delete_not_correctly_book(self):
        response = requests.delete(books_url + '/test', headers=headers_for_get_books)

        assert bad_request == response.status_code
