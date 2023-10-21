# csv

Работа Дубина Дмитрия Олеговича

Для запуска

1. Сделайте Pull
2. Создайте .env файл со следующей структурой

DB_HOST = postgresql
DB_PORT = 5432
POSTGRES_DB = csv
POSTGRES_USER = csv_admin
POSTGRES_PASSWORD = 7140043

SECRET_KEY = eyGLe5*13F!u5yEFfu,5ci6iE;_vd6'cS7p.fm2gd$eypG`T'07aH?c5+Q[
JWT_ALGORITHM = HS256
SWAGGER_URL = /api

VITE_APP_OUTPUT_PORT = 80
VITE_APP_API_OUTPUT_PORT = 90

3. Запустите командой docker-compose up --build
4. После превого запуска перейдите по ссылке localhost:90/user/init
Будет создано два пользователя

login: admin@admin.ru
passsword: admin

login: user@user.ru
passsword: user
