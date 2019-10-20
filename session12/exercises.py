# Exercise 2.1
def most_frequent(x):
    d = dict()
    for letter in x:
        d[letter] = d.get(letter, 0) + 1
    t = []
    for key, value in d.items():
        t.append((value, key))
    t.sort()
    t.reverse()
    print(t)

most_frequent('llllllliaaabb')

# Exercise 2.2
from collections import defaultdict

with open('session13/words.txt', 'r') as fd:
    words = fd.read().splitlines()


def make_anagram_dict(word_list):
    """Take a list of words, return a dict with a fingerprint as the key
    and the anagrams made from that fingerprint as the value."""
    result = defaultdict(list)
    for word in word_list:
        fp = ''.join(sorted(word))
        result[fp].append(word)
    a = dict(result)
    for fp in result:
        if len(result[fp]) <= 1:
            del a[fp]
    return a

# print(make_anagram_dict(words))

# Exercise 2.3
def sort_anagram_dict(word_list):
    """ Print the longest list of anagrams first, followed by the second longest, and so on"""
    result = defaultdict(list)
    for word in word_list:
        fp = ''.join(sorted(word))
        result[fp].append(word)
    a = dict(result)
    for fp in result:
        if len(result[fp]) <= 1:
            del a[fp]
    t = []
    for key in a:
        t.append(a[key])
    t.sort(key=len)
    t.reverse()        
    return t

print(sort_anagram_dict(words))