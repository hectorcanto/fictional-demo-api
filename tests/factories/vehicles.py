import factory
from factory import fuzzy, SubFactory, RelatedFactory

from factory.django import DjangoModelFactory
from fictional.vehicles.models import VehiclePart, Model, Vehicle

PART_NAMES = ("bumper", "radiator", "door", )


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
        print(extracted)
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for part in extracted:
                self.model_parts.add(part)


MIN_VIN = 10_000_000_000_000_000
MAX_VIN = 99_999_999_999_999_999


class VehicleFactory(DjangoModelFactory):

    class Meta:
        model = Vehicle

    chassis_number = fuzzy.FuzzyInteger(MIN_VIN, MAX_VIN)
    model = SubFactory(ModelFactory)

