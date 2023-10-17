<H1>DJANGO DRF</H1> 

Планировщик событый через telegram-bot

<H2>Установка</H2> 

- загрузить репозиторий
- Установить зависимости из файла requirements.txt (pip install -r requirements.txt)
- Запустить сервер Redis (service redis-server start)
- Подготовить .env файл (пример в .env_sample)
- Создать базу для postgres
- сделать миграции (python manage.py makemigrations/migrate)
- создать telegram bot для отправки сообщений
- run command /start in telegram bot

<H2>Старт</H2>

- run command: celery -A config worker -l INFO
- run command: celery -A config beat -l info -S django
- python manage.py runserver

<H2>API</H2>
<H4>API Документация</H4>
http://127.0.0.1:8000/redoc/

<H4>Работа с API (users)</H4>
http://127.0.0.1:8000/api/v1/users/show/ - показать всех пользователей
http://127.0.0.1:8000/api/v1/users/show/int:pk/ - детальная информация пользователя
http://127.0.0.1:8000/api/v1/users/update/int:pk/ - обновить пользователя
http://127.0.0.1:8000/api/v1/users/delete/int:pk/ - удалить пользователя
http://127.0.0.1:8000/api/v1/users/registration/ - регистрация пользователя
http://127.0.0.1:8000/api/v1/users/token/ - получить токен для пользователя
http://127.0.0.1:8000/api/v1/users/token/refresh/ - обновить токен

<H4>Работа с API (habits)</H4>
http://127.0.0.1:8000/api/v1/habits/ - показать все привычки пользователя
http://127.0.0.1:8000/api/v1/habit/int:pk/ - детальная информация привычки
http://127.0.0.1:8000/api/v1/habit/create/ - создать привычку    
http://127.0.0.1:8000/api/v1/habit/update/int:pk/ - обновить привычку
http://127.0.0.1:8000/api/v1/habit/delete/int:pk/ - удалить привычку   
http://127.0.0.1:8000/api/v1/share_habits/ -  показать все публичные привычки


<H2>Описание</H2>
place - место для привычки пользователя

action - исполнитель

award - награда

duration - продолжительность(не более 120 секунд)

is_public - публичность или приватность привычки

is_pleasant - полезность привычки

frequency - периодичность

time - время

link_pleasant - обычная (неприятная) привычка может иметь приятную привычку (в данном случае без награды)

<H3>Дополнение:</H3>

Автор: Болибок Олег
