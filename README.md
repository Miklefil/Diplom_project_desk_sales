# Ads board - доска обьявлений.

## Описание

Проект представляет собой backend-часть для сайта объявлений. 
Предполагает реализацию следующего функционала:

- Авторизация и аутентификация пользователей.
- Распределение ролей между пользователями (пользователь и админ).
- CRUD для объявлений на сайте (админ может удалять или редактировать все объявления, а пользователи только свои).
- Под каждым объявлением пользователи могут оставлять отзывы.
- В заголовке сайта можно осуществлять поиск объявлений по названию.


## Подготовка к работе с проектом

### Шаг 1: Клонирование проекта
1. Зайти в терминал
2. С помощью команды `cd` перейти в директорию, где будет находиться проект
3. Клонировать проект
```bash
git clone https://github.com/Miklefil/Diplom_project_desk_sales.git
```

### Шаг 2: Настройка окружения
1. В директории проекта создать файл `.env`

3. Записать в файл следующие настройки
```bash
POSTGRES_DB=название базы данных (skymarket)
POSTGRES_USER=имя пользователя (postgres)
POSTGRES_PASSWORD=пароль
POSTGRES_HOST = db
POSTGRES_PORT=5432
```
*В проекте есть шаблон файла .env - `.env_example`

### Шаг 3: Создание образа и запуск проекта
Выполнить команду в терминале
```bash
docker-compose up --build  
```


### Шаг 4: Загрузка данных
Выполнить команды
```bash
docker-compose exec app python3 manage.py loaddata users.json
docker-compose exec app python3 manage.py loaddata ad.json
docker-compose exec app python3 manage.py loaddata comments.json
```

## Запуск тестов

### Для запуска тестов выполнить команду
```bash
docker-compose exec app coverage3 run --source='.' manage.py test

```
### Для просмотра результата покрытия тестами выполнить команду
```bash
docker-compose exec app coverage report

 *coverage_result.png - в корне проекта
```

## Работа с сервисом через Postman

1. Получить токен
```bash
POST: http://localhost:8000/api/token/
body: {
  "email": <электронная почта>,
  "password": <пароль>
  }
```
2. Подключить авторизацию по токену

3. Эндпоинты:

- Создание объявления
```bash
POST: http://localhost:8000/api/ads/
body: {
    "title": "Компьютер недорого",
    "price": 10000,
    "description": "Компьютер недорого"
  } 
  
      *image, created_at - необязательны для заполнения 
```

- Просмотр детальной информации об объявлении
```bash
GET: http://localhost:8000/api/ads/<id_объявления>/
```
- Просмотр всех объявлений
```bash
GET: http://localhost:8000/api/ads/
```
- Редактирование объявления
```bash
PUT: http://localhost:8000/api/ads/<id_объявления>/
PATCH: http://localhost:8000/api/ads/<id_объявления>/
```
- Удаление объявления
```bash
DELETE: http://localhost:8000/api/ads/<id_объявления>/
```
- Просмотр отзывов определенного объявления
```bash
GET: http://localhost:8000/api/ads/<id_объявления>/comments
```
- Просмотр конкретного отзыва определенного объявления
```bash
GET: http://localhost:8000/api/ads/<id_объявления>/comments/<id_отзыва>/
```
- Изменение отзыва
```bash
PUT: http://localhost:8000/api/ads/<id_объявления>/comments/<id_отзыва>/
PATCH: http://localhost:8000/api/ads/<id_объявления>/comments/<id_отзыва>/
```
- Удаление отзыва
```bash
DELETE: http://localhost:8000/api/ads/<id_объявления>/comments/<id_отзыва>/
```

## Просмотр документации
### Swagger
```bash
http://localhost:8000/swagger/
```
### Redoc
```bash
http://localhost:8000/redoc/
```