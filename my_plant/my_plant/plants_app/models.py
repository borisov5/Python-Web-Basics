from django.core.validators import MinLengthValidator
from django.db import models

from my_plant.core.validators import validate_only_letters


class Plant(models.Model):
    TYPES = (
        ("Outdoor Plants", "Outdoor Plants"),
        ("Indoor Plants", "Indoor Plants")
    )

    plant_type = models.CharField(
        max_length=14,
        choices=TYPES,
    )

    name = models.CharField(
        max_length=20,
        validators=[
            MinLengthValidator(2),
            validate_only_letters,
        ]
    )


    image_url = models.URLField()

    description = models.TextField()

    price = models.FloatField()
