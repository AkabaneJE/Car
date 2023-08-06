class Car:
    def __init__(self,make,model,year,speed=0):
        self.make = make
        self.model = model
        self.year = year
        self.speed = speed
    def accelerate(self,speed):
        self.speed += speed
        print(f"The {self.make} {self.model} is now going {self.speed} mph")
    def brake (self,speed):
        self.speed -= speed
        if self.speed < 0:
            self.speed - 0
        print(f"The {self.make} {self.model} is now going {self.speed} mph")

