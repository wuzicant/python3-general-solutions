from Others import other_print


class Vehicle:
    def __init__(self, make='mb', name='911'):
        self.__make = make
        self.__name = name
        self.__year = 1995

    # def __init__(self, make='mb', name='N'):
    #     self.__make = make
    #     self.__year = 1995

    def get_make(self):
        return self.__make

    def get_name(self):
        return self.__name

    def set_make(self, make):
        self.__make = make

    def get_year(self):
        return self.__year
    
    def horn(self):
        print('b---------')


if __name__ == '__main__':
    v = Vehicle(None,'918')
    v.horn()

