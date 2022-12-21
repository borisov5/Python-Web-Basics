from django.core.validators import MinLengthValidator
from django.db import models

from my_plant.core.validators import validate_capital_leter


class Profile(models.Model):
    username = models.CharField(
        max_length=10,
        validators=[
            MinLengthValidator(2),
            validate_capital_leter,
        ]
    )

    first_name = models.CharField(
        max_length=20,

    )

    last_name = models.CharField(
        max_length=20,

    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )

