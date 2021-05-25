import factory

from factory.django import DjangoModelFactory
from fictional.users.models import User

from .common import FAKER, generate_dict_factory


class UserFactory(DjangoModelFactory):

    class Meta:
        model = User
    #    #django_get_or_create = ("id", )

    # ID? or let it be autofield
    username = factory.LazyAttribute(lambda o: f"{o.first_name.lower()}_{o.last_name.lower()}")
    first_name = factory.LazyFunction(FAKER.first_name())
    last_name = factory.LazyFunction(FAKER.last_name())


UserDictFactory = generate_dict_factory(UserFactory)
