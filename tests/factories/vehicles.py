import factory
from factory import fuzzy, SubFactory
from factory.django import DjangoModelFactory

from fictional.vehicles.models import VehiclePart, Model, Vehicle

PART_NAMES = ("bumper", "radiator", "door", "decklid", "spoiler", "roof",
              "trunk", "window", "door seal", "hinge", "lock", "tank", "windshield",
              "seat", "handle", "latch", "grille", "bonnet", "spring", "glass",
              "regulator", "carburator", "antenna", "radio", "alternator", "battery",
              "gauge", "deposit")
# TODO more parts, with variations and grouping (electronics, chassis, motor ...) and their associated manufacturing line


class PartsFactory(DjangoModelFactory):

    class Meta:
        model = VehiclePart

    name = fuzzy.FuzzyChoice(PART_NAMES)


MODEL_NAMES = ("Edinburgh", "Glasgow", "Dundee", "Aberdeen", "Inverness", "Perth", "Stirling")


class ModelFactory(DjangoModelFactory):

    class Meta:
        model = Model

    model_name = fuzzy.FuzzyChoice(MODEL_NAMES)

    @factory.post_generation
    def model_parts(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of parts were passed in, use them
            for part in extracted:
                self.model_parts.add(part)


MIN_VIN = 10_000_000_000_000_000
MAX_VIN = 99_999_999_999_999_999


class VehicleFactory(DjangoModelFactory):

    class Meta:
        model = Vehicle

    chassis_number = fuzzy.FuzzyInteger(MIN_VIN, MAX_VIN)
    model = SubFactory(ModelFactory)
