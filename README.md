# The APP

A Django RESTful API project for managing travel-related listings, bookings, and user reviews.

This project is part of the ALX Backend specialization and demonstrates core backend engineering skills such as model design, serialization, and database seeding using Django management commands.

## Features
- **Listings**: Create and manage travel property listings
- **Bookings**: Users can book listings for specific dates
- **Reviews**: Leave reviews on listings after booking
- **Database Seeder**: Custom Django command to populate sample data

### Listing
- `title`: Title of the listing
- `description`: Description text
- `location`: City or region
- `price_per_night`: Decimal field
- `available`: Boolean flag

### Booking
- ForeignKey to `Listing`
- `guest_name`
- `check_in`, `check_out` dates

### Review
- ForeignKey to `Listing`
- `reviewer_name`
- `rating` (1-5)
- `comment`

## Serializers

- `ListingSerializer`: Exposes listing data via the API
- `BookingSerializer`: Handles booking data serialization/deserialization


## Seeder Command

The `seed` management command populates the database with sample listings and related data:

## Requirements
- Python 3.8+
- Django 4.x
- MySQL or SQLite (default for dev)

Developed by: 
Samuel Mabuka
Backend Developer
GitHub: @SamuelMabuka

