class Point:
    '''
    Represents a point in 2-D space.

    attributes: x, y
    '''
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        '''return True if x of both are same'''
        return self.x == other.x

    def __contains__(self, number):
        return number == self.x or number == self.y

my_point = Point(5, 4)
print(my_point)

point2 = Point(5, 5)

print(my_point + point2)
print(point2 - my_point)

print(my_point == point2)

print(4 in my_point)
print(4 in point2)
