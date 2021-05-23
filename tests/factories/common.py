from functools import partial
from typing import Any, Dict

from django.db import models

from factory import Factory
from factory.base import StubObject
from factory.faker import faker


FAKER = faker.Faker()


# https://github.com/FactoryBoy/factory_boy/issues/68#issuecomment-636452903
def generate_dict_factory(the_factory: Factory):
    def convert_dict_from_stub(stub: StubObject) -> Dict[str, Any]:
        stub_dict = stub.__dict__
        for key, value in stub_dict.items():
            if isinstance(value, StubObject):
                stub_dict[key] = convert_dict_from_stub(value)
            elif isinstance(value, models.Model):  # Patch for user_id
                stub_dict[key] = value.pk
        return stub_dict

    def dict_factory(the_factory, **kwargs):
        stub = the_factory.stub(**kwargs)
        stub_dict = convert_dict_from_stub(stub)
        return stub_dict

    return partial(dict_factory, the_factory)
