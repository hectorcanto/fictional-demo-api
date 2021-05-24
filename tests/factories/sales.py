from datetime import datetime, timezone

import factory
from factory import SubFactory
from factory.django import DjangoModelFactory

from fictional.sales.models import Sale, Office
from .common import FAKER
from .vehicles import VehicleFactory
from fictional.infra.helpers import dt_now

def make_region():
    return FAKER.location_on_land()[3]


def make_phone():
    return FAKER.phone_number().split("x")[0]


class OfficeFactory(DjangoModelFactory):

    class Meta:
        model = Office

    address = factory.LazyFunction(FAKER.address)
    phone = factory.LazyFunction(make_phone)
    region = factory.LazyFunction(make_region)


class SalesFactory(DjangoModelFactory):

    class Meta:
        model = Sale

    created_at = factory.LazyFunction(dt_now)
    model = factory.LazyAttribute(lambda o: o.vehicle.model)
    vehicle = SubFactory(VehicleFactory)
    office = SubFactory(OfficeFactory)
