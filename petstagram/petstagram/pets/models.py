from django.db import models
from django.template.defaultfilters import slugify

from petstagram.core.model_mixins import StrFromFieldsMixin


class Pet(StrFromFieldsMixin, models.Model):
    str_fields = ('id', 'name')
    NAME_MAX_LEN = 30

    name = models.CharField(
        max_length=NAME_MAX_LEN,
        null=False,
        blank=False,
    )

    personal_photo = models.URLField(
        null=False,
        blank=False,
    )

    slug = models.SlugField(
        unique=True,
        null=False,
        blank=True,
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(f'{self.id}-{self.name}')

        return super().save(*args, **kwargs)

    # def __str__(self):
    #     return f'Id= {self.id}; Name= {self.name}'
