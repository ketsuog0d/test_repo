class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return 'Woof'

class Cat(Animal):
    def make_sound(self):
        return 'Meow'

class Cow(Animal):
    def make_sound(self):
        return 'Muuuu'

dog = Dog()
cat = Cat()
cow = Cow()

print('Sobaka: ', dog.make_sound())
print('Koshka: ', cat.make_sound())
print('Korova: ', cow.make_sound())

