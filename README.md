# Coding Encouragement

A Django web application designed to provide encouragement and motivation for coding learners and developers. 🚀

## 📱 Wireframes

Wireframes play a crucial role in shaping a website’s architecture, ensuring a cohesive and well-optimised experience for users. The wireframes for this project have been created using [Balsamiq](https://balsamiq.com/) and the Chrome extension [Wireframe-Prage](https://chromewebstore.google.com/detail/wireframe-page/bhaaofjcbafngjjneehlganleamobkke) to define the core feature layout, ensuring a user-friendly experience that prioritises clarity and ease of navigation. These mid-fidelity wireframes serve as a foundational guide for structuring the site's design and responsiveness across different screen sizes.

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

## 🧪 Testing and Validation
This section summarises the results of user interface (UI) element functionality testing for the website.

## [✅ HTML Validation](https://validator.w3.org/#validate_by_input) and [Lighthouse](https://developers.google.com/web/tools/lighthouse/)

The website currently has <span style="color:#39FF14">no errors or warnings</span>.

<img src="https://raw.githubusercontent.com/Ozzymara/docpe/refs/heads/main/assets/celighthouse.webp" alt="wireframe" style="width:100%;">

<img src="https://raw.githubusercontent.com/Ozzymara/docpe/refs/heads/main/assets/cevalidation.png" alt="wireframe" style="width:100%;">

When MS Copilot generated code, occasional stray elements like <span style="font-family:monospace;">&lt;/span&gt;</span> and other closing tags appeared due to the way it predicted and completed code snippets. These errors were flagged during HTML validation and were corrected in [VS Code](https://code.visualstudio.com/download).

Additionally, the use of explicit ARIA role attributes (e.g. role="button", role="main") on HTML elements was initially guided by recommendations from the WAVE accessibility tool. However, these roles are inherently implied by the semantic HTML5 elements themselves. The Nu HTML Validator correctly flags them as unnecessary. To ensure leaner, more semantic code and to align with modern best practices, we chose to deselect checking redundant role attributes.

## ✅ Chrome DevTools Lighthouse
• A [Lighthouse](https://developers.google.com/web/tools/lighthouse/) audit was conducted using the tool on Chrome DevTools for each web page.  
• Categories *Accessibility*, *Best Practices*, and *SEO* all have a score of <span style="color:#39FF14">100</span>.
• The *Performance* scores for the various pages ranged between <span style="color:#39FF14">91-100</span>.

## ✅ CSS Validation

<span style="color:#39FF14">No errors found</span>

<img src="https://raw.githubusercontent.com/Ozzymara/docpe/refs/heads/main/assets/cecss.webp" alt="wireframe" style="width:100%;">

This document validates as CSS level 3 + SVG.

## ✅ JS Validation

Because this project uses a modern script, JS Hint was configured to allow 'New JavaScript features (ES6)'. <span style="color:#39FF14">No errors</span> are found in the current version of the site.

## ✅ CI Python Linter
To check code quality and adherence to Python style guidelines, all Python files were checked using the [Code Institute’s Python Linter](https://pep8ci.herokuapp.com/), which uses [PEP8](https://peps.python.org/pep-0008/) (8th Python Enhancement Proposal (PEP) document).

The result "<span style="color:#39FF14">All clear, no errors found</span>" across all files means that there are no stylistic or syntax errors and the code complies with Python linting standards.

<img src="https://raw.githubusercontent.com/Ozzymara/docpe/refs/heads/main/assets/cepython.webp" alt="wireframe" style="width:100%;">

The table below explains the Python linter error/warning codes found, why they are not urgent, and recommended fixes for the future:

| Code | Meaning | Why Not Urgent | Recommended Fix |
| --- | --- | --- | --- |
| E302 | Expected 2 blank lines before function/class | Style issue to improve readability | Add 2 blank lines before function/class |
| E304 | Blank lines found after function decorator | Minor style issue, does not affect code | Remove unnecessary blank lines after decorators |
| E501 | Line too long (exceeds max length, e.g. 79) | Code runs fine, but hard to read | Break long lines into shorter ones |
| E722 | Do not use bare except | Catching all exceptions hides errors | Specify exception type in except clause |
| W293 | Blank line contains whitespace | Whitespace does not cause errors | Remove trailing whitespace |
| W291 | Trailing whitespace | Harmless but messy code | Remove trailing whitespace |

Summary: These are mainly style and best practice warnings intended to improve code readability and maintainability. They do not break the code but addressing them makes the code cleaner and easier to understand. Setting up automated formatting tools can help fix and prevent these in the future.

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
