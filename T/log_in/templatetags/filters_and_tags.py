import datetime
from django import template
from django.template.defaultfilters import stringfilter
from abc import ABCMeta

from log_in.helpers import SomeHelper


register = template.Library()

@register.simple_tag
def buttons_view(request):
    some_helper = SomeHelper()
    some = some_helper.some_work(request)
    return {
        'buttons_list': some,
    }

@register.simple_tag
def say_hi(request):
    return {'Hi':'Hi from current_time'}
