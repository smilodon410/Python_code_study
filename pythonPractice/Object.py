x = list()
print(type(x))
print(dir(x))


class Hong:
    x = 0

    def __init__(self):
        print('constructor')

    def party(self):
        self.x = self.x + 1
        print('So far', self.x)

    def __del__(self):
        print('destructor')

an = Hong()
an.party()
an.party()
an = 42
print('an contains', an)