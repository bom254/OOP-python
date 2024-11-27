class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model

    def mode(self):
        return "Driving"

# Creating objects with unique attributes
car1 = Car("blue", "SUV")
car2 = Car("red", "Sedan")

print(car1.color, car1.model)

class Plane:
    def __init__(self, color):
        self.color = color
    
    def mode(self):
        return "Flying"
    
for motion in [Car(color="Red", model="SUv"), Plane(color="Blue")]:
    print(motion.mode())