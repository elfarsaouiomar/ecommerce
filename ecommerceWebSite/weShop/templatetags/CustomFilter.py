"""
    create simple tags and filters
"""

from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    """
    this fucntion take two argument as must be
    int and returm the multiple
    :param value:
    :param arg:
    :return:
    """
    if value and arg:
        return value * arg
    return 0
