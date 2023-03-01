# World-Dataset-Library
WDL is a web-based platform built with Django and React to share datasets online. It allows users to upload, search, and download datasets from a 
variety of domains.

## Installation

To run the World Dataset Library application locally, you need to have the following software installed on your system:

- Python (version 3.6 or higher)
- Node.js (version 12 or higher)

You can follow these steps to install and run the application:

1. Clone this repository to your local machine.
2. Install the required Node.js packages by running the command `npm install` in the `frontend` directory.
3. Create a new database by running the command `python manage.py migrate`.
4. Create a superuser account by running the command `python manage.py createsuperuser` and follow the prompts to enter your desired username and password.
5. Start the development server by running the command `python manage.py runserver`.
6. Open your web browser and navigate to `http://localhost:8000/` to access the application.
