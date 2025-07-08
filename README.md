Create virtual environment
```
python -m venv venv
```

activate venv (bash)
```
source venv/scripts/activate
```

install requirements
```
pip install -r requirements.txt
```

create super user to access admin panel (/admin)
```
python manage.py createsuperuser
```

run migrasi
```
python manage.py migrate
```

run server
```
python manage.py runserver
```
