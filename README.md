# Crypto currency price monitor Backend

The project is a Django-based backend for a cryptocurrency price monitoring application. It includes user registration, the ability for logged-in users to save their favorite currency pairs, and utilizes the Django framework with an SQLite database.

1. Clone the repository:
   
   ```shell
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   
   ```shell
   cd crypto-price-monitor-backend
   ```

3. Install Poetry (if not already installed):
   
   ```shell
   pip install poetry
   ```

4. Create a virtual environment and install dependencies using Poetry:
   
   ```shell
   poetry install
   ```

5. Apply database migrations:
   
   ```shell
   poetry shell
   python manage.py migrate
   ```

6. Start the Django development server:
   
   ```shell
   python manage.py runserver
   ```

   The server should now be running at `http://localhost:8000/`.


