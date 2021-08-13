class Lol:
    @staticmethod
    def if_else(i):
        print(i)

    def wrippers(func):
        def inner(*args, **kwargs):
            print('Start s')
            func(*args, **kwargs)
            print('End s')
        return inner

    def wripper(func):
        def inner(*args, **kwargs):
            print('Start')
            f = func(*args, **kwargs)
            for i in f:
                Lol.if_else(i)
            print('End')
        return inner

    @staticmethod
    @wrippers
    @wripper
    def a():
        a = [
            1, 2, 3, 4, 5, 6, 7, 8, 9
        ]
        return a

Lol.a()