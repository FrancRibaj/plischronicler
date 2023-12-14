👋 HELLO THERE

**To make FRONTEND changes please address these files:**

./plis_web/home/static/home.css 


./plis_web/home/static/home.html 


**Setting up Django and Virtual Environment:**

### 1. Install Python
# Windows
https://www.python.org/downloads/](https://www.python.org/downloads/

# Linux

```bash
sudo apt update
```

```
sudo apt install python3
```

### 2. Install Virtualenv 

```bash
pip install virtualenv
```

### 3. Create a Virtual Environment

Navigate to the directory where you want to create your Django project and create a virtual environment:

- On Windows
```bash
python -m venv venv
```

- On macOS/Linux
```bash
python3 -m venv venv
```

Virtual environment named "venv" in your project directory is created.

### 4. Activate the Virtual Environment

Activate the virtual environment:

- On Windows:

```bash
venv\Scripts\activate
```

- On macOS/Linux:

```bash
source venv/bin/activate
```

### 5. Install Django

While the virtual environment is active, install Django using `pip`:

```bash
pip install django
```

### 6. Navigate to the Project Directory

Change into the project directory:

```bash
cd ./plis_web
```

### 7. Make Migrations

```bash
python manage.py makemigrations
```

### 8. Run Migrations

```bash
python manage.py migrate
```

### 9. Run the Development Server

Start the Django development server:

```bash
python manage.py runserver
```

Visit http://localhost:8000 in your web browser. You should see the default Django welcome Home page. :)


