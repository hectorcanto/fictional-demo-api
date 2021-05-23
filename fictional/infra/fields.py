from django.db import models


class PhoneField(models.TextField):
    pass


class RegionField(models.TextField):
    pass


class AddressField(models.TextField):
    pass


__all__ = ["PhoneField", "RegionField", "AddressField"]