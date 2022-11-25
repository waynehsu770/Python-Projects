



class Vehicle:
    typeOf = "Unknown"
    brand = "Unknown"
    engine = "Unknown"
    origin = "Unknown"
    price = "Unknown"
    seats = None
    fuel_based = True

    def info(self):
        msg = "\nType: {}\nBrand: {}\nEngine: {}\nOrigin: {}\nPrice: {}\nSeats: {}\nFuel Based: {}".format(self.typeOf,self.brand,self.engine,self.origin,self.price,self.seats,self.fuel_based)
        return msg


# child class instance
class Car(Vehicle):
    typeOf = 'Sedan'
    brand = 'Mercedes'
    subclass = 'E350'
    engine = 'V6'
    price = '$70,000 USD'
    origin = 'Germany'
    seats = 5

    def info(self):
        msg = "\nType: {}\nBrand: {}\nClass: {}\nEngine: {}\nOrigin: {}\nPrice: {}\nSeats: {}\nFuel Based: {}".format(self.typeOf,self.brand,self.subclass,self.engine,self.origin,self.price,self.seats,self.fuel_based)
        return msg
    
    def specification(self):
        msg = "\nA powerful luxury sedan that is good for a small family."
        return msg


# another child class instance
class Plane(Vehicle):
    typeOf = "Commercial Plane"
    brand = 'Boeing'
    subclass = '747'
    engine = 'Rolls-Royce RB211'
    origin = 'Seattle, Washington'
    price = '418 Million USD'
    seats = 366
    wheels = 18

    def info(self):
        msg = "\nType: {}\nBrand: {}\nClass: {}\nEngine: {}\nOrigin: {}\nPrice: {}\nSeats: {}\nWheels: {}\nFuel Based: {}".format(self.typeOf,self.brand,self.subclass,self.engine,self.origin,self.price,self.seats,self.wheels,self.fuel_based)
        return msg
    
    def details(self):
        msg = "\nOne of the most widely used commerical airplanes"
        return msg



if __name__ == "__main__":
    car = Car()
    print(car.info())
    print(car.specification())

    plane = Plane()
    print(plane.info())
    print(plane.details())
