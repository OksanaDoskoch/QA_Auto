from abc import ABC, abstractmethod


class Figure(ABC):
    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass


class Rectangle(Figure):
    def __init__(self, width: float, height: float):
        self.__width = width
        self.__height = height

    def get_area(self):
        return self.__width * self.__height

    def get_perimeter(self):
        return 2 * (self.__width + self.__height)


class Square(Rectangle):
    def __init__(self, side: float):
        super().__init__(side, side)


class Triangle(Figure):
    def __init__(self, a: float, b: float, c: float):
        self.__a = a
        self.__b = b
        self.__c = c

    def get_area(self):
        s = (self.__a + self.__b + self.__c) / 2
        return (s * (s - self.__a) * (s - self.__b) * (s - self.__c)) ** 0.5

    def get_perimeter(self):
        return self.__a + self.__b + self.__c


rectangle = Rectangle(3, 4)
square = Square(5)
triangle = Triangle(3, 4, 5)

figures = [rectangle, square, triangle]

for fig in figures:
    print(f"{fig.__class__.__name__}")
    print("Area:", round(fig.get_area(), 2))
    print("Perimeter:", round(fig.get_perimeter(), 2))
    print()