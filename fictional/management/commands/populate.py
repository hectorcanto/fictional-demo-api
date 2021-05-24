from datetime import timedelta
from random import randint

from django.core.management.base import BaseCommand
from factory import fuzzy

from fictional.infra.helpers import dt_now
from tests.factories import ModelFactory, SalesFactory, VehicleFactory

NOW = dt_now()
ONE_YEAR_AGO = timedelta(days=365)


class Command(BaseCommand):

    def __init__(self):
        super(Command, self).__init__()

    def handle(self, *args, **kwargs):
        print("Creating new vehicle models")
        models = ModelFactory.create_batch(5)
        for model in models:
            number = randint(8, 12)
            print(f"Creating {number} Sales for Model {model.id}:{model.model_parts})")
            SalesFactory.create_batch(number, vehicle=VehicleFactory(model=model), created_at=fuzzy.FuzzyDateTime(NOW - ONE_YEAR_AGO, NOW))