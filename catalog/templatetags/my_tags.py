from django import template
from django.templatetags.static import static

register = template.Library()

@register.simple_tag
def mediapath(image_path):
    return static(image_path)