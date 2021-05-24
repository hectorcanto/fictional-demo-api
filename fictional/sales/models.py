from django.db import models
from fictional.infra.models import TrackedAbstract
from fictional.infra.fields import *
from fictional.infra.helpers import dt_now


class Sale(TrackedAbstract):

    # Tracked: updated_at
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(db_index=True, default=dt_now)
    model = models.ForeignKey("vehicles.Model", on_delete=models.DO_NOTHING)
    vehicle = models.ForeignKey("vehicles.Vehicle", on_delete=models.SET_NULL, null=True)
    office = models.ForeignKey("sales.Office", on_delete=models.DO_NOTHING)


class Office(TrackedAbstract):

    # Tracked: created_at
    # Tracked: updated_at

    id = models.AutoField(primary_key=True)
    address = AddressField(max_length=100)
    phone = PhoneField(max_length=20)
    region = RegionField(max_length=20)  # will work with country codes
