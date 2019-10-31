a = 1
b = 1
print(a==b) #True
print(a is b) #True

a = 'a'
b = 'a'
print(a==b) #True
print(a is b) #True

a = 'Babson College Julie'
b = a
print(a==b) #True
print(a is b) #True

a = [1,2,3,4,5]
b = [1,2,3,4,5]
print(a==b) #True
print(a is b) #False (different id, store in different places)
print(id(a))
print(id(b))