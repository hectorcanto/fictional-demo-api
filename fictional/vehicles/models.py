from django.db import models

from fictional.domain.fields import VINumberField


class Model(models.Model):
    id = models.AutoField(primary_key=True)
    model_name = models.TextField()
    model_parts = models.ManyToManyField("VehiclePart", related_name="related_models")
    # If it needs to extend Intermediate table, use through and define it

    def __repr__(self):
        return f"<{self.__class__.__qualname__}: {self.model_name}>"


class VehiclePart(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()


class Vehicle(models.Model):

    chassis_number = models.PositiveBigIntegerField(primary_key=True)
    model = models.ForeignKey(Model, on_delete=models.SET_NULL, null=True)


    def __repr__(self):
        return f"<{self.__class__.__qualname__} {self.model.model_name}: {self.chassis_number}>"
