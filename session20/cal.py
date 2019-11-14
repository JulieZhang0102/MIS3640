# from math import log10

# a = log10(100)
# print(a)

# log10 = log10(100) #naming conflict

# print(log10(1000))

# num1 = 10_000_000.1
# num2 = 100_000_000_000

# print(num1)
# total = num1 + num2
# print(total)
# print(f'{total:,}')
# print(f'{total:025,.2f}')

'''
context managers
'''

# f = open('session20/t.txt')
# content = f.read()
# print(content)
# f.close()

# print(len(content.split()))

# better code

# with open('session20/t.txt') as f:
#     content = f.read()

# print(len(content.split()))

'''
Enumerate
'''
# names = ['Julie', 'Julia', 'Jennie']

# # i = 0
# # for name in names:
# #     print(i, name)
# #     i+=1

# # better code

# for i, name in enumerate(names, start=101):
#     print(i, name)

'''
zip
'''

# names = ['Julie Zhang', 'Julia Xu', 'Jennie Zheng']
# heroes = ['Spiderman', 'Superman', 'Batman']
# universes = ['Marvel', 'DC', 'Marvel']

# # for i, name in enumerate(names):
# #     hero = heroes[i]
# #     print(f'{name} is actually {hero}.')

# # better code

# for name, hero, u in zip(names, heroes, universes):
#     print(f'{name} is actually {hero} from {u}.')


