# diplom_3
UI-тесты для сервиса Stellar Burgers 
https://stellarburgers.nomoreparties.site/

Репозиторий содержит UI-автотесты для проверки функциональности сервиса "Stellar Burgers" 
Код тестов находится в директории /tests.

Структура проекта
Фикстуры: Тесты используют фикстуры из файла conftest.py.

Локаторы описаны в файле locators.py.

Файлы с классами страниц лежат в директории pages

Зависимости
Внешние зависимости указаны в requirements.txt 

Генерация отчетов
Для создания  отчетов о тестировании используется фреймворк Allure.  


Как запустить тесты:
Установка зависимостей

$ pip install -r requirements.txt

Запуск всех тестов одной командой

pytest -v

Allure-отчет о тестировании 

allure serve allure_results
pytest -v tests.py
