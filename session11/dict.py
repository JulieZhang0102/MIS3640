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