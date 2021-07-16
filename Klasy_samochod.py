class Car:
    def __init__(self, make, model_name, top_speed, color):
        self.make=make
        self.model_name=model_name
        self.top_speed=top_speed
        self.color=color
    def __gt__(self, other):
        return self.top_speed > other.top_speed
car1=Car(make='Opel', model_name='Astra', top_speed=200, color='Yellow')
car2=Car(make='Ford', model_name='Mustang', top_speed=250, color='Red')
print(car1<car2)

