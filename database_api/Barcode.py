import shelve


class Mycode():
    __id = 0
    __count = 0
    __weight = 0
    __reuse_count = 0
    __name = f'container {0}'

    def __int__(self, barcode, name=None):
        if name is not None:
            self.__name = name
        self.__id = str(barcode)
        self.__count += 1

    def set_weight(self, weight):
        self.__weight = weight

    def get(self, key):
        match key:
            case 'count': return self.__count
            case 'weight': return self.__weight
            case 'name': return self.__name
            case 'reuse_count': return self.__reuse_count
            case _: raise KeyError('no search key')


code = Mycode(name='me')
print(code['barcode'])
