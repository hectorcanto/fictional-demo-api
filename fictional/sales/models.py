from django.db import models
from fictional.infra.models import TrackedAbstract, UUIDAbstract
from fictional.infra.fields import *


class Sale(TrackedAbstract):

    # Tracked: created_at <- Relevant to the domain
    # Tracked: updated_at
    created_at = models.DateTimeField(db_index=True)
    id = models.AutoField(primary_key=True)
    model_id = models.ForeignKey("vehicles.Model")
    vehicle_id = models.ForeignKey("vehicles.Vehicle")
    office_id = models.ForeignKey("sales.Office")


class Office(TrackedAbstract, UUIDAbstract):

    # Tracked: created_at
    # Tracked: updated_at
    # UUID: id

    address = AddressField()
    phone = PhoneField()
    region = RegionField()

    # TODO office members and roles