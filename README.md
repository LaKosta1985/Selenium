#### Python скрипт для проверки сценария покупки товара на сайте

#### Задание:

Создать автоматический e2e тест для проверки сценария покупки товара на сайте saucedemo.com с использованием Python + Selenium.

#### Сценарий теста:

Тест должен выполнять следующие действия на сайте saucedemo.com:

1. Авторизация: Использовать тестовый аккаунт:
   > Логин: standard_user
   > Пароль: secret_sauce
2. Выбор товара: Выбрать один товар (например, "Sauce Labs Backpack") и добавить его в корзину.
3. Оформление покупки:
   Перейти в корзину и убедиться, что товар добавлен.
   Оформить покупку, заполнив поля
4. Завершить покупку.
   Проверка: Убедиться, что покупка завершена успешно.

#### Последовательность действий:

1. Клонируйте репозиторий:
   git clone https://github.com/LaKosta1985/Selenium
   cd github-api-test
2. Установите зависимости
   pip install -r requirements.txt
3. Запустите скрипт
   python test_searche.py c помощью команды pytest -s в терминале(-s флаг для вывода ошибок в консоль).
4. Тест автоматически проверит все условия сценария.
