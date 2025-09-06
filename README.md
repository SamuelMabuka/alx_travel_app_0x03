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
1. Clone the repository:
   ```bash
   git clone git@github.com:SamuelMabuka/alx_travel_app_0x03.git
   cd alx_travel_app_0x03
2. python3 -m venv alx_env-> source alx_env/bin/activate
3. Install Dependencies-> pip install -r requirements.txt
4. Database migrations-> python manage.py migrate
5. Start server-> python manage.py runserver
6. Start Celery Worker-> celery -A alx_travel_app worker -l info
