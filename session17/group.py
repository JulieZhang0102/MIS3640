class Cat:
    '''
    Represent a cat with attrabutes breed, weight, age, eyecolor
    '''

    def __init__(self, breed = "Ragdoll", weight = 10, age = 3, eyecolor = []):
        self.breed = breed
        self.weight = weight
        self.age = age
        self.eyecolor = eyecolor

    def __str__(self):
        return f'Your cat breed is {self.breed}, weight is {self.weight}, age is {self.age}, eyecolor is {self.eyecolor}'

    def __eq_(self, other):
        return self.age == other.age


Tomato = Cat(eyecolor = ['yellow, green'])
print(Tomato)
Potato = Cat(age = 5)
print(Potato == Tomato)