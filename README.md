### Автотесты для проверки API, сваггер - https://fakerestapi.azurewebsites.net/index.html

### Реализованные сценарии

Созданы несколько API-тестов для примера структуры и архитектуры автотестов.

Использованы методы: GET, POST, PUT, DELETE

Процент выполненных API-тестов 100% (отчет allure в виде скриншота: Allure_API.jpg)

### Структура проекта

- `data` - папка, содержащая различные тестовые данные.
- `tests` - пакет, содержащий тесты.

### Запуск автотестов

**Установка зависимостей**

> `$ pip install -r requirements.txt`

**Запуск автотестов и генерация allure отчета о прохождении тестов**

>  `$ pytest .\tests --alluredir=allure_results --clean-alluredir`
>
>  `$ allure serve allure_results`
