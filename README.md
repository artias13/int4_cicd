# int4_cicd
## Для запуска:
1. Склонируйте репу
```git clone https://github.com/artias13/int4_cicd```
2. Создайте .env
3. Соберите образ
```docker build -t webserver .```
4. Запустите образ
```docker run -p 8225:8225 webserver```
5. Отправьте запрос
```curl localhost:8225/healthz```
