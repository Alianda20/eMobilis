class Animal:
     def speak(self):
         print("Animal speaking")
class Dog(Animal):
    def bark(self):
        print("Dog barks")

class DogChild(Dog):
    def eats(self):
        print("Drinking milk")
dog=Dog()
dog.speak()
dog.bark()

dogmdogo=DogChild()
dogmdogo.speak()
dogmdogo.bark()
dogmdogo.eats()