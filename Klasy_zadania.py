class Car:
    def __init__(self, make, model_name, top_speed, color):
        self.make = make
        self.model_name = model_name
        self.top_speed = top_speed
        self.color = color
car_one = Car(make="Ford", model_name="Mustang", top_speed=250, color="Red")
car_two = Car(make="Ford", model_name="Fiesta", top_speed=200, color="Blue")
car_three = Car(make="Porsche", model_name="911", top_speed=320, color="Black")
cars=[car_one, car_two, car_three]
by_speed= sorted(cars, key=lambda car: car.top_speed)
by_make=sorted(cars, key=lambda car: car.make)
for i in by_speed:
    print (i.top_speed)