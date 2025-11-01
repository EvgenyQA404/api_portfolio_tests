import pytest
import requests
import allure
import random
from data.urls import books_url
from data.variables import ok
from data.helpers import headers_for_get_books


@pytest.fixture
def random_book_id():
    # вернуть значение id книги от 1 до 100
    return random.randint(1, 100)


@allure.parent_suite("Автоматизация API")
@allure.suite("Примеры тестов API")
@allure.sub_suite("Проверка получения одной конкретной книги")
class TestGetOneBook:
    @allure.description('Проверка соответсвия статуса и id книги')
    @allure.title('Получить одну книгу')
    def test_get_one_book(self, random_book_id):
        response = requests.get(books_url + '/' + str(random_book_id), headers=headers_for_get_books)
        payload = response.json()

        assert ok == response.status_code and random_book_id == payload['id']
