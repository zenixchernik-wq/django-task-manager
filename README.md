# Django Task Manager

Учебный backend-проект на Django для управления задачами и профилями пользователей.

## Возможности проекта

### Пользователи
- регистрация
- вход и выход из аккаунта
- ограничение доступа к отдельным действиям для неавторизованных пользователей

### Профили
- создание профиля
- просмотр профиля
- загрузка аватара
- поиск профилей по имени
- пагинация списка профилей

### Задачи
- создание задачи
- просмотр списка задач
- просмотр detail-страницы задачи
- редактирование задачи
- удаление задачи
- фильтрация выполненных задач
- фильтрация задач по категории

### Дополнительно
- категории задач
- теги задач
- работа с Django ORM
- работа с `ModelForm`
- загрузка изображений через `ImageField`

## Стек
- Python
- Django
- SQLite
- HTML
- CSS
- Pillow

## Что реализовано
- CRUD для задач
- аутентификация пользователей
- поиск через `request.GET`
- пагинация через `Paginator`
- загрузка изображений через `ImageField`
- связи между моделями:
  - `ForeignKey`
  - `ManyToManyField`

## Как запустить проект

### 1. Клонировать репозиторий
```bash
git clone https://github.com/zenixchernik-wq/django-task-manager.git
cd django-task-manager

2. Создать виртуальное окружение
python -m venv venv

3. Активировать виртуальное окружение
Windows
venv\Scripts\activate
Linux / macOS
source venv/bin/activate

4. Установить зависимости
pip install -r requirements.txt

5. Применить миграции
python manage.py makemigrations
python manage.py migrate

6. Создать суперпользователя
python manage.py createsuperuser

7. Запустить сервер
python manage.py runserver
