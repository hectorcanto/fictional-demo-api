from django.db import models
from typing import NewType, Union
import re


ReadableVIN = NewType('ReadableVIN', str)


# TODO we could have used or created a VIN library
class VINumberField(models.IntegerField):
    pass
    # TODO validation

    # NOTE since we are a manufacturer we could consider saving the manufacturer prefix
    # but we could have problems if we buy another manufacture

    # Alphanumeric form 4Y1SL65848Z411439
    # Numeric form 48123658489411439
    # More readable 4Y1-SL658-4-8-Z-41-1439


# https://cars.usnews.com/cars-trucks/best-cars-blog/2017/01/what-is-a-vin-number
# inspired in https://rgxdb.com/r/61PVCR9B
VIN_REGEX = re.compile(r"(?P<wmi>[\d]{3})(?P<vds>[\d]{5})(?P<check>\d)"
                       r"(?P<vis>(?P<year>\d)(?P<plant>\d)(?P<seq1>[\d]{2})(?P<seq2>[\d]{4}))")
"""
REGEX for a numeric VIN without hyphens
"""


def to_friendly_vin(numeric_vin: Union[int, str]) -> ReadableVIN:
    result = re.search(VIN_REGEX, str(numeric_vin)).groupdict()
    if not result:
        raise TypeError("VIN is not valid")
    blk = result.groupdict()
    return ReadableVIN(f'{blk["wmi"]}-{blk["vds"]}-{blk["year"]}-{blk["plant"]}-{blk["seq1"]}-{blk["seq2"]}')


