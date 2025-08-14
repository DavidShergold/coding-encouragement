# Coding Encouragement

A Django web application designed to provide encouragement and motivation for coding learners and developers. 🚀

## Getting Started

### Prerequisites
- Python 3.11+
- Virtual environment (automatically created)

### Installation

1. The virtual environment is already set up in `.venv/`
2. Django is already installed
3. Database migrations have been applied

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
