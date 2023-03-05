from django import template
from app_tag.models import Menu

register = template.Library()


@register.inclusion_tag('menu.html')
def draw_menu(type=None):
    if 'main_menu' == type:
        return {'menu': Menu.objects.all()}
