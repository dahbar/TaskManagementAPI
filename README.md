# Task Management API

A simple task management API built with FastAPI.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/task_management_api.git
   cd task_management_api
   ```

2. **Create and activate a virtual environment:**

    On a macOS/Linux:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

    On Windows:
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```

3. **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

1. **Initialize the database:**

    This step will create the necessary tables in your database.
    ```bash
    python3 scripts/database_setup.py
    ```

2. **Run the FastAPI application:**

    Start the development server using Uvicorn:
    ```bash
    uvicorn main:app --reload
    ```

3. **Access the API documentation:**

    Open your browser and go to http://127.0.0.1:8000/docs to see the interactive Swagger UI documentation.





