# Flask Ads API

Проект — простой REST API для управления объявлениями. Реализован на Flask. В качестве базы данных используется PostgreSQL.

---

## Возможности

- Создание, получение и удаление объявлений

---

## Как запустить
1. Склонируйте репозиторий:
    ```bash
    git clone https://github.com/yourusername/flask_ads_api.git
    cd flask_ads_api
    ```
2. Создайте и активируйте виртуальное окружение:
    ```bash
    POSTGRES_USER=USER
    POSTGRES_PASSWORD=PASSWORD
    POSTGRES_DB=DB_NAME
    DATABASE_URL=postgresql+psycopg2://USER:PASSWORD@db:5432/DB_NAME
   ```
3. Запустите проект:
    ```bash
    docker-compose up --build
    ```
   
После запуска:
- API будет доступен на http://localhost:5000
- База данных — на localhost:5432

---

## Примеры запросов


### Создать объявление

```bash
POST /ads/
Content-Type: application/json
{
  "title": "Продам велосипед",
  "description": "Горный велосипед, отличное состояние",
  "owner": "Иван Иванов"
}
```


### Получить объявление по ID

```bash
GET http://127.0.0.1:5000/ads/1
```

### Удалить объявление по ID

```bash
DELETE http://127.0.0.1:5000/ads/1
```

---
# Лицензия

Пока что ее нет :D