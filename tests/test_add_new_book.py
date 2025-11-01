import requests
import allure
from data.test_data import book
from data.urls import books_url
from data.helpers import headers_for_add_book, validation_error
from data.variables import bad_request, ok


@allure.parent_suite("Автоматизация API")
@allure.suite("Примеры тестов API")
@allure.sub_suite("Проверка добавления новой книги")
class TestAddBook:
    @allure.description('Проверка соответсвия статуса и полного тела ответа')
    @allure.title('Добавить книгу - корректные значения')
    def test_add_correctly_book(self):
        response = requests.post(books_url, headers=headers_for_add_book, json=book)
        payload = response.json()

        assert ok == response.status_code and book == payload

    @allure.description('Проверка соответсвия статуса и ошибки в теле ответа')
    @allure.title('Добавить книгу - некорректные значения')
    def test_add_not_correctly_book(self):
        response = requests.post(books_url, headers=headers_for_add_book)
        payload = response.json()

        assert bad_request == response.status_code and payload['title'] == validation_error
