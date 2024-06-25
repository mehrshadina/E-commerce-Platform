# E-commerce Platform

This is an E-commerce platform built with Django. It allows administrators to manage products and customers to place orders. The platform includes user authentication, order management, and wallet functionality.

## Features

### Admin
- Login with username and password.
- Add new products with unique codes.
- Update product inventory and prices.
- View order history.
- Change password.

### Customer
- Register with username and password.
- Login with username and password.
- View wallet balance.
- Place orders with available products.
- Use discount codes for orders.
- View order history.
- Change password.

## Installation

### Prerequisites
- Python 3.8 or higher
- Django 4.0 or higher
- pip (Python package installer)

### Setup
1. Clone the repository:
    ```sh
    git clone https://github.com/mehrshadinaa/E-commerce-Platform.git
    cd your-repo-name
    ```

2. Create a virtual environment:
    ```sh
    python -m venv venv
    ```

3. Activate the virtual environment:
    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On macOS and Linux:
        ```sh
        source venv/bin/activate
        ```

4. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

5. Apply the database migrations:
    ```sh
    python manage.py migrate
    ```

6. Create a superuser account:
    ```sh
    python manage.py createsuperuser
    ```

7. Collect static files:
    ```sh
    python manage.py collectstatic
    ```

8. Run the development server:
    ```sh
    python manage.py runserver
    ```

9. Open your browser and go to `http://127.0.0.1:8000/` to see the application.

## Project Structure

your-repo-name/
│
├── main/
│ ├── migrations/
│ ├── static/
│ │ └── main/
│ │ ├── style.css
│ ├── templates/
│ │ └── main/
│ │ ├── base.html
│ │ ├── home.html
│ │ ├── login.html
│ │ ├── register.html
│ │ ├── customer_panel.html
│ │ ├── admin_panel.html
│ │ └── place_order.html
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── tests.py
│ ├── urls.py
│ └── views.py
├── your_repo_name/
│ ├── init.py
│ ├── asgi.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md

less
Copy code

## Usage

### Admin Panel
- Navigate to `http://127.0.0.1:8000/admin/`
- Log in with your superuser credentials.
- Add, update, or delete products.
- View and manage customer orders.

### Customer Panel
- Register a new account at `http://127.0.0.1:8000/register/`.
- Log in at `http://127.0.0.1:8000/login/`.
- View wallet balance and place orders.
- Use discount codes when placing orders.
- View order history and manage account.

## Contributing

1. Fork the repository.
2. Create a new branch:
    ```sh
    git checkout -b feature-name
    ```
3. Make your changes and commit them:
    ```sh
    git commit -m 'Add some feature'
    ```
4. Push to the branch:
    ```sh
    git push origin feature-name
    ```
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

Your Name - [mehrshadinaa@gmail.com](mailto:mehrshdinaa@gmail.com)

Project Link: [https://github.com/mehrshadina/E-commerce-Platform](https://github.com/meheshadina/E-commerce-Platform
