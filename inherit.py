# class Animal:
#     alive= True
#     def eat(self):
#         print("This animal is eating")
  

# class Rabbit(Animal):
#     def eat(self):
#         print("rabbit is running")



# rabbit= Rabbit()
# rabbit.eat()

class Car:
    def start(self):
        print("you start the car")
        return self
    def drive(self):
        print("you drive the car")
        return self
    def brake(self):
        print("you hit the brake of the car")
        return self
    def stop(self):
        print("you stop the car")
        return self

car= Car()
car.start().drive().brake().stop()



