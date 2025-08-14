# PostgreSQL Database Setup Guide

## Step 1: Create Database in pgAdmin4

1. **Open pgAdmin4**
2. **Connect to your PostgreSQL server** (usually localhost)
3. **Right-click on "Databases"** 
4. **Select "Create" > "Database..."**
5. **Enter Database Name:** `coding_encouragement`
6. **Click "Save"**

## Step 2: Configure Django Settings

1. **Copy the environment template:**
   ```bash
   copy .env.example .env
   ```

2. **Edit `.env` file with your PostgreSQL credentials:**
   ```
   DB_NAME=coding_encouragement
   DB_USER=postgres
   DB_PASSWORD=your_actual_password
   DB_HOST=localhost
   DB_PORT=5432
   ```

## Step 3: Run Database Migrations

```bash
# Test database connection
C:/Users/sherg/Desktop/vs-code-projects/coding-encouragement/.venv/Scripts/python.exe manage.py check

# Run migrations to create tables
C:/Users/sherg/Desktop/vs-code-projects/coding-encouragement/.venv/Scripts/python.exe manage.py migrate

# Load sample quotes
C:/Users/sherg/Desktop/vs-code-projects/coding-encouragement/.venv/Scripts/python.exe manage.py load_sample_quotes

# Create admin user
C:/Users/sherg/Desktop/vs-code-projects/coding-encouragement/.venv/Scripts/python.exe manage.py createsuperuser
```

## Step 4: Verify Setup

1. **Start the development server:**
   ```bash
   C:/Users/sherg/Desktop/vs-code-projects/coding-encouragement/.venv/Scripts/python.exe manage.py runserver
   ```

2. **Check pgAdmin4:**
   - Navigate to your `coding_encouragement` database
   - You should see tables like: `auth_user`, `coding_encouragement_quote`, etc.

## Troubleshooting

### Connection Error?
- Verify PostgreSQL is running
- Check username/password in `.env`
- Ensure database `coding_encouragement` exists

### Permission Error?
- Make sure your PostgreSQL user has CREATE privileges
- Try using the `postgres` superuser initially

### Port Error?
- Default PostgreSQL port is 5432
- Check your PostgreSQL installation settings
