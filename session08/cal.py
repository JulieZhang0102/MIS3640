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


def count(word, letter):
    c = 0
    for ch in word:
        if ch.lower() == letter:
            c = c + 1
    return c

print(count('Julie', 'e'))

