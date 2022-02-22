from django.core.management.base import BaseCommand
from rooms.models import Amenity


class Command(BaseCommand):

    help = "This command creates amenities"

    """ def add_arguments(self, parser):
        parser.add_argument(
            "--times",
            help="How many times do you want me to tell you that I love you?",
        )
        """

    def handle(self, *args, **options):
        amenities = [
            "Heating",
            "Washer",
            "Wifi",
            "Indoor fireplace",
            "Iron",
            "Laptop friendly workspace",
            "Toast machine",
            "Crib",
            "Shampoo",
            "Rinse",
            "Conditioner",
            "Body wash",
            "Body lotion",
            "Bath towel",
            "Air conditioning",
            "Dryer",
            "Breakfast",
            "Hangers",
            "Hair dryer",
            "Smoke detector",
        ]
        for a in amenities:
            Amenity.objects.create(name=a)
            self.stdout.write(self.style.SUCCESS("Amenities created!"))
