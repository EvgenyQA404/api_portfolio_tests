import random
import pytest
import requests
import allure
from data.helpers import headers_for_add_book
from data.variables import ok
from data.test_data import change_title
from data.urls import books_url


@pytest.fixture
def random_book_id():
    # вернуть значение id книги от 1 до 100
    return random.randint(1, 100)


@allure.parent_suite("Автоматизация API")
@allure.suite("Примеры тестов API")
@allure.sub_suite("Проверка смены названия книги")
class TestChangeTitleBook:
    @allure.description('Проверка соответсвия статуса и нового названия в теле ответа')
    @allure.title('Изменить название книги')
    def test_change_title_of_book(self, random_book_id):
        response = requests.put(books_url + '/' + str(random_book_id), headers=headers_for_add_book, json=change_title)
        payload = response.json()

        assert ok == response.status_code and 'Book 255' == payload['title']
