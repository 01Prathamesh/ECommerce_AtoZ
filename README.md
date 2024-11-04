# ECommerce AtoZ

Welcome to the ECommerce AtoZ project, a Django-based web application for managing an online store. This project features product listings, product details, a checkout process, and mock payment handling.

## Features

- **User-friendly Homepage**: Navigate to products and checkout easily.
- **Product Listing**: View products list and information overview.
-  **Product Detail**: View detail informaition of the product.
- **Checkout Process**: Submit orders and handle payments.
- **Mock Payment System**: Simulate payment success and failure.

## Technologies Used

- **Django**: The web framework used for backend development.
- **Django REST Framework**: For creating API endpoints.
- **HTML/CSS**: For frontend design.
- **SQLite/PostgreSQL**: For database management (depending on configuration).
- **Pillow**: For image handling in products.

## Requirements

To run this project, you'll need to have Python and pip installed. You can install the required packages using:

    ```bash
    pip install -r requirements.txt


## Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/ECommerce_AtoZ.git

2. **Navigate to the project directory**:
    ```bash
    cd ECommerce_AtoZ

3. **Set up a virtual environment(optional but recommended)**:
    ```bash
    source myenv/bin/activate
    
Activate the virtual environment:

On macOS/Linux:
    
        ```bash
        source myenv/bin/activate

On Windows:

        ```bash
        myenv\Scripts\activate

4. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt

5. **Run database migrations**:
    ```bash
    python manage.py makemigrations
    python manage.py migrate

6. **Create a superuser to access the admin panel**:
    ```bash
    python manage.py createsuperuser

7. **Start the development server**:
    ```bash
    python manage.py runserver

8. **Open your browser and navigate to http://127.0.0.1:8000/ to view the application.**

## API Endpoints
- **GET /api/products/**: List all products.
- **GET /api/products/<id>/**: Retrieve details of a specific product.
- **POST /api/products/**: Create a new product (requires authentication).
- **GET /api/categories/**: List all categories (if implemented).

## Contribution
    Contributions are welcome! If you'd like to contribute to this project, please fork the repository and create a pull request.

## License
    This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
    Thanks to the Django community for their support and resources.
