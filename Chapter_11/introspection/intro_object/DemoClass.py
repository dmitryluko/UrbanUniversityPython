# Simple class for inspection

class DemoClass:
    def __init__(self, x: int, y: int, label: str = 'Demo'):
        self.data = 1
        self.__coord = (x, y)
        self.__label = label

    @property
    def label(self):
        return self.__label

    @label.setter
    def label(self, value):
        self.__label = value

    def __str__(self):
        return f'{self.__label}: {self.__coord}'
