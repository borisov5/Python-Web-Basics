from django.db import models


class Profile(models.Model):
    USERNAME_MAX_LEN = 10
    USERNAME_MIN_LEN = 2

    PASSWORD_MAX_LEN = 30

    FIRST_NAME_MAX_LEN = 30

    LAST_NAME_MAX_LEN = 30

    username = models.CharField(
        max_length=USERNAME_MAX_LEN,
    )

    email = models.EmailField()

    age = models.IntegerField()

    password = models.CharField(
        max_length=PASSWORD_MAX_LEN,
    )

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN,
        null=True,
        blank=True,
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LEN,
        null=True,
        blank=True,
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class Car(models.Model):
    TYPE_MAX_LEN = 10

    MODEL_MAX_LEN = 20

    type = models.CharField(
        max_length=TYPE_MAX_LEN,
    )

    model = models.CharField(
        max_length=MODEL_MAX_LEN,
    )

    year = models.IntegerField(

    )

    image_url = models.URLField()

    price = models.FloatField()
