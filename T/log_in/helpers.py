from abc import ABC
from django import template



class SomeDaseHelper(ABC):
    def __init__(self):
        self.some_list = []
        self.refer_dict = {
            'Monobank': 'currency:mono_view',
            'Privatbank': 'currency:privat_view',
        }

    def some_work(self, request):
        pass

class SomeHelper(SomeDaseHelper):
    def some_work(self, request):
        if request:
            for i in request.user.groups.all():
                i = str(i)
                if i in list(self.refer_dict.keys()):
                    some_dict = {}
                    some_dict['name'] = i
                    some_dict['link'] = self.refer_dict.get(i)
                    self.some_list.append(some_dict)
        return self.some_list


class Tags:
    register = template.Library()

    @register.simple_tag
    def base_tag(self, request):
        return '2'









