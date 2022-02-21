from django import template
from mainapp.models import Tank

register = template.Library()


@register.inclusion_tag('mainapp/tanks.html', name='tanks')
def get_tanks(lvl=None):
    if lvl:
        return {'tanks': Tank.objects.filter(lvl=lvl)}
    return {'tanks': Tank.objects.all()}