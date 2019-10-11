# def histogram(x):
#     '''
#     Count the number of letter for each letter in the string x
#     '''
#     d = dict()
#     for letter in x:
#         if letter not in d:
#             d[letter] = 1
#         else:
#             d[letter] += 1
#     return d

# print(histogram('bookkeeper')) 

# def histogram(x):
#     '''
#     Count the number of letter for each letter in the string x
#     '''
#     d = dict()
#     for letter in x:
#         d[letter] = d.get(letter,0) + 1
#     return d

# print(histogram('bookkeeper')) 

# with open('session11/she_loves_you.txt') as f:
#     lyrics = f.read().split()
#     print(lyrics)

# def histogram(x):
#     '''
#     Count the number of letter for each letter in the string x
#     '''
#     d = dict()
#     for letter in x:
#         d[letter] = d.get(letter,0) + 1
#     return d

# def print_hist(n):
#     for c in n:
#         print(c, n[c])

# beatles = histogram(lyrics)
# print_hist(beatles)

# def reverse_lookup(d, v):
#     for k in d:
#         if d[k] == v:
#             return k
#     raise LookupError('value does not appear in the dictionary')

# h = {'Julie': 2, 'Julia': 4, 'Jennie': 8}
# key = reverse_lookup(h, 2)
# print(key)

# def invert_dict(d):
#     inverse = dict()
#     for key in d:
#         val = d[key]
#         if val not in inverse:
#             inverse[val] = [key]
#         else:
#             inverse[val].append(key)
#     return inverse

# hist = histogram('parrot')
# print(hist)
# inverse = invert_dict(hist)
# print(inverse)