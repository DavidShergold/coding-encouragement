# Coding Encouragement

A Django web application designed to provide encouragement and motivation for coding learners and developers. 🚀

## Getting Started

### Prerequisites
- Python 3.11+
- PostgreSQL database server
- pgAdmin4 (for database management)
- Virtual environment (automatically created)

### Database Setup

1. **Create PostgreSQL Database:**
   - Open pgAdmin4
   - Create a new database named `coding_encouragement`
   - Note your PostgreSQL username and password

2. **Configure Database Connection:**
   - Copy `.env.example` to `.env`
   - Update the database credentials in `.env`:
     ```
     DB_NAME=coding_encouragement
     DB_USER=your_postgres_username
     DB_PASSWORD=your_postgres_password
     DB_HOST=localhost
     DB_PORT=5432
     ```

### Installation

1. The virtual environment is already set up in `.venv/`
2. Django and PostgreSQL dependencies are installed
3. **Configure your database settings in `.env`**
4. Run database migrations (see below)

### Database Migration

After setting up your PostgreSQL database and updating `.env`:

```bash
# Run migrations to create tables
C:/Users/sherg/Desktop/vs-code-projects/coding-encouragement/.venv/Scripts/python.exe manage.py migrate

# Load sample quotes (optional)
C:/Users/sherg/Desktop/vs-code-projects/coding-encouragement/.venv/Scripts/python.exe manage.py load_sample_quotes

# Create superuser for admin access
C:/Users/sherg/Desktop/vs-code-projects/coding-encouragement/.venv/Scripts/python.exe manage.py createsuperuser
```

### Running the Application

The Django development server is configured to run via VS Code tasks:

1. Open the Command Palette (Ctrl+Shift+P)
2. Run "Tasks: Run Task"
3. Select "Django Development Server"

Or use the terminal:
```bash
C:/Users/sherg/Desktop/vs-code-projects/coding-encouragement/.venv/Scripts/python.exe manage.py runserver
```

The application will be available at: http://127.0.0.1:8000/

### Project Structure

```
myproject/          # Main Django project
├── __init__.py
├── settings.py     # Project settings
├── urls.py         # Main URL configuration
└── wsgi.py         # WSGI configuration

coding_encouragement/  # Coding Encouragement Django app
├── migrations/     # Database migrations
├── __init__.py
├── admin.py        # Admin configuration
├── apps.py         # App configuration
├── models.py       # Database models
├── tests.py        # Tests
├── urls.py         # App URL patterns
└── views.py        # View functions

manage.py           # Django management script
```

### Next Steps

- Add models to `coding_encouragement/models.py` for your data structure
- Create templates in `coding_encouragement/templates/` for encouragement messages
- Add static files in `coding_encouragement/static/` for styling
- Build features like daily coding tips, progress tracking, motivational quotes
- Create additional views and URL patterns as needed
- Set up proper database configuration for production

### Development

- The project uses Django 5.2.5
- SQLite database (default Django setting)
- Development server runs on port 8000
