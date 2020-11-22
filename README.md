# fyndHackingChallenge_IMDB

##Project Setup and Run
```
python3 -m virtualenv env
pip install -r requirements.txt
python manage.py migrate
python manage.py populate_movies
python manage.py runserver
```

At base url, i.e. http://127.0.0.1:8000/, you'll see the url for movie data
GET with id: 127.0.0.1:8000/imdb/1/
