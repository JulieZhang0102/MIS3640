import math


class Point:
    """Represents a point in 2-D space.

    attributes: x, y
    """

# my_point = Point()
# print(my_point)
# print(type(my_point))
# # Print doc string
# print(my_point.__doc__)
# my_point.x = 3.0
# my_point.y = 4
# print(my_point.x, my_point.y)

def print_point(p):
    """Print a Point object in human-readable format."""
    print(f'({p.x}, {p.y}).')

# print_point(my_point)

# # Check if attribute is defined/existed or not
# print(hasattr(my_point, 'x'))
# print(hasattr(my_point, 'z'))

# # Return attributes (including hidden ones)
# print(dir(my_point))

def distance_between_points(p1, p2):
    """Computes the distance between two Point objects.

    p1: Point
    p2: Point

    returns: float
    """
    distance_x = p1.x - p2.x
    distance_y = p1.y - p2.y
    distance = math.sqrt(distance_x**2 + distance_y**2)
    return distance

# julie_point = Point()
# # julie_point.x = 6
# # julie_point.y = 8
# julie_point.x, julie_point.y = 6, 8
# print(distance_between_points(my_point, julie_point))


class Rectangle:
    """Represents a rectangle. 

    attributes: width, height, corner.
    """

# box = Rectangle()
# box.width = 100.0
# box.height = 200.0
# box.corner = Point()
# box.corner.x = 0
# box.corner.y = 0

def find_center(rect):
    """Returns a Point at the center of a Rectangle.

    rect: Rectangle

    returns: new Point
    """
    p = Point()
    p.x = rect.corner.x + rect.width / 2.0
    p.y = rect.corner.y + rect.height / 2.0
    return p

# center_of_box = find_center(box)
# print_point(center_of_box)

def grow_rectangle(rect, dwidth, dheight):
    """Modifies the Rectangle by adding to its width and height.

    rect: Rectangle object.
    dwidth: change in width (can be negative).
    dheight: change in height (can be negative).
    """
    rect.width += dwidth
    rect.height += dheight

def print_rectangle(rect):
    '''
    print the width, height, and lower-left corner of the given Rectangle object
    '''
    print(f'width: {rect.width}, height:{rect.height}')
    print('the lower-left corner:')
    print_point(rect.corner)

# print_rectangle(box)
# grow_rectangle(box, 100, 100)
# print('After growing...')
# print_rectangle(box)

# string and tuple are immutable, list and dictionary are mutable, class is mutable

def main():
    # pass
    my_point = Point()
    print(Point.__doc__)
    my_point.x = 3
    my_point.y = 4
    print('My point', end=' ')
    print_point(my_point)

    print('Is my_point an instance of Point?', isinstance(my_point, Point))
    print('Is my_point an instance of Rectangle?',
          isinstance(my_point, Rectangle))
    print('Does my_point have an attribute x?', hasattr(my_point, 'x'))
    print('Does my_point have an attribute z?', hasattr(my_point, 'z'))

    box = Rectangle()
    box.width = 100.0
    box.height = 200.0
    box.corner = Point()
    box.corner.x = 0.0
    box.corner.y = 0.0

    print('Does box have an attribute x?', hasattr(box, 'x'))

    print('Does box have an attribute corner?', hasattr(box, 'corner'))

    print('Rectangle has these:', dir(box))

    center = find_center(box)
    print('center', end=' ')
    print_point(center)

    # print(box.width)
    # print(box.height)
    print_rectangle(box)
    print('grow')
    grow_rectangle(box, 50, 100)
    # print(box.width)
    # print(box.height)
    print_rectangle(box)


if __name__ == '__main__':
    main()
    # p1 = Point()
    # p1.x = 3
    # p1.y = 4

    # import copy
    # p2 = copy.copy(p1)

    # print_point(p1)
    # print_point(p2)

    # print(p1 is p2) #False
    # print(p1.x is p2.x) #True
    # print(p1 == p2) # False
