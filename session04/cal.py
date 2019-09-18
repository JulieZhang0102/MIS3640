# print(abs(-100))
# print(min(5,6,7,-1))
# print(max(5,7,6,-2))
# print(ord('a'))
# print(chr(97))
# print(round(3.76))



# challenge
# print(2**38)
# print(chr(ord('K')+2))
# encrypted_msg = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
# decoded_msg = ''
# for letter in encrypted_msg:
#     if letter.isalpha():
#         decoded_msg += chr(ord(letter)+2)
#     else:
#         decoded_msg += letter
# print(decoded_msg)

# import math
# ratio = 100
# print(math.log10(ratio))

# def print_lyrics():
#     print('Hey Jude. Don\'t make it bad.')
#     print('Take a sad song and make it better.')
# # print_lyrics()
# # print(type(print_lyrics))
# def repeat_lyrics():
#     print_lyrics()
#     print('lalalalla')
#     print_lyrics()
# # repeat_lyrics()

# def print_twice(whatever):
#     print(whatever)
#     print(whatever)
# print_twice('Julie')

# her_name = 'Julie'
# print_twice(her_name)
# print_twice(42)

# def myabs(a):
#     if a >= 0:
#         print(a)
#     else:
#         print(-a)
# myabs(3)
# myabs(-8)
# myabs(0)
# myabs(-8.54)

# def give_me_a_break():
#     msg = 'break'
#     return msg
# print(give_me_a_break())
# return will end the function, whatever after that will not work. But if put before, will work

# def give_me_a_break():
#     msg = 'break'
#     print('another break')
#     return msg
# print(give_me_a_break())
# NOTICE: 'another break' will show up first, 'break' will show later

def my_abs(number):
    if isinstance(number, float):
        if number>=0:
            return number
        else:
            return -number
    else:
        return 'I don\'t know.'
print(my_abs(-0.6))
print(my_abs('A'))

#from my_abs import my_abs

# def f1():
#     pass
