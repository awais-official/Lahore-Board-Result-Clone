# myapp/templatetags/my_filters.py
from django import template

register = template.Library()
# my_filters.py
import inflect

@register.filter
def number_to_words(value):
    p = inflect.engine()
    if value:  # Check if value is not empty
        return p.number_to_words(int(value))
    else:
        return value  # Return an error message if value is empty
    