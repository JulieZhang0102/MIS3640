# name = 'Julie'
# for i, letter in enumerate(name):
#     print(i, letter)

# for i, _ in enumerate(name):
#     print(i)

# """
# Four suspects; one of them is a thief. In interrogation
#     John said: I am not the thief.
#     Paul said: George is the thief.
#     George said: It must be Ringo.
#     Ringo said: George is lying.
# Among them, three are telling the truth while one is lying.
# Could you find out who is the thief?
# """
# suspects = ['John', 'Paul', 'George', 'Ringo']
# for name in suspects:
#     if sum([
#         "John" != name,
#         "George" == name,
#         "Ringo" == name,
#             "Ringo" != name]) == 3:
#         print(name)

# sorted(x) will not change orginal list x, return a temporary list unless assign to a new name
# x.sort() will change the orginal list x, and this return nothing

# When import funtion from other file, the funcion will run testing code first before run anything in the current file.
# To avoid that, use code below, change pass to testing code
# if __name__ == "__main__":
#     pass

# names = ['Emely','Krishna','Patrick']
# grades = [90, 80, 65]
# for i in range(3):
#     print(names[i], grades[i])

# grades = dict()
# grades['Emely'] = 90
# grades = {'Emely': 90, 'Krishna': 80, 'Patrick': 70}
# print(len(grades))
# print(grades['Krishna'])
# print('Julie' in grades)
# print(90 in grades.values())

# for name, score in grades.items():
#     if score > 75:
#         print (name, score)

# for score in grades.values():
#     if score > 75:
#         print (score)

# grades = {'Emely': 90, 'Krishna': 80, 'Patrick': 70}
# print(grades.get('Julie', 0))