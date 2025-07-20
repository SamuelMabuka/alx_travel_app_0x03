from django.core.management.base import BaseCommand
from listings.models import Listing


class Command(BaseCommand):
    help = 'Seed the database with sample listings'

    def handle(self, *args, **kwargs):
        listings = [
            {
                "title": "Cozy Cottage",
                "description": "A small cozy cottage in the countryside.",
                "location": "Oxford",
                "price_per_night": 75.00,
                "is_available": True
            },
            {
                "title": "Modern Apartment",
                "description": "A modern flat in central London.",
                "location": "London",
                "price_per_night": 150.00,
                "is_available": True
            },
            {
                "title": "Lake House",
                "description": "A serene house by the lake.",
                "location": "Manchester",
                "price_per_night": 120.00,
                "is_available": True
            },
        ]

        for listing in listings:
            Listing.objects.create(**listing)

        self.stdout.write(self.style.SUCCESS("✅ Database seeded successfully!"))