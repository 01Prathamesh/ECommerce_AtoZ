# ECommerce AtoZ

Welcome to the ECommerce AtoZ project, a Django-based web application for managing an online store. This project features product listings, product details, a checkout process, and mock payment handling.

## Features

- **User-friendly Homepage**: A clean and intuitive interface that allows users to easily navigate the store, find products, and access the checkout process. The homepage highlights featured products to attract customer interest.

- **Product Listing**: Users can view a comprehensive list of products with essential details, including product names, prices, and thumbnail images. The listing is designed for easy browsing, with options to filter and sort products based on various criteria.

- **Product Detail Page**: Each product has its own detail page that provides an in-depth view of the product, including high-resolution images, detailed descriptions, specifications, and customer reviews. This helps customers make informed purchasing decisions.

- **Checkout Process**: A streamlined checkout process that guides users through submitting their orders with minimal friction. Users can review their cart, enter shipping information, and select payment options in a clear, step-by-step manner.

- **Mock Payment System**: A simulated payment gateway that allows users to experience the payment process without actual transactions. It includes scenarios for both payment success and failure, making it ideal for testing and demonstration purposes.

- **User Authentication**: Secure user registration and login functionality, enabling users to create accounts, manage their profiles, and track their orders.

## Technologies Used

- **Django**: A high-level Python web framework that simplifies the development of secure and maintainable web applications. It follows the "batteries-included" philosophy, providing built-in features for authentication, routing, and ORM.

- **Django REST Framework**: A powerful toolkit for building Web APIs in Django. It facilitates the creation of RESTful services, allowing for easy integration with front-end frameworks and mobile applications.

- **HTML/CSS**: The foundational technologies for building web pages. HTML structures the content, while CSS styles the visual presentation, ensuring a responsive and visually appealing design across devices.

- **SQLite/PostgreSQL**: Two options for database management. SQLite is lightweight and suitable for development and testing, while PostgreSQL offers advanced features and scalability for production environments.

- **Pillow**: A Python Imaging Library that enables image processing capabilities within the application. It allows for tasks like image uploading, resizing, and format conversion, enhancing product presentation.

- **JavaScript**: Used for client-side scripting to create a dynamic and interactive user experience. JavaScript enhances functionality like product filtering and cart management without requiring full page reloads.

- **Bootstrap **: A popular front-end framework for building responsive and mobile-first websites. It provides a collection of pre-designed components and a grid system to streamline development.

## Requirements

To run this project, you'll need to have Python and pip installed. You can install the required packages using:
    ```bash
    
        pip install -r requirements.txt

## Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/01Prathamesh/ECommerce_AtoZ.git

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

This project is licensed under the [MIT License](LICENSE). See the LICENSE file for details.


## Acknowledgments
    Thanks to the Django community for their support and resources.
