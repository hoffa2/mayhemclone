import math
class Vector2D(object):
    """ Implements a two dimensional vector. """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Vector(%s, %s)" % (self.x, self.y)

    def __add__(self, b):
        """ Addition. Returns a new vector. """
        return Vector2D(self.x + b.x, self.y + b.y)

    def __sub__(self, b):
        """ Subtraction. Returns a new vector. """
        return Vector2D(self.x - b.x, self.y - b.y)

    def __getitem__(self, key):
        if key == 0:
            return self.x
        elif key == 1:
            return self.y
        else:
            raise IndexError("Invalid subscript "+str(key)+" to Vec2d")

    def __setitem__(self, key, value):
        if key == 0:
            self.x = value
        elif key == 1:
            self.y = value
        else:
            raise IndexError("Invalid subscript "+str(key)+" to Vec2d")


    def __abs__(self):
        return Vector2D(abs(self.x), abs(self.y))

    def __div__(self, b):

        try:
            b = float(b)
            return Vector2D(self.x / b, self.y / b)
        except ValueError:
            print "Oops! Right value must be a float"
            raise

    def __mul__(self, b):
        """ Multiplication by a scalar

        Note that the scalar must be to the right.

        """
        try:
            b = float(b)
            return Vector2D(self.x * b, self.y * b)
        except ValueError:
            print "Oops! Right value must be a float"
            raise

    def __eq__(self, b):
        if (self.x == b) & (self.y == b):
            return True
        else:
            return False

    def magnitude(self):
        """ Returns the magnitude of the vector. """
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def normalized(self):
        """ Returns a new vector with the same direction but magnitude 1. """
        try:
            m = self.magnitude()
            return Vector2D(self.x / m, self.y / m) * 2
        except ZeroDivisionError:
            print "Oops! Cannot normalize a zero-vector"
            raise

    def copy(self):
        """ Returns a copy of the vector. """
        return Vector2D(self.x, self.y)
