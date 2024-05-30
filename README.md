# Publishing Portal

A Django application to manage publishers, authors, and books.

## Features

- List, create, update, and delete books, authors, and publishers
- View details of books, authors, and publishers
- Filter books by author and publisher
- Pagination for book and author lists
- Search functionality for books, authors, and publishers
- User authentication for creating, updating, and deleting items
- Responsive design with Bootstrap
- File uploads for author headshots and book covers
- Prevent deletion of authors assigned to books

## Setup Instructions

### Prerequisites

- Python 3.x
- Django 3.x
- Virtualenv (optional but recommended)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/jbhonest/publishing-portal.git
    cd publishing-portal
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Apply the migrations:

    ```bash
    python manage.py migrate
    ```

5. Create a superuser:

    ```bash
    python manage.py createsuperuser
    ```

6. Run the development server:

    ```bash
    python manage.py runserver
    ```

7. Open your browser and go to `http://127.0.0.1:8000/`

### Admin Panel
1. Navigate to http://127.0.0.1:8000/admin
2. Log in with the superuser credentials you created
3. Add authors, books, and publishers from the admin panel

### Adding Fake Data
You can also generate fake data using the custom management command:

    
    python manage.py generate_fake_data
    
### Navigating the App
* Publishers: View the list of publishers and their details
* Authors: View the list of authors and their details
* Books: View the list of books and their details

### Search
Use the search bar in the navbar to find books, authors, and publishers by name.

### Authentication
* Users must be logged in to create, update, or delete authors, books, and publishers.
* Log in and log out links are available in the navbar.

---
Developed by Jamal Badiee (jbhonest@yahoo.com)