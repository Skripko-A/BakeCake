# BakeCake Project

Проект BakeCake - это веб-приложение для заказа кастомных тортов. Приложение позволяет пользователям выбирать различные параметры торта, такие как форма, начинка, ягоды, декор и т.д., и делать заказ через веб-интерфейс.

## Установка

1. Клонируйте репозиторий:
    ```bash
    git clone https://github.com/Skripko-A/BakeCake.git
    ```

2. Перейдите в директорию проекта:
    ```bash
    cd BakeCake
    ```

3. Установите зависимости:
    ```bash
    pip install -r requirements.txt
    ```

4. Выполните миграции базы данных:
    ```bash
    python manage.py migrate
    ```

5. Запустите сервер разработки:
    ```bash
    python manage.py runserver
    ```

## Основные функции

### Основная страница

На главной странице (`index.html`) пользователи могут выбрать параметры для создания кастомного торта. Доступны следующие параметры:
- Уровни
- Форма
- Начинка
- Ягоды
- Декор

### Каталог тортов

Пользователи могут просматривать каталог готовых тортов на странице `cakes_catalog.html`. Каждый торт включает изображение, описание и цену.

### Страница торта

На странице каждого торта (`cake_page.html`) пользователи могут видеть подробную информацию о торте и делать заказ.

### Личный кабинет

Пользователи могут просматривать свои заказы в личном кабинете (`lk.html`).

## Модели

Проект использует следующие модели:
- `Cake`: Модель для хранения информации о тортах.
- `Topping`: Модель для хранения информации о начинках.
- `Berry`: Модель для хранения информации о ягодах.
- `Decor`: Модель для хранения информации о декоре.
- `Layer`: Модель для хранения информации об уровнях торта.
- `Shape`: Модель для хранения информации о формах торта.
- `Order`: Модель для хранения информации о заказах.

## Формы

Проект использует Django формы для обработки данных заказов:
- `OrderRegularCakeForm`: Форма для оформления заказа на готовый торт.

## Важные функции

### Создание кастомного заказа на торт

Функция `create_custom_cake_order` обрабатывает POST-запросы на создание кастомного заказа. Она получает данные пользователя и параметры торта, сохраняет их в базе данных и отображает страницу успеха заказа.

### Создание заказа на готовый торт

Функция `create_regular_cake_order` обрабатывает POST-запросы на создание заказа на готовый торт. Она получает данные заказа из формы, сохраняет их в базе данных и