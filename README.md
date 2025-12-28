# Django Signals Assignment

This project demonstrates the core behaviors of Django Signals (Synchronous execution, Threading, and Transaction management) through three practical examples.

## 📂 File Structure Overview

* **`views.py`**: The "Caller". It triggers the database saves, measures execution time, checks thread ID and verifies if transactions were rolled back.
* **`signals.py`**: The "Receiver". It contains the logic to pause execution (sleep), print thread IDs, and intentionally raise exceptions to test reliability.
* **`models.py`**: Contains the simple `AnswerModel` class used to create records and trigger the signals.
* **`apps.py`**: The configuration file that ensures `signals.py` is loaded and registered when the server starts.

---

## 🚀 How to Execute

### 1. Setup the Environment
Clone the repository and navigate into the project folder. If you haven't installed Django yet, run:
```bash
pip install django
```

### Prepare the Database
Run the migrations to create the necessary table for AnswerModel:
```bash
python manage.py makemigrations
python manage.py migrate
```
### Run the Server
Start the local development server:
```bash
python manage.py runserver
```
### Run the Tests
Open your web browser and navigate to this URL:
```bash
http://127.0.0.1:8000/
```
Browser Output: You will see the timing results for Question 1 and Thread ID for Question 2 and the Transaction rollback verification for Question 3.

Terminal Output: Check your command prompt/terminal to see the Thread ID comparison for Question 2.
