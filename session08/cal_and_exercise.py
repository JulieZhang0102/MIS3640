# team = 'New England Patriots'
# letter = team[0]
# # start counting from 0
# print(letter)
# print(team[1])
# print(team[19])
# print(len(team))

# print(team[-1])
# print(team[-20])

# team = 'New England Patriots'

# index = 0
# while index < len(team):
#     letter = team[index]
#     print(letter)
#     index = index + 1

# for letter in team:
#     print(letter)

# print(letter)
# # last letter in for

# prefixes = 'JKLMNOPQ'
# suffix = 'ack'

# for letter in prefixes:
#     if letter == 'O' or letter == 'Q':
#         print(letter + 'u' + suffix)
#     else:
#         print(letter + suffix)

# team = 'New England Patriots'
# # latter number is exclusive
# print(team[:11])
# print(team[12:])
# print(team[:])

# print(team[::2])
# print(team[::-2])

# Cannot change directly, need to assign another variable
# New_team = team[:12] + 'Giants'
# print(New_team)
# print(team)


# find where is the letter in a word
# def find(word, letter):
#     index = 0
#     while index < len(word):
#         if word[index] == letter:
#             return index
#         index = index + 1
#     return -1


# def count(word, letter):
#     c = 0
#     for ch in word:
#         if ch.lower() == letter:
#             c = c + 1
#     return c

# print(count('Julie', 'e'))

# team = 'New England Patriots'
# new_team = team.upper()
# print(new_team)

# team = 'New England Patriots'
# index = team.find('a')
# print(index)

# # Only the first letter counts
# print(team.find('En'))

# # Find "a" after 9 letters (start inclusive, end exclusive)
# print(team.find('a', 10)) 

# # If not find, return -1
# name = 'bob'
# print(name.find('b', 1, 2))

# print('1,2,3'.split(','))
# print('1,2,3'.split(',', maxsplit=1))
# print('1,2,,3,'.split(','))

# print( '   spacious   '.strip())

# # Will omit from start until reaching a character not in (), same from end. In the middle, do not count
# print('www.example.com'.strip('cmowa.'))

# comment_string = '#....... Section 3.2.1 Issue #32 .......'
# print(comment_string.strip('.#! '))

# print('Julie'.replace('e','a'))

# print('bob'.replace('b','a',1))

# print('a' in 'team')
# print('Boston' in 'team')

# def in_both(word1, word2):
#     for letter in word1:
#         if letter in word2:
#             print(letter)

# in_both('Julie', 'julia')

# # Exercise 4.1 & 4.2
# def price(menu):
#     sum = 0
#     for letter in menu:
#         singal = ord(letter)-96
#         sum = sum + singal
#     return sum

# s1 = " "

# b = 'bananas'
# r = 'rice'
# pa = 'paprika'
# po = 'potato chips'

# p1 = price(b)
# p2 = price(r)
# p3 = price(pa)
# p4 = price(po)

# sum = p1 + p2 + p3 + p4


# print(b, s1*6, '{:>10}'.format('$'), '{:.2f}'.format(p1))
# print(r, s1*9, '{:>10}'.format('$'), '{:.2f}'.format(p2))
# print(pa, s1*6, '{:>10}'.format('$'), '{:.2f}'.format(p3))
# print(po, s1, '{:>10}'.format('$'), '{:.2f}'.format(p4))
# print('-'*31)
# print('Total', s1*7, '{:>10}'.format('$'), '{:.2f}'.format(sum))

# Exercise 5
def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False
# Only check the first letter because 'return' ends the loop

def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'
# Will always return True because it is checking if letter 'c'

def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag
# Only check the last letter because return is outside of 'for' loop

def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag
# Works well

def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True
# It checks if all letter are lowercases or not, not any of them

# Exercise 6
def rotate_word(word, number):
    for letter in word:
        if number >= 0:
            if letter.islower():
                if ord('z') - ord(letter) >= abs(number):
                    new_number = ord(letter) + number
                    new_letter = chr(new_number)
                    print(new_letter)
                else:
                    new_number = ord(letter) - number - 24
                    new_letter = chr(new_number)
                    print(new_letter)
            else:
                if ord('Z') - ord(letter) >= abs(number):
                    new_number = ord(letter) + number
                    new_letter = chr(new_number)
                    print(new_letter)
                else:
                    new_number = ord(letter) - number - 24
                    new_letter = chr(new_number)
                    print(new_letter)
        elif letter.islower():
            if ord(letter) - ord('a') >= abs(number):
                new_number = ord(letter) + number
                new_letter = chr(new_number)
                print(new_letter)
            else: 
                new_number = ord(letter) - 95 + abs(number) + ord(letter)
                new_letter = chr(new_number)
                print(new_letter)
        else:
            if ord(letter) - ord('A') >= abs(number):
                new_number = ord(letter) + number
                new_letter = chr(new_number)
                print(new_letter)
            else: 
                new_number = ord(letter) - 64 + abs(number) + ord(letter)
                new_letter = chr(new_number)
                print(new_letter)

rotate_word('cheer',7)
rotate_word('melon',-10)
rotate_word('IBM',-1)
rotate_word('zoo',1)
rotate_word('Zoo',1)

print(ord('A'))