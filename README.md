# Django_Products

This is a **Django-based project** for managing products. It allows users to **add, view, and display products** with categories, images, and details. This project was created as part of a class activity.

---

## **Features**

- Add new products with:
  - Name
  - Price
  - Category
  - Description (optional)
  - Image (optional)
- View all products in a list
- View product details (optional)
- Products and categories registered in **Django Admin**
- Media handling with `ImageField` and Pillow library

---

## **Project Structure**

Django_Products/
│
├── manage.py
├── requirements.txt
├── myproject/
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── products/
│ ├── models.py
│ ├── views.py
│ ├── admin.py
│ ├── urls.py
│ └── templates/products/
│ ├── add_product.html
│ ├── product_list.html
│ └── product_detail.html
└── env/

yaml
Copy code

---

## **Installation & Setup**

1. **Clone the repository** (or download ZIP)

```bash
git clone https://github.com/masud520/Django_Products.git
cd Django_Products
Create and activate virtual environment

bash
Copy code
python3 -m venv env
source env/bin/activate
Install dependencies

bash
Copy code
pip install -r requirements.txt
Run migrations

bash
Copy code
python manage.py makemigrations products
python manage.py migrate
Create superuser (optional if already provided)

bash
Copy code
python manage.py createsuperuser
**Admin Login (for testing)
Username: user

Password: user123**

Login at: http://127.0.0.1:8000/admin/

Running the Server
bash
Copy code
python manage.py runserver
Access pages in your browser:

mathematica
Copy code
Add Product:   http://127.0.0.1:8000/products/add/
Product List:  http://127.0.0.1:8000/products/
Admin Panel:   http://127.0.0.1:8000/admin/
Terminal showing server running

Add Product page

Product List page

Admin panel showing Product & Category models

Technologies Used
Python 3.x

Django 4.x

SQLite (default database)

HTML/CSS

Pillow (for image handling)

License
This project is for educational purposes.
