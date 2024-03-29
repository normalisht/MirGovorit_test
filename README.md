# MirGovorit_test


## Запуск проекта

На основе файла `.env.example` необходимо создать 
файл `.env` (можно просто переименовать)

Для запуска необходимо [установить docker](https://docs.docker.com/engine/install/) 

После установки докера выполнить следующие команды
```bash
docker build -t mir_govorit_app .
```
```bash
docker run --name mir_govorit_app_container -p 8000:8000 -d mir_govorit_app
```

После запуска контейнера переходим на сайт http://127.0.0.1:8000/admin

Необходимо создать несколько блюд и 
ингредиентов для дальнейшей проверки проекта

#### Данные для входа в админку

username: admin

password: admin


### Функционал проекта
```http request
GET http://127.0.0.1:8000/cook_recipe/?recipe_id=<int>
```
Увеличивает на единицу количество приготовленных блюд для каждого
продукта, входящего в указанный рецепт.


```http request
GET http://127.0.0.1:8000/show_recipes_without_product/?product_id=<int>
```
Возвращает HTML страницу, на которой размещена таблица. 
В таблице отображены id и названия всех рецептов, 
в которых указанный продукт отсутствует, или присутствует 
в количестве меньше 10 грамм.

```http request
GET http://127.0.0.1:8000/add_product_to_recipe/?recipe_id=<int>&product_id=<int>&weight=<int>
```
Функция добавляет к указанному рецепту указанный продукт с указанным весом. 
Если в рецепте уже есть такой продукт, то функция 
меняет его вес в этом рецепте на указанный.


# Для запуска без докера

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cd mir_govorit
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```