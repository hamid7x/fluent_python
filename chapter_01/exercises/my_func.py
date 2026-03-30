class MyFunc:
    def __call__(self, *args, **kwds):
        print('function get called')
        bob, jhon = args
        country = kwds['country']
        return f"names: {bob}, {jhon}, country: {country}"


func = MyFunc()
print(func('bob', 'jhon', country='Morroco'))
