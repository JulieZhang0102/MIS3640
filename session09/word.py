# fin = open("session09/words.txt")
# line = fin.readline()
# word = line.strip()
# print(word)

# for line in fin:
#     word = line.strip()
    # print(word)


# def find_long_words():
#     """
#     prints only the words with more than 20 characters
#     """
#     f = open('session09/words.txt')
#     for line in f:
#         word = line.strip()
#         if len(word) > 20:
#             print(word, len(word))

# find_long_words()


# def has_no_e(word):
#     """
#     returns True if the given word doesn’t have the letter "e" in it
#     """
#     for letter in word:
#         if letter == 'e' or letter == 'E':
#             return False
#     return True

# print(has_no_e('Babson'))
# print(has_no_e('College'))
# print(has_no_e('EA'))


# def find_words_no_e():
#     """
#     returns the percentage of the words that don't have the letter "e"
#     """
#     count = 0
#     num_of_line = 0
#     f = open('session09/words.txt')
#     for line in f:
#         num_of_line +=1
#         word = line.strip()
#         if has_no_e(word):
#              count +=1
#     return count/num_of_line

# print('The percentage of the words with no "e" is {:.2f}%.'.format(
#     find_words_no_e()*100))


# def avoids(word, forbidden):
#     """
#     returns True if the given word does not use any of the forbidden letters
#     """
#     for letter in word:
#         if letter in forbidden:
#             return False
#     return True
        

# print(avoids('Babson', 'abcde'))
# print(avoids('College', 'a'))


# def find_words_no_vowels():
#     """
#     returns the percentage of the words that don't vowel letters
#     """
#     count = 0
#     num_of_word = 0
#     f = open('session09/words.txt')
#     for line in f:
#         num_of_word +=1
#         word = line.strip()
#         if avoids(word, 'aeiou'):
#             count +=1
#     return count/num_of_word

# print('The percentage of the words without vowel letters is {:.2f}%.'.format(
#     find_words_no_vowels()*100))


# def uses_only(word, available):
#     """
#     takes a word and a string of letters, 
#     and that returns True if the word
#     contains all letters available.
#     """
#     for letter in word:
#         if letter not in available:
#             return False
#     return True


# print(uses_only('Babson', 'aBbsonxyz'))
# print(uses_only('college', 'aBbsonxyz'))


# def find_words_using_all_planet():
#     """
#     return the number of the words that use all the planet letters
#     """
#     f = open('session09/words.txt')
#     num_of_word = 0
#     for line in f:
#         word = line.strip()
#         if uses_only(word, 'planet'):
#             num_of_word +=1
#     return num_of_word


# print('The number of words that use all the vowels:',
#       find_words_using_all_planet())



# def uses_all(word, required):
#     """
#     takes a word and a string of required letters, 
#     and that returns True if
#     the word uses all the required letters at least once.
#     """
#     for letter in required:
#         if letter not in word:
#             return False
#     return True

# print(uses_all('Babson', 'abs'))
# print(uses_all('college', 'abs'))
# print(uses_all('Babson', 'aeoiu'))
# print(uses_all('Babesonious', 'aeoiu'))

# def find_words_using_all_vowels():
#     '''
#     return the number of the words that use all the vowel letters
#     '''
#     f = open('session09/words.txt')
#     num_of_word = 0
#     for line in f:
#         word = line.strip()
#         if uses_all(word, 'aeiou'):
#             num_of_word +=1
#     return num_of_word

# print('The number of words that use all the vowels', 
# find_words_using_all_vowels())



# def is_abecedarian(word):
#     """
#     returns True if the letters in a word appear in alphabetical order
#     (double letters are ok).
#     """
#     left = word[0]
#     for letter in word[1:]:
#         if left > letter:
#             return False
#         left = letter
#     return True

# print(is_abecedarian('abb'))
# print(is_abecedarian('college'))


# def find_abecedarian_words():
#     """
#     returns the number of abecedarian words 
#     and the longest abecedarian word
#     """
#     count = 0
#     length = 0
#     f = open('session09/words.txt')
#     for line in f:
#         word = line.strip()
#         if is_abecedarian(word):
#             count +=1
#             if len(word) > length:
#                 length = len(word)
#                 a = word
#     return count, a

# print(find_abecedarian_words())


# def is_abecedarian_using_recursion(word):
#     """
#     returns True if the letters in a word appear in alphabetical order
#     (double letters are ok).
#     """
#     n = len(word)
#     if n >= 2:
#         if word[n-1] < word[n-2]:
#             return False
#         else:
#             word = word[:n-1]
#             return is_abecedarian_using_recursion(word)
#     else:
#         return True

# print(is_abecedarian_using_recursion('baaa'))


# def is_abecedarian_using_while(word):
#     """
#     returns True if the letters in a word appear in alphabetical order
#     (double letters are ok).
#     """
#     n = len(word)
#     while n >= 2:
#         if word[n-1] < word[n-2]:
#             return False
#         else:
#             n-=1
#     return True


# Exercise 3.1

# def is_word_triple(word):
#     count = 0
#     n = len(word)
#     while n >=2:
#         if word[n-1] == word[n-2]:
#             n -= 2
#             count += 1
#             if count == 3:
#                 return True
#         else:
#             n -= 1
#             count = 0
#     return False

# def check_list_triple():
#     f = open('session09/words.txt')
#     for line in f:
#         word = line.strip()
#         if is_word_triple(word):
#             print(word)

# check_list_triple()

# word = "Julie"
# print('le' not in word)