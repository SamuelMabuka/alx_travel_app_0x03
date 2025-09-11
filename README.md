# ALX Travel App 0x03

This is a Django-based travel booking application built as part of the ALX Backend Python specialization.  
It demonstrates advanced Django project setup with:

- **Django REST Framework** for building APIs  
- **Swagger (drf-yasg)** for API documentation  
- **Celery + RabbitMQ** for background task management (e.g., sending booking confirmation emails)  
- **MySQL** as the database  
- **CORS support** for frontend integration  
- **Payment integration** using Chapa API (Ethiopia)

## Features
- User registration and management  
- Travel **listings** (create, view, update, delete)  
- **Bookings** linked to users and listings  
- Automated **email notifications** via Celery  
- **Payment initiation & verification** through Chapa  

## Setup Instructions

### Local Development
1. Clone the repository:
   ```bash
   git clone git@github.com:SamuelMabuka/alx_travel_app_0x03.git
   cd alx_travel_app_0x03
   ```

2. Create and activate virtual environment:
   ```bash
   python3 -m venv alx_env
   source alx_env/bin/activate
   ```

3. Install Dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your database and API credentials
   ```

5. Database migrations:
   ```bash
   python manage.py migrate
   ```

6. Collect static files:
   ```bash
   python manage.py collectstatic
   ```

7. Start development server:
   ```bash
   python manage.py runserver
   ```

8. Start Celery Worker (in separate terminal):
   ```bash
   celery -A alx_travel_app worker --loglevel=info
   ```

## Deployment

This application is deployment-ready with configurations for multiple platforms:

### Heroku Deployment
1. Install Heroku CLI
2. Create Heroku app:
   ```bash
   heroku create your-app-name
   ```
3. Set environment variables:
   ```bash
   heroku config:set DEBUG=False
   heroku config:set SECRET_KEY=your-production-secret-key
   heroku config:set ALLOWED_HOSTS=your-app-name.herokuapp.com
   ```
4. Add database addon:
   ```bash
   heroku addons:create jawsdb:kitefin  # MySQL
   # or
   heroku addons:create heroku-postgresql:mini  # PostgreSQL
   ```
5. Deploy:
   ```bash
   git push heroku main
   ```

### Render.com Deployment
1. Connect your GitHub repository to Render
2. Use the provided `render.yaml` configuration
3. The deployment will automatically:
   - Install dependencies
   - Collect static files
   - Run database migrations
   - Start the web server

### Railway Deployment
1. Connect your GitHub repository to Railway
2. Set environment variables in Railway dashboard:
   ```
   DEBUG=False
   SECRET_KEY=your-production-secret-key
   ALLOWED_HOSTS=*
   DATABASE_URL=your-database-url
   ```

### Environment Variables for Production
```bash
# Required
SECRET_KEY=your-long-random-secret-key
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com

# Database (use DATABASE_URL for easier deployment)
DATABASE_URL=mysql://user:password@host:3306/dbname
# OR individual settings:
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=your_db_host
DB_PORT=3306

# Celery (Redis recommended for production)
CELERY_BROKER_URL=redis://user:password@host:6379/0
CELERY_RESULT_BACKEND=redis://user:password@host:6379/0

# Optional
CHAPA_SECRET_KEY=your-chapa-api-key
```

## API Documentation
Once deployed, visit `/swagger/` or `/redoc/` for interactive API documentation.

## Production Checklist
- [x] Security settings configured for HTTPS
- [x] Static files handling with WhiteNoise
- [x] Database URL configuration
- [x] Environment-based settings
- [x] Gunicorn WSGI server ready
- [x] Celery worker configuration
- [x] Deployment files (Procfile, render.yaml)

## Support
For deployment issues, check the Django deployment checklist:
```bash
python manage.py check --deploy
```
