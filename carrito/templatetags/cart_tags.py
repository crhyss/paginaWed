from django import template

register = template.Library()

@register.filter()
def multiplicar(value, arg):
    return float(value) * arg

@register.filter()
def formato_monetario(value, arg):
    return f"{arg}{value}"

