# Heroku Deployment Guide

## Prerequisites
1. Install Heroku CLI: https://devcenter.heroku.com/articles/heroku-cli
2. Create a Heroku account: https://signup.heroku.com/

## Deployment Steps

### 1. Login to Heroku
```bash
heroku login
```

### 2. Create Heroku App
```bash
heroku create your-app-name-coding-encouragement
```
(Replace `your-app-name` with your preferred app name)

### 3. Set Environment Variables
```bash
heroku config:set SECRET_KEY="your-secret-key-here"
heroku config:set DEBUG=False
```

### 4. Deploy to Heroku
```bash
git push heroku main
```

### 5. Run Database Migrations
```bash
heroku run python manage.py migrate
heroku run python manage.py load_sample_quotes
heroku run python manage.py createsuperuser
```

### 6. Open Your App
```bash
heroku open
```

## Your app will be available at:
`https://your-app-name-coding-encouragement.herokuapp.com`

## Useful Heroku Commands

### View logs
```bash
heroku logs --tail
```

### Run Django management commands
```bash
heroku run python manage.py shell
heroku run python manage.py collectstatic
```

### Scale dynos
```bash
heroku ps:scale web=1
```

## Environment Variables Set on Heroku
- `SECRET_KEY` - Django secret key
- `DEBUG` - Set to False for production
- Database URL is automatically provided by Heroku PostgreSQL addon

## Notes
- Heroku automatically provides a PostgreSQL database
- Static files are served by WhiteNoise
- The app uses Gunicorn as the WSGI server
- SSL is automatically provided by Heroku
