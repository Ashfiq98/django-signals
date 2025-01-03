# Django Signals
## Project Overview

The task is to log user activity in a Django application by using Django signals. Specifically, you need to create a mechanism to automatically record a log entry every time a model instance is saved (either created or updated).

## Key Features

 - Django Signals 
 - Logging User Activity

## Prerequisites
- Python 3.9+ (for local development)
- Git


## Project Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Ashfiq98/django-signals.git
```
### 2. Environment Configuration

1. Ensure Docker and Docker Compose are installed on your system
2. Make virtual environment
   ```bash
   python -m venv ENV ##if pyhon gives you error you can use python3
   ```
   For Linux/MacOS:
   ```bash
   source ENV/bin/activate
   ```
   For Windows:
   ```bash
   ENV\Scripts\activate
   ```
3. 
```bash
cd myproject
code . ## for opening inside vs code
```
4. 
```bash
python manage.py makemigrations
python manage.py migrate
```
5. For creating superuser:
```bash
  python manage.py createsuperuser
  ##whatever you want
  #username : admin
  #email : admin@admin.com
  #password : password
```
6. Run the application :
```bash
python manage.py runserver
```
- Web Application: `http://localhost:8000`
- Admin Interface: `http://localhost:8000/admin`
  - Use the superuser credentials created in step 3
- When we create a new instance of the tracked model (MyModel), a log     
  entry is automatically added to the LogEntry model, indicating the instance was created. 
  When we update an existing instance of the tracked model, a log entry is added indicating the instance was updated. 
