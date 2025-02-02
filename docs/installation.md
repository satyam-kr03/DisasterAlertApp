# Project Setup Instructions

## 1. Clone the Repository

```shell
git clone https://github.com/YashChaudharyBz/DisasterAlertApp.git && cd DisasterAlertApp
```

## 2. Create and Activate Virtual Environment

First, create the virtual environment:

```shell
python -m venv venv
```

Then activate it:

**For Linux/Mac:**

```shell
source venv/bin/activate
```

**For Windows:**

```shell
.\venv\Scripts\activate
```

## 3. Install Dependencies

```shell
pip install -r requirements.txt
```

## 4. Setup Database

```shell
python manage.py makemigrations alerts
python manage.py migrate
```

## 5. Start Development Server

```shell
python manage.py runserver
```

Once the server is running, visit http://localhost:8000 in your browser to access the application.
