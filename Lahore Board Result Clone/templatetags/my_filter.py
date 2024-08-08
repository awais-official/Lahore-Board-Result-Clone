# myapp/templatetags/my_filters.py
from django import template
import inflect

register = template.Library()

@register.filter
def number_to_words(value):
    p = inflect.engine()
    return p.number_to_words(value)