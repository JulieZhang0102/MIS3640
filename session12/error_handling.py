try:
    number = int(input('Please enter a number: '))
    result = 2019/number
    print(result)
    name = 'Babson'
    print(name[number])
except ZeroDivisionError as e:
    print('Something is wrong!',e)
except ValueError as e:
    print('Something is wrong!',e)
except IndexError as e:
    print(e)

print('After something is wrong, we still can get here!')