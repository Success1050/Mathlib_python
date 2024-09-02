class Person:
    color= None

def human(person):
    person.color= "blue"

emma= Person()
human(emma)

print(emma.color)

class Duck:
    def talk(self):
        print(f"the duck is talking")
    def walk(self):
         print(f"the duck is walking")

class Chicken:
    def talk(self):
        print(f"the chicken is talking")
    def crow(self):
         print(f"the chicken is crow")

class Success():
    def catch(self, animal):
        animal.crow()
        animal.talk()
        print("you caught the critter")


# duck= Duck()
# chicken= Chicken()
# success= Success()

# print(success.catch(chicken))

foods= list()

# while True:
#     food =input("whats your favorite food?")
#     if food == "quit":
#         break

#     foods.append(food)


