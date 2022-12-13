# Object-Oriented Programming (OOP) exercise

class emptyObject:
    pass

class Vehicle:
    color = 'white'
    def __init__(self, name, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
        self.name = name
    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"
    def fare(self):
        return self.capacity * 100

# 仅继承，不做任何更改
class Bus(Vehicle):
    pass
    # def __init__(self, name, max_speed, mileage):
    #     super().__init__(name, max_speed, mileage)

class Car(Vehicle):
    capacity = 50
    def __init__(self, name, max_speed, mileage):
        super().__init__(name, max_speed, mileage)

    # 重写父类方法 
    def seating_capacity(self, capacity = 50):
        return super().seating_capacity(capacity)
    def fare(self):
        return (super().fare()) * 1.1

def main():
    # bus = Bus('bus', 240, 80)
    # print(bus.color)

    car = Car('car', 120, 600)
    print(car.color)
    print(car.seating_capacity())
    print(car.fare())
    # 检查属于哪一个类
    print(type(car))

main()