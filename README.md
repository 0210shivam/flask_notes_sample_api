# Flask CRUD API Project

This is a Flask project that provides a simple CRUD (Create, Read, Update, Delete) API for managing resources.

## Specifications

- **Authentication and Authorization:**
  This API implements authentication for users, ensuring secure access to resources based on their identity. Users can perform operations on specific notes resources, and the API verifies user credentials to ensure access only to relevant resources.


- **Session Management:**
  The API includes functionality for session management to track user login status. When a user logs in, they receive a session_id. Upon logout, the session_id and session are automatically removed. This ensures secure access control and prevents unauthorized access to resources. 

## Validation

This API enforces certain validation rules to ensure the integrity of the data. Here are some key points to note:

- **Resource Creation (POST Request):**
  - The request body must be a valid JSON object.
  - For registering user, "username", "email", and "password" field is required.
  - For "username" field, it must have at least three characters in it.
  - "username" field must contain only letters, numbers, and underscores".
  - For "email", it must be in a valid email format.
  - For "password" field, it must have at least 6 characters.
  - For notes, "title" field is required.


## Getting Started

### Prerequisites

- Python 3.x
- Flask
- Pymongo 4.6.0
- python-decouple 3.8
- marshmallow 3.20.1

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/0210shivam/flask_notes_sample_api.git
   cd second_flask

2. Optional: Create and Activate a Virtual Environment

    ```bash
    python -m venv venv
   pip install -r requirements.txt   # to get all dependencies
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`

3. Run the flask app
    ```bash
   python run.py

## API Endpoints
### Database testing routes
#### 1. To test database by adding one document

- **Endpoint:** `/add_one`
- **Method:** POST
- **Description:** Adds one document to database.
- **Sample request:** 
    ```bash
    curl -X POST -H "Content-Type: application/json" -d '{"name": "New Resource", "description": "This is a sample resource."}' http://localhost:5000/add_one

#### 2. To test database by adding many documents

- **Endpoint:** `/add_many`
- **Method:** POST
- **Description:** Adds many documents to database.
- **Sample request:** 
    ```bash
    curl -X POST -H "Content-Type: application/json" -d '[{"name": "New Resource", "description": "This is a sample resource."},{"name": "Another Resource", "description": "This is second resource."}}]' http://localhost:5000/add_many

### Authentication related routes
#### 1. To register user

- **Endpoint:** `/auth/register`
- **Method:** POST
- **Description:** Register user and added to database.
- **Sample request:** 
    ```bash
    curl -X POST -H "Content-Type: application/json" -d '{"username": "test_name", "email": "test123@gmail.com", "password": "12345678"}' http://localhost:5000/auth/register

#### 2. To login user

- **Endpoint:** `/auth/login`
- **Method:** POST
- **Description:** Logs in user if exists in database.
- **Sample request:** 
    ```bash
    curl -X POST -H "Content-Type: application/json" -d '{"username": "test_name", "email": "test123@gmail.com", "password": "12345678"}' http://localhost:5000/auth/login

#### 3. To logout user

- **Endpoint:** `/auth/logout`
- **Method:** GET
- **Description:** Logs out user if logged-in.
- **Sample request:** 
    ```bash
    curl -X GET -H "Content-Type: application/json" -d '{"username": "test_name", "email": "test123@gmail.com", "password": "12345678"}' http://localhost:5000/auth/logout

#### 4. To update user details 

- **Endpoint:** `/auth/update_profile`
- **Method:** PATCH
- **Description:** Updates credentials.
- **Sample request:** 
    ```bash
    curl -X PATCH -H "Content-Type: application/json" -d '{"username": "updated_name", "email": "updated123@gmail.com", "password": "12345678"}' http://localhost:5000/auth/update_profile

#### 5. To delete user

- **Endpoint:** `/auth/delete_profile`
- **Method:** DELETE
- **Description:** Deletes user from database.
- **Sample request:** 
    ```bash
    curl -X DELETE -H "Content-Type: application/json" -d '{"username": "test_name", "email": "test123@gmail.com", "password": "12345678"}' http://localhost:5000/auth/delete_profile

### Notes related routes
#### 1. To add note

- **Endpoint:** `/notes/add_note`
- **Method:** POST
- **Description:** Adds note to database.
- **Sample request:** 
    ```bash
    curl -X POST -H "Content-Type: application/json" -d '{"title": "test_title", "desc": "test description"}' http://localhost:5000/notes/add

#### 2. To fetch all notes

- **Endpoint:** `/notes/all_notes`
- **Method:** GET
- **Description:** Fetches all notes from database
- **Sample request:** 
    ```bash
    curl -X GET http://localhost:5000/notes/add

#### 3. To update existing note

- **Endpoint:** `/notes/update_note/{note_id}`
- **Method:** PATCH
- **Description:** Updates note.
- **Sample request:** 
    ```bash
    curl -X PATCH -H "Content-Type: application/json" -d '{"title": "updated_title", "desc": "updated description"}' http://localhost:5000/notes/update/654f0fe579cd5720305ff416

#### 4. To delete note

- **Endpoint:** `/note/delete_note`
- **Method:** DELETE
- **Description:** Deletes note.
- **Sample request:** 
    ```bash
    curl -X DELETE http://localhost:5000/notes/delete/654f0fe579cd5720305ff416

## Contributing
Feel free to contribute to this project. Submit a pull request with your changes or open an issue if you find any bugs.


## Contact

For questions or concerns, feel free to reach out to [shivam.shrivastava1006@gmail.com](mailto:shivam.shrivastava1006@example.com).
