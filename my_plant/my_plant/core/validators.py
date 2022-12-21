from django.core import exceptions


def validate_only_letters(value):
    for ch in value:
        if not ch.isalpha():
            raise exceptions.ValidationError("Plant name should contain only letters!")


def validate_capital_leter(value):
    pass
