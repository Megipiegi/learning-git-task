class Car:
    def __init__ (self, make, model_name, top_speed, colour):
        self.make=make
        self.model=model_name
        self.top_speed=top_speed
        self.colour=colour
        self.current_speed = 0
car = Car(make="Ford", model_name="Mustang", top_speed=250, colour="Red")
    def accelerate(self, step=10):
        self.current_speed += step
    def decelerate(self, step=10):
        self.current_speed -= step
car.top_speed
print(car)