import datetime
from django import template
from django.template.defaultfilters import stringfilter
from abc import ABCMeta

from log_in.helpers import SomeHelper
from currency.models import Currency

register = template.Library()

@register.simple_tag
def buttons_view(request):
    some_helper = SomeHelper()
    some = some_helper.some_work(request)
    return {
        'buttons_list': some,
    }

@register.simple_tag
def delete_messages_from_base(request, *args):
    try:
        if args[0]:
            obj = Currency.objects.filter(id=28)
            obj.delete()
            print(args, 'Delete')
            return {
                'message': 'Message is delete'
            }
    except Exception as e:
        print(e)

@register.simple_tag
def edit_(self):
    pass


@register.simple_tag
def say_hi(request):
    return {'Hi':'Hi from current_time'}
