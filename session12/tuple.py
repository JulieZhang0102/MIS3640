# Set is in {}, tuple is in ()

# t = 'a', 'b', 'c'
# print(type(t))
# # t[0] = 'z' immutable

# t = tuple('Babson')
# print(t)

# t = tuple([1,2,3])
# print(t)

# tel = '123-456-7890'
# print(tel.split('-'))

# tel = '123-456-7890'
# print(tel.split('-')[-1])

# a, b, c = tel.split('-')
# print(c)

# # use * to say do not care how many element in list, only want last part c below
# *a, c = tel.split('-')
# print(a)

# tel = '+1-123-234-3456'
# international, *_, local = tel.split('-')
# print(international)
# print(local)

# Above is use tuple to unpack
# Below is use tuple to swich value

# a = 10
# b = 20
# a, b = b, a
# print(a)

# print(divmod(7, 3))

# def f():
#     return 1, 2

# temp, humidity = f()
# print(temp)
# print(humidity)

# def multiply(*a):
#     result = 1
#     for num in a:
#         result *= num
#     return result

# print(multiply(1,2,3,4,5,6))

# set is unordered

# s = set('rrrrrru')
# print(s)

# s.add('e')
# print(s)

# s.add('r')
# print(s)
# # No error but just do not add because it is there already

# s = {1,2,3}
# s1 = {1,2,3}
# s2 = {2,3,4}

# print(s1 & s2)
# print(s1 | s2)

# # Compare to s2, print differences in s1
# print(s1.difference(s2))

# word = 'bookkeeper'
# print(set(word))
# print(list(set(word)))

# name = 'Julie'

# # String and list
# namel = list(name)
# print(namel)
# names = ''.join(namel)
# print(names)

# # String and dictionary
# named = dict()
# for letter in name:
#     named[letter] = named.get(letter, 0) + 1
# print(named)

# String and tuple
# namet = tuple(name)
# print(namet)
# names = ''.join(namet)
# print(names)

# # String and set
# names = set(name)
# print(names)

name = 'Julie'
t = [1,2,3,4,5]
zip(name, t)

for pair in zip(name,t):
    print(pair)

print(list(zip(name,t)))

print(dict(zip(name, t)))

x = dict(zip(name, t))
print(x.items())
