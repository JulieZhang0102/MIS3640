import pickle

with open('session14/saved.p', 'rb') as p:
    t2 = pickle.load(p)

print(t2)