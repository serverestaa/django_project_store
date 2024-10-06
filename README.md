
# Django Project Store

This is a Django-based e-commerce store that allows users to browse products, place orders, and manage their accounts. The project includes features like user authentication, product listings, order management, and an admin interface for managing the store.

## Features

- User authentication (login, registration)
- Product listing and filtering
- Order placement and management
- Admin panel for managing products, orders, and users
- REST API for accessing store data

## Installation

1. Clone the repository:
   ```
    git clone https://github.com/serverestaa/django_project_store.git
   ```

2.	Navigate to the project directory:
   ```
    cd django_project_store
   ```


3.	Install dependencies:
  ```
    pip install -r requirements.txt
  ```

4.	Apply migrations:
```
    python manage.py migrate
```

5.	Run the development server:
```
    python manage.py runserver
```


Project Structure
```
django_project_store/
├── api/
│   ├── __init__.py
│   ├── urls.py
│   └── views.py
├── common/
│   ├── __init__.py
│   └── utils.py
├── orders/
│   ├── __init__.py
│   ├── models.py
│   └── views.py
├── products/
│   ├── __init__.py
│   ├── models.py
│   └── views.py
├── static/
│   └── css/
│       └── styles.css
├── store/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── users/
│   ├── __init__.py
│   ├── models.py
│   └── views.py
├── manage.py
└── requirements.txt
```

4. Save the file, commit the changes, and push it to your GitHub repository.
