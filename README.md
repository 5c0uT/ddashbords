1. Склонируйте репозиторий:
```bash
git clone https://github.com/5c0uT/ddashbords.git
cd ddashbords/project
```

2. Создайте файл .env на основе примера:
```bash
cp .env.example .env
```

Заполните реальными значениями:
```bash
SECRET_KEY=super-secret-key
ALGORITHM=HS256
DATABASE_URL=postgresql://user:password@postgres:5432/dbname
REDIS_URL=redis://redis:6379
```

3. Запустите сервисы через Docker Compose:
```bash
docker-compose up -d
```

4. Приложение будет доступно по адресу:
- API: http://localhost:8000
- Grafana: http://localhost:3000 (логин/пароль по умолчанию: admin/admin)

### 3. Примеры запросов:

Регистрация пользователя:
```bash
curl -X POST "http://localhost:8000/register" -H "Content-Type: application/json" -d '{"login":"user1", "password":"pass"}'
```

Логин:
```bash
curl -X POST "http://localhost:8000/login" -H "Content-Type: application/json" -d '{"login":"user1", "password":"pass"}'
```

Создание автомобиля (используйте токен из ответа):
```bash
curl -X POST "http://localhost:8000/avto/" -H "Authorization: Bearer <ваш-токен>" -H "Content-Type: application/json" -d '{"brand":"Toyota", "model":"Camry", "year":2020}'
```

Получение информации об автомобиле:
```bash
curl -X GET "http://localhost:8000/avto/1" -H "Authorization: Bearer <ваш-токен>"
```
