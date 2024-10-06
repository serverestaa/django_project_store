
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
.
├── api
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-39.pyc
│   │   ├── apps.cpython-39.pyc
│   │   ├── urls.cpython-39.pyc
│   │   └── views.cpython-39.pyc
│   ├── apps.py
│   ├── migrations
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       └── __init__.cpython-39.pyc
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── common
│   ├── __pycache__
│   │   └── views.cpython-39.pyc
│   └── views.py
├── manage.py
├── media
│   ├── products_images
│   │   ├── Adidas-hoodie.png
│   │   ├── Black-Dr-Martens-shoes.png
│   │   ├── Black-Nike-Heritage-backpack.png
│   │   ├── Blue-jacket-The-North-Face.png
│   │   ├── Brown-sports-oversized-top-ASOS-DESIGN.png
│   │   └── Dark-blue-wide-leg-ASOs-DESIGN-trousers.png
│   └── users_images
│       ├── wallpaperflare.com_wallpaper.jpg
│       └── wallpaperflare.com_wallpaper_cDbH5cr.jpg
├── orders
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-39.pyc
│   │   ├── admin.cpython-39.pyc
│   │   ├── apps.cpython-39.pyc
│   │   ├── forms.cpython-39.pyc
│   │   ├── models.cpython-39.pyc
│   │   ├── urls.cpython-39.pyc
│   │   └── views.cpython-39.pyc
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── 0001_initial.cpython-39.pyc
│   │       └── __init__.cpython-39.pyc
│   ├── models.py
│   ├── templates
│   │   └── orders
│   │       ├── canceled.html
│   │       ├── order-create.html
│   │       ├── order.html
│   │       ├── orders.html
│   │       └── success.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── products
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-39.pyc
│   │   ├── admin.cpython-39.pyc
│   │   ├── apps.cpython-39.pyc
│   │   ├── context_preprocessors.cpython-39.pyc
│   │   ├── models.cpython-39.pyc
│   │   ├── serializers.cpython-39.pyc
│   │   ├── urls.cpython-39.pyc
│   │   └── views.cpython-39.pyc
│   ├── admin.py
│   ├── apps.py
│   ├── context_preprocessors.py
│   ├── fixtures
│   │   ├── categories.json
│   │   └── goods.json
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── 0002_alter_product_price.py
│   │   ├── 0003_basket.py
│   │   ├── 0004_auto_20240930_1418.py
│   │   ├── 0005_product_stripe_product_price_id.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── 0001_initial.cpython-39.pyc
│   │       ├── 0002_alter_product_price.cpython-39.pyc
│   │       ├── 0003_basket.cpython-39.pyc
│   │       ├── 0004_auto_20240930_1418.cpython-39.pyc
│   │       ├── 0005_product_stripe_product_price_id.cpython-39.pyc
│   │       └── __init__.cpython-39.pyc
│   ├── models.py
│   ├── serializers.py
│   ├── templates
│   │   └── products
│   │       ├── base.html
│   │       ├── baskets.html
│   │       ├── index.html
│   │       └── products.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── requirements.txt
├── static
│   └── vendor
│       ├── bootstrap
│       │   ├── css
│       │   │   ├── bootstrap-grid.css
│       │   │   ├── bootstrap-grid.css.map
│       │   │   ├── bootstrap-grid.min.css
│       │   │   ├── bootstrap-grid.min.css.map
│       │   │   ├── bootstrap-reboot.css
│       │   │   ├── bootstrap-reboot.css.map
│       │   │   ├── bootstrap-reboot.min.css
│       │   │   ├── bootstrap-reboot.min.css.map
│       │   │   ├── bootstrap.css
│       │   │   ├── bootstrap.css.map
│       │   │   ├── bootstrap.min.css
│       │   │   └── bootstrap.min.css.map
│       │   └── js
│       │       ├── bootstrap.bundle.js
│       │       ├── bootstrap.bundle.js.map
│       │       ├── bootstrap.bundle.min.js
│       │       ├── bootstrap.bundle.min.js.map
│       │       ├── bootstrap.js
│       │       ├── bootstrap.js.map
│       │       ├── bootstrap.min.js
│       │       └── bootstrap.min.js.map
│       ├── css
│       │   ├── auth.css
│       │   ├── index.css
│       │   ├── orders.css
│       │   ├── products.css
│       │   └── profile.css
│       ├── fontawesome
│       │   └── fontawesome-icons.js
│       ├── img
│       │   ├── products
│       │   │   ├── Adidas-hoodie.png
│       │   │   ├── Black-Dr-Martens-shoes.png
│       │   │   ├── Black-Nike-Heritage-backpack.png
│       │   │   ├── Blue-jacket-The-North-Face.png
│       │   │   ├── Brown-sports-oversized-top-ASOS-DESIGN.png
│       │   │   └── Dark-blue-wide-leg-ASOs-DESIGN-trousers.png
│       │   ├── slides
│       │   │   ├── slide-1.jpg
│       │   │   ├── slide-2.jpg
│       │   │   └── slide-3.jpg
│       │   ├── users
│       │   │   └── default_avatar.jpg
│       │   └── wallpaper.jpg
│       ├── jquery
│       │   ├── jquery.js
│       │   ├── jquery.min.js
│       │   ├── jquery.min.map
│       │   ├── jquery.slim.js
│       │   ├── jquery.slim.min.js
│       │   └── jquery.slim.min.map
│       └── js
│           ├── auth-admin.js
│           └── datatable.js
├── store
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-39.pyc
│   │   ├── celery.cpython-39.pyc
│   │   ├── settings.cpython-39.pyc
│   │   ├── urls.cpython-39.pyc
│   │   └── wsgi.cpython-39.pyc
│   ├── asgi.py
│   ├── celery.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── users
    ├── __init__.py
    ├── __pycache__
    │   ├── __init__.cpython-39.pyc
    │   ├── admin.cpython-39.pyc
    │   ├── apps.cpython-39.pyc
    │   ├── forms.cpython-39.pyc
    │   ├── models.cpython-39.pyc
    │   ├── tasks.cpython-39.pyc
    │   ├── urls.cpython-39.pyc
    │   └── views.cpython-39.pyc
    ├── admin.py
    ├── apps.py
    ├── forms.py
    ├── migrations
    │   ├── 0001_initial.py
    │   ├── 0002_auto_20240930_1418.py
    │   ├── __init__.py
    │   └── __pycache__
    │       ├── 0001_initial.cpython-39.pyc
    │       ├── 0002_auto_20240930_1418.cpython-39.pyc
    │       └── __init__.cpython-39.pyc
    ├── models.py
    ├── tasks.py
    ├── templates
    │   └── users
    │       ├── base.html
    │       ├── email_verification.html
    │       ├── login.html
    │       ├── profile.html
    │       └── register.html
    ├── tests.py
    ├── urls.py
    └── views.py
```

4. Save the file, commit the changes, and push it to your GitHub repository.
