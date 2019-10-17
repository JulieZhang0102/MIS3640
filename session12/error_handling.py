# try:
#     number = int(input('Please enter a number: '))
#     result = 2019/number
#     print(result)
#     name = 'Babson'
#     print(name[number])
# except ZeroDivisionError as e:
#     print('Something is wrong!',e)
# except ValueError as e:
#     print('Something is wrong!',e)
# except IndexError as e:
#     print(e)
# else:
#     print('This number is good')
# finally:
#     print('This is finally')
# # else will show up only when there is no error, finally will show up no matter there is an error or not

# # Purpose is no matter there is error above or not, reach print below
# print('After something is wrong, we still can get here!')

def reverse_lookup(d,v):
    for k in d:
        if d[k] == v:
            return k
    raise LookupError()

name_dict = {'Julie':90, 'Julia':80, 'Jennie':100}
try:
    print(reverse_lookup(name_dict,70))
except LookupError as e:
    print('There is no such value.')