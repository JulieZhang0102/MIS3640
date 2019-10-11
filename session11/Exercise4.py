# with open('session11/words.txt') as f:
#     keys = f.read().split()

# def store_as_key(w):
#     d = dict()
#     for words in w:
#         d[words] = 0
#     return d

# print(store_as_key(keys))

# print('Julie' in store_as_key(keys))

def has_duplicates(l):
    d = dict()
    for i in l:
        d[i] = d.get(i,0) + 1
        if d[i] > 1:
            return True
    return False

list1 = ['Julie','Jennie','Julia','Jennie']
print(has_duplicates(list1))

