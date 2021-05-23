from django.db import models


class Vehicle(models.Model):
    chassis_number = models.IntegerField(primary_key=True)
    model_id = models.ForeignKey()


class Model(models.Model):
    model_id = models.UUIDField(primary_key=True)
    model_name = models.TextField()
    model_parts = models.ManyToManyRel("model_part")


# Intermediate table Many2Many
# class PartsOfModel(models.Model):
#    model_id = models.ForeignKey()
#     part_id_ = models.ForeignKey()

class VehiclePart(models.Model):
    id = models.UUIDField(primary_key=True)
    part_name = models.TextField()
    related_models = models.ManyToManyRel("model_part")

