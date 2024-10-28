# int4_cicd
## Для запуска:
1. Склонируйте репу
```git clone https://github.com/artias13/int4_cicd```
2. Соберите образ
```docker build -t webserver .```
3. Запустите образ
```docker run -p 8225:8225 webserver```
4. Отправьте запрос
```curl localhost:8225/healthz```
