class Vehicle:
    def __init__(self,brand:str , year:int):
        self.brand = brand
        self.year = year
    def print_my_info(self):
        print("I'm general print my info method")
        
class Car(Vehicle):
    # brand = "BMW"
    # year = 2024
    my_class = "Car"

    def __init__(self,brand:str , year:int, wheels = 4):
        super().__init__(brand,year)
        self.wheels = wheels

    def print_my_info(self):
        print(f"I'm {self.brand} car with {self.wheels} wheels")        




class Truck(Vehicle):
    # brand = "BMW"
    # year = 2024
    my_class = "Truck"

    def __init__(self,brand:str , year:int , wheels = 8 , hp =500):
        super().__init__(brand,year)
        self.wheels = wheels
        self.hp = hp


    def print_my_info(self):
        print(f"I'm{self.year} {self.brand} truck with {self.wheels} wheels ,I have {self.hp} hp")        

bmw_car = Car("BMW" ,2024,5)
bmw_car.print_my_info()
# print(Car.brand)
print(Car.my_class)
vw_car = Truck("VW",2015)
vw_car.print_my_info()

