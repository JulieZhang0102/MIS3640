# print('Please enter your name:')
first_name = input('Please enter your first name:')
last_name = input('Please enter your last name:')

full_name = first_name + ' ' + last_name

print('Hello,', full_name + '!')

print('Hello, {}!'.format(full_name))

print(f'Hello, {full_name}!')