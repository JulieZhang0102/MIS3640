import string
print(string.punctuation)

import random
def histogram(s):
    d = {}
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

t = ['a', 'a', 'b']
hist = histogram(t)
print(hist)

def random_word(h):
    t = []
    for word, freq in h.items():
        t.extend([word] * freq)

    return random.choice(t)