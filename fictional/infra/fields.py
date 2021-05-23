from django.db import models


class PhoneField(models.CharField):
    pass


class RegionField(models.CharField):
    pass


class AddressField(models.CharField):
    pass


__all__ = ["PhoneField", "RegionField", "AddressField"]