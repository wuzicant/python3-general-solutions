from Vehicle import Vehicle


class Car(Vehicle):

    def __init__(self, power=False, name='duo'):
        Vehicle.__init__(self, 'ss', '918')
        #super(Car, self).__init__()
        self.__power = power
        self.__name = name

    def get_name(self):
        print('child')
        return self.__name

    @staticmethod
    def get_power():
        return 'self.__power'

    def move_forward(self):
        print('forward -----')

    def move_backward(self):
        n = self.__name
        print(f'{n} backward -----')

    def move_left(self):
        print('left -----')

    def move_right(self):
        print('right -----')

if __name__ == '__main__':
    v = Vehicle()
    c = Car(True, 'bmw')
    print(c.get_name())

