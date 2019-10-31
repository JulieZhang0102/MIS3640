import math

class Point:
    '''
    a point with x, y attributes
    '''

class Circle:
    '''
    Circle with attributes center and radius
    '''
    center = Point()

circle = Circle()
circle.center.x = 150
circle.center.y = 100
circle.radius = 75

class Rectangle:
    """Represents a rectangle. 

    attributes: width, height, corner.
    """


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

def point_in_circle(Circle, Point):
    circle_center = Circle.center
    if distance_between_points(circle_center, Point) <= Circle.radius:
        return True
    else:
        return False

def rect_in_circle(Circle, Rectangle):
  
  aCorner=Rectangle.corner
  bCorner=Rectangle.corner
  cCorner=Rectangle.corner
  dCorner=Rectangle.corner
  
  bCorner.x=aCorner.x+Rectangle.width
  dCorner.y=bCorner.y-Rectangle.height
  cCorner.x=dCorner.x-Rectangle.width
  
  #Checking All Corners of Rec
  if point_in_circle(Circle,aCorner):
      if point_in_circle(Circle,bCorner):
          if point_in_circle(Circle,cCorner):
              if point_in_circle(Circle,dCorner):
                  return True

def rect_circle_overlap(Circle,Rectangle):
  
  a2Corner=Rectangle.corner
  b2Corner=Rectangle.corner
  c2Corner=Rectangle.corner
  d2Corner=Rectangle.corner
  
  b2Corner.x=a2Corner.x+Rectangle.width
  d2Corner.y=b2Corner.y-Rectangle.height
  c2Corner.x=d2Corner.x-Rectangle.width
  
  if point_in_circle(Circle,a2Corner):
    return True
  elif point_in_circle(Circle,b2Corner):
    return True
  elif point_in_circle(Circle,c2Corner):
    return True
  elif point_in_circle(Circle,d2Corner):
    return True

