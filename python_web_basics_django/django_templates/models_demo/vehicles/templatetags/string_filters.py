from django import template

register = template.Library()


@register.filter(name='capitalize')
def capitalize(value):
    """
    Capitalizes the first letter of a text and lowers the rest:
    
    * HelLO tHEre -> Hello there
    """

    value = str(value)
    return value[0].upper() + value[1:].lower()


@register.filter(name='to_upper_case')
def to_upper_case(value):
    """
    Capitalizes all the letters of a text

    * hello there -> HELLO THERE
    """

    value = str(value)
    return value.upper()


@register.filter  # Not necessary to provide default name
def join_names(owners):
    return ', '.join([f"{owner.first_name} {owner.last_name}" for owner in owners])
