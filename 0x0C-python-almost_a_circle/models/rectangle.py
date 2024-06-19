#!/usr/bin/python3

""" this module call another module and access it class """

from models.base import Base

class Rectangle(Base):

    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width
    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x
    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
             raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        return self.__height * self.__width

    """de display(self):
        if self.__x > 1:
            for i in range(self.__x):
                print()
        for i in range(self.__height):
            print(" " * self.__y ,"#" * self.__width)
    """
    def display(self):
        """Displays the rectangle using # """
        for y in range(self.y):
            print("")
        for row in range(self.__height):
            for x in range(self.x):
                print(" ", end="")
            for column in range(self.__width):
                print("#", end="")
            print()
    def __str__(self):
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"
    def update(self, *args, **kwargs):
        if args:
            if len(args) == 1:
                self.id = args[0]
            elif len(args) == 2:
                self.width = args[1]
            elif len(args) == 3:
                self.height = args[2]
            elif len(args) == 4:
                self.x = args[3]
            elif len(args) == 5:
                self.y = args[4]
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        dict_ = {"id":self.id,"width":self.width,\
                 "height":self.height, "x":self.x, "y":self.y}

        return dict_
