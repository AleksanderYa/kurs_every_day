from abc import ABC


class SomeDaseHelper(ABC):
    def __init__(self):
        # self.some_dict = {}
        self.some_list = []
        self.refer_dict = {
            'Monobank': 'currency:mono_view',
            'Privatbank': 'currency:privat_view',
        }

    def some_work(self, request):
        pass

class SomeHelper(SomeDaseHelper):
    def some_work(self, request):

        # print(request.user.groups.all()[0], 'req')
        if request:
            for i in request.user.groups.all():
                i = str(i)
                # print(list(self.refer_dict.keys()))
                # print(i)
                # print(self.refer_dict.get(str(i)))
                if i in list(self.refer_dict.keys()):
                    some_dict = {}
                    print(i, 'ref')
                    print(list(self.refer_dict.keys()))
                    some_dict['name'] = i
                    some_dict['link'] = self.refer_dict.get(i)
                    self.some_list.append(some_dict)
        print(self.some_list)
        return self.some_list




# class FindLinkHelper:
#     @staticmethod
#     def find_link(name):
#         if name








