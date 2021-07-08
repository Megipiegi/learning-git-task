class Car:
    def __init__ (self, make, model_name, top_speed, colour):
        self.make=make
        self.model=model_name
        self.top_speed=top_speed
        self.colour=colour
mustang=Car(make='Ford', model_name='Mustang', top_speed='250', colour='yellow')
print(mustang.make)


