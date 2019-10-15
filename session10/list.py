# b = ['span', 2.0, 5, [10, 20]]
# print(len(b))
# print(b[0])
# b[0] = 'link'
# print(b[0])
# print(b[3])
# print(b[3][0])
# print(5 in b)
# print(100 in b)

# numbers = [2, 0, 1, 6, 9]

# for i in range(len(numbers)):
#     numbers[i] = numbers[i] * 2

# print(numbers)

# a = [1, 2, 3]
# b = [4, 5, 6]
# c = a + b
# print(c)
# print(c[0:2])
# # skip number
# print(c[::2])
# print(c[::-1])
# print(c[::-2])

# x = [0] * 4
# print(x)
# # Add as a whole
# x.append(3)
# print(x)
# # Add as speprate
# x.extend('369')
# print(x)
# x.reverse()
# print(x)

# t = ['a', 'Julie', 'd', 'e', 'f']
# t[1] = 'Nico'
# print(type(t[1]))
# print(t)
# t[1:3] = 'Nico'
# print(type(t[1:3]))
# print(t)

# names = ['Julie', 'Rachel', 'Julia']
# boys = ['Jack', 'John']
# names.extend(boys)
# print(names)
# names = ['Julie', 'Rachel', 'Julia']
# names.append(boys)
# print(names)
# sppend consider as one item, extend consider as few items

# def capitalized_all(t):
#     result = []
#     for word in t:
#         result.append(word.capitalize())
#     return result

# names = ['julie', 'rachel', 'julia']
# print(capitalized_all(names))

# t = [1, 2, 3]
# print(sum(t))

# def only_upper(t):
#     res = []
#     for s in t:
#         if s[0].isupper():
#             res.append(s)
#     return res
# names = ['JULIE', 'rachel', 'Julia']
# print(only_upper(names))

# names = ['julie', 'rachel', 'julia']
# # With nothing in (), remove last element
# no_name = names.pop(1)
# print(names)
# print(no_name)

# names = ['julie', 'rachel', 'julia']
# del names[0]
# print(names)

# # Only remove the first item that meets condition
# names = ['julie', 'rachel', 'julia']
# names.remove('julia')
# print(names)

# name = 'Julie'
# letter = list(name)
# print(letter)
# print(''.join(letter))
# print('!!'.join(letter))

# team = 'New England Patriots'
# word = team.split()
# print(word)
# print(' '.join(word))

# a = 'banana'
# b = 'banana'
# print(a is b)

# a = [1, 2, 3]
# b = [1, 2, 3]
# print(a is b)

# #List will be influenced once being aliased
# a = [1, 2, 3]
# b = a
# print(a is b)

# b[0] = 'something else'
# print(a)
# #a will change as well

# 3 ways to add element to list
# t.append(x)
# t = t + [x]
# t += [x]

# t = ['5','4','3','2','1']
# t.sort()
# print(t)

# t = [3, 1, 2]
# t2 = t[:]
# # Copy the list will not cause aliased problem
# t2.sort()
# print(t)
# print(t2)
