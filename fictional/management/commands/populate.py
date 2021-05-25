from datetime import timedelta
from random import randint

from django.core.management.base import BaseCommand
from factory import fuzzy

from fictional.infra.helpers import dt_now
from tests.factories import ModelFactory, SalesFactory, VehicleFactory, PartsFactory

NOW = dt_now()
ONE_YEAR_AGO = timedelta(days=365)


class Command(BaseCommand):
    def __init__(self):
        super(Command, self).__init__()

    def handle(self, *args, **kwargs):
        print("Creating new vehicle models")
        models = []
        for _ in range(5):
            model = ModelFactory.create_batch(
                1, model_parts=[part.id for part in PartsFactory.create_batch(5)]
            )
            models.append(model[0])

        for model in models:
            number = randint(8, 12)
            print(f"Creating {number} Sales for Model {model.id}:{model.model_name})")
            SalesFactory.create_batch(
                number,
                vehicle=VehicleFactory(model=model),
                created_at=fuzzy.FuzzyDateTime(NOW - ONE_YEAR_AGO, NOW),
            )
