# Disaster Alert App

### To setup the project:
```shell
  git clone https://github.com/YashChaudharyBz/DisasterAlertApp.git
  cd DisasterAlertApp
  pip install asgiref==3.7.2 channels==4.0.0 Django==4.2.7 django-crispy-forms==2.1 django-environ==0.11.2 geopy==2.4.1 gunicorn==21.2.0 python-decouple==3.8 pytz==2023.3 sqlparse==0.4.4 whitenoise==6.6.0
  python manage.py makemigrations alerts
  python manage.py migrate
```

### To use the app:
```shell
  python manage.py runserver
```
