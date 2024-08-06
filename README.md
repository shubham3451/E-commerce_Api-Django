# Django E-Commerce Project

## Overview

This is a Django-based e-commerce application designed to manage products, product lines, images, categories, brands, attributes, and attribute values. The project uses Django REST Framework to provide a robust API for interacting with these entities.

## Features

- **Categories**: Manage product categories.
- **Brands**: Manage product brands.
- **Products**: Manage individual products.
- **Product Lines**: Handle different variants or lines of a product.
- **Product Images**: Manage images associated with product lines.
- **Attributes**: Define various attributes for products.
- **Attribute Values**: Manage possible values for each attribute.

## Requirements

-asgiref==3.8.1
-Django==5.0.7
-django-js-asset==2.2.0
-djangorestframework==3.15.2
-pillow==10.4.0
-sqlparse==0.5.1

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/your-project.git
   cd your-project
   ```

2. **Create and Activate a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**

   ```bash
   python manage.py migrate
   ```

5. **Create a Superuser**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the Development Server**

   ```bash
   python manage.py runserver
   ```


## API Endpoints

The project uses Django REST Framework's `ModelViewSet` to provide CRUD operations for each model. Below is a summary of the available endpoints:


   - "categories": "http://127.0.0.1:8000/api/api/categories/",
   - "brands": "http://127.0.0.1:8000/api/api/brands/",
   - "products": "http://127.0.0.1:8000/api/api/products/",
   - "productsline": "http://127.0.0.1:8000/api/api/productsline/",
   - "productimages": "http://127.0.0.1:8000/api/api/productimages/",
   - "attributes": "http://127.0.0.1:8000/api/api/attributes/",
   - "attributevalues": "http://127.0.0.1:8000/api/api/attributevalues/"



## Testing

To run tests for the project:

```bash
python manage.py test
```
