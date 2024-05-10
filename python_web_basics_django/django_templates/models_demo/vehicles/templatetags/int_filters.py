import math

from django import template

register = template.Library()


@register.filter
def self_multiply(value):
    """
    Multiplies a number by itself once

    * 10 -> 100
    """

    try:
        number = int(value)
        return number * number
    except ValueError as e:
        print(e)
        return 'Invalid'


@register.filter
def sqrt(value):
    """
    Finds the square root of a number

    * 100 -> 10
    """

    try:
        number = int(value)

        if number < 0:
            raise ValueError('Cannot find the sqrt of a negative number!')

        return f'{math.sqrt(number):.2f}'
    except ValueError as e:
        print(e)
        return 'Invalid'


@register.filter
def increase_by(value, other):
    try:
        return value + other
    except TypeError:
        return int(value) + other
