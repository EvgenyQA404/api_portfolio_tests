import requests
import allure
from data.variables import ok
from data.urls import books_url
from data.helpers import headers_for_get_books, description_for_get_books, title_for_get_first_book, \
    title_for_get_last_book


@allure.parent_suite("Автоматизация API")
@allure.suite("Примеры тестов API")
@allure.sub_suite("Проверка получения всех книг")
class TestGetAllBooks:
    @allure.description('Проверка соответсвия статуса и названий первой и последней книг')
    @allure.title('Получить все книги')
    def test_get_all_books(self):
        response = requests.get(books_url, headers=headers_for_get_books)
        payload = response.json()

        assert ok == response.status_code and description_for_get_books == payload[0][
            'description'] and title_for_get_first_book == payload[0]['title'] and title_for_get_last_book == \
               payload[-1]['title']
