# Coding Encouragement

A Django web application designed to provide encouragement and motivation for coding learners and developers. 🚀

## 📱 Wireframes

Wireframes play a crucial role in shaping a website’s architecture, ensuring a cohesive and well-optimised experience for users. The wireframes for this project have been created using [Balsamiq](https://balsamiq.com/) and Chrome extension [Wireframe-Prage](https://chromewebstore.google.com/detail/wireframe-page/bhaaofjcbafngjjneehlganleamobkke) to define the core feature layout, ensuring a user-friendly experience that prioritises clarity and ease of navigation. These mid-fidelity wireframes serve as a foundational guide for structuring the site's design and responsiveness across different screen sizes.

Each template is developed using user-centred principles: prioritising simplicity, searchability, and visually-guided interactions, ensuring an intuitive experience that fulfils business and customer needs.

| Template Name       | Description / Purpose          | Expand Feature to View Image                               |
|---------------------|-------------------------------|------------------------------------------------------------|
| main.html           | Display inspirational quotes related to coding | <details><summary>view wireframe</summary><img src="https://raw.githubusercontent.com/Ozzymara/docpe/refs/heads/main/assets/cemain.webp" alt="wireframe" style="width:100%;"></details> |
| signup.html          | User registration page          | <details><summary>view wireframe</summary><img src="https://raw.githubusercontent.com/Ozzymara/docpe/refs/heads/main/assets/cesignup.webp" alt="wireframe" style="width:100%;"></details> |
| login.html           | User authentication page        | <details><summary>view wireframe</summary><img src="https://raw.githubusercontent.com/Ozzymara/docpe/refs/heads/main/assets/celogin.webp" alt="wireframe" style="width:100%;"></details> |
| myquotes.html         | Display's users uploaded quotes | <details><summary>view wireframe</summary><img src="https://raw.githubusercontent.com/Ozzymara/docpe/refs/heads/main/assets/cemyquotes.webp" alt="wireframe" style="width:100%;"></details> |
| submit.html            | Allows user to submit quotes | <details><summary>view wireframe</summary><img src="https://raw.githubusercontent.com/Ozzymara/docpe/refs/heads/main/assets/cesubmit.webp" alt="wireframe" style="width:100%;"></details> |
| report.html       | Allows users to report quotes  | <details><summary>view wireframe</summary><img src="https://raw.githubusercontent.com/Ozzymara/docpe/refs/heads/main/assets/cereport.webp" alt="wireframe" style="width:100%;"></details> |
| myvotes.html         | Allows users to rate a quote   | <details><summary>view wireframe</summary><img src="https://raw.githubusercontent.com/Ozzymara/docpe/refs/heads/main/assets/cemyvotes.webp" alt="wireframe" style="width:100%;"></details> |

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
### User Stories

- As a new coder, I want to see a new inspirational quote so that I can feel encouraged while learning to code
- As a new coder, I want to the quotes to be snappy and uplifting so that they're easy to remember
- As a contributor, I want to submit my own inspirational quotesso that I can share encouragement with others who are learning to code
- As a contributor, I want to see my quote appear randomly in the rotation so thatI feel part of the community
- As a visitor, I want to load the site quickly and on any device so that I can get inspiration wherever I am

  
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
