import math
def quadratic(a, b, c):
    y = b**2 - 4*a*c
    if y > 0:
        x1 = (((-b) + math.sqrt(y))/(2*a))
        x2 = (((-b) - math.sqrt(y))/(2*a))
        print('The answers are', x1, 'and', x2)
    elif y == 0:
        x = (-b) / 2*a
        print('The answer is', x)
    else:
        print('There is no answer for this problem.')

quadratic(2,4,1)
quadratic(1,2,1)
quadratic(10,3,11)