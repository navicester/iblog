from django import template
from urllib import quote_plus

register = template.Library()

@register.filter
def urlify(value):
    if isinstance(value,unicode):
        return quote_plus(value.encode('utf8')) # data from database is unicode, quote_plus can only accept ascii
    return quote_plus(value)