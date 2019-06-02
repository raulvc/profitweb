from django.core.management.base import BaseCommand

from profitweb.core.models import Client, Product


class Command(BaseCommand):
    help = "Seed's database"

    def handle(self, *args, **options):
        self.stdout.write('seeding database...')
        run_seed()
        self.stdout.write('done.')


def seed_clients():
    clients = ['Darth Vader', 'Obi-Wan Kenobi', 'Luke Skywalker', 'Imperador Palpatine', 'Han Solo']
    for c in clients:
        client = Client(name=c)
        client.save()


def seed_products():
    products = [
        {"name": "Millenium Falcon", "unit_price": 550000, "multiplier": None},
        {"name": "X-Wing", "unit_price": 60000, "multiplier": 2},
        {"name": "Super Star Destroyer", "unit_price": 4570000, "multiplier": None},
        {"name": "TIE Fighter", "unit_price": 75000, "multiplier": 2},
        {"name": "Lightsaber", "unit_price": 6000, "multiplier": 5},
        {"name": "DLT-19 Heavy Blaster Rifle", "unit_price": 5800, "multiplier": None},
        {"name": "DL-44 Heavy Blaster Pistol", "unit_price": 1500, "multiplier": 10}
    ]
    for p in products:
        product = Product(name=p["name"], unit_price=p["unit_price"], multiplier=p["multiplier"])
        product.save()


def run_seed():
    """ Seed's database"""
    seed_clients()
    seed_products()
