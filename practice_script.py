class car:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def __str__(self):
        return ("the name of the car is {} and the color is {}".format(self.name, self.color))
    
class Bus(car):
    pass

class jeep(car):
    pass

benz = car("mx", "grey")
print(benz)

benz = car("model 3", "red")
print(benz)

print(car("mx", "grey") == car("mx", "grey"))

print(issubclass(jeep, Bus))
print(isinstance(benz, car))
#is