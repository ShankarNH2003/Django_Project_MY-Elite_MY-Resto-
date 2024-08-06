from django import template

register = template.Library()

@register.filter
def float(value):
    try:
        return float(value)
    except (ValueError, TypeError):
        return value
