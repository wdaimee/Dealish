from django import template

register = template.Library()

@register.filter
def space_plus(value):
    return value.replace(" ", "+")