with open('session11/words.txt') as f:
    keys = f.read().split()

def store_as_key(w):
    d = dict()
    for words in w:
        d[words] = 0
    return d

print(store_as_key(keys))

print('Julie' in store_as_key(keys))

def has_duplicates(l):
    d = dict()
    for i in l:
        d[i] = d.get(i,0) + 1
        if d[i] > 1:
            return True
    return False

list1 = ['Julie','Jennie','Julia','Jennie']
print(has_duplicates(list1))

def create_dict():
    f = open("session09/words.txt")
    words = dict()
    for line in f:
        word = line.strip()
        words[word] = 0
    return words

words_dict = create_dict()

# for w in words_dict:
#     print(w, words_dict[w])

# for w, v in words_dict.items():
#     print(w,v)

def check_word(word, d):
    return word in d

if __name__ == "__main__":
    words_dict = create_dict()
    word = input('Enter a word: ')
    if check_word(word, words_dict):
        print(f'Yes, the word {word} is in the dictionary.')
    else:
        print(f'Sorry, the word {word} is not in the dictionary.')
    