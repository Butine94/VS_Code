class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def get_width(self):
        return self._width

    def set_width(self, value):
        if value > 0:
            self._width = value
        else:
            raise ValueError("Width must be a positive number")

    def get_height(self):
        return self._height

    def set_height(self, value):
        if value > 0:
            self._height = value
        else:
            raise ValueError("Height must be a positive number")

    width = property(get_width, set_width)
    height = property(get_height, set_height)

# Creating an instance of Rectangle
rectangle = Rectangle(10, 5)

# Accessing width using the getter method
print(rectangle.width)  # Output: 10

# Accessing height using the getter method
print(rectangle.height)  # Output: 5

# Setting new values using the setter methods
rectangle.width = 20
rectangle.height = 8

print(rectangle.width)  # Output: 20
print(rectangle.height)  # Output: 8

