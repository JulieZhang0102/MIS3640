"""
Question 1:
Given 3 integers, a b c, return their sum. However, if two numbers are the same, only return the other number. If three numbers are the same, return 0.
"""


def sum_uniques(a, b, c):
    """
    Given 3 integers, a b c, return their sum. However, if two numbers are the same, only return the other number. If three numbers are the same, return 0.
    """
    if a == b == c:
        return 0
    elif a == b:
        return c
    elif b == c:
        return a
    elif a == c:
        return b
    else:
        return a + b + c


# When you've completed your function, uncomment the
# following lines and run this file to test!

print(sum_uniques(2019, 10, 1))
# expect: 2030
print(sum_uniques(10, 1, 10))
# expect: 1
print(sum_uniques(10, 10, 10))
# expect: 0


"""
-----------------------------------------------------------------------
Question 2:
If the number, n, is divisible by 4, return True. Return False if n is divisible by 100 (for example, 1900); the only exception is when n is divisible by 400(for example, 2000), return True.
"""


def is_special(n):
    """
    If the number, n, is divisible by 4 (for example, 2020), return True. Return False if n is divisible by 100 (for example, 300); 
    the only exception is when n is divisible by 400(for example, 2400), return True.
    """
    if n % 400 == 0:
        return True
    elif n % 100 == 0:
        return False
    elif n % 4 == 0:
        return True
    else:
        return False



# When you've completed your function, uncomment the
# following lines and run this file to test!


print(is_special(2020))
# expect: True
print(is_special(300))
# expect: False
print(is_special(2019))
# expect: False
print(is_special(2000))
# expect: True


"""
-----------------------------------------------------------------------
Question 3:
Write a function with loops that computes the average of all cubes of all the odd numbers between 1 and n (inclusive).
"""


def calculate_avg(n):
    """
    Given integer n, return the average of all cubes of all the odd numbers between 1 and n (inclusive).
    """
    result = 0
    s = 0
    for i in range(1, n+1, 2):
        result = result + i**3
        s = s + 1
    return result/s



# When you've completed your function, uncomment the
# following lines and run this file to test!

print(calculate_avg(1))
# expect: 1
print(calculate_avg(10))
# expect: 245


"""
-----------------------------------------------------------------------
Question 4:
Write a function with loops that prints the following pattern.
If n is 5, expected output is:
5
4 4
3 3 3
2 2 2 2
1 1 1 1 1
"""

def print_numbers(n):
    # x = 1
    # while n > 0:
    #     print((str(n)+' ')*x)
    #     x = x + 1
    #     n = n - 1

    for i in range(n):
        print((str(n-i)+' ')*(i+1))
    


# When you've completed your function, uncomment the
# following lines and run this file to test!

# print_numbers(5)
## expect:
## 5
## 4 4
## 3 3 3
## 2 2 2 2
## 1 1 1 1 1

print_numbers(9)
# expect:
# 9
# 8 8
# 7 7 7
# 6 6 6 6
# 5 5 5 5 5
# 4 4 4 4 4 4
# 3 3 3 3 3 3 3
# 2 2 2 2 2 2 2 2
# 1 1 1 1 1 1 1 1 1