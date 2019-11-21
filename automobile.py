class Automobile(object):
    def __init__(self, make, model, mileage, price):
        self.__make = make
        self.__model = model
        self.__mileage = mileage
        self.__price = price

    def set_make(self, make):
        self.__make = make

    def get_make(self):
        return self.__make

    def set_model(self, model):
        self.__model = model

    def get_model(self):
        return self.__model

    def set_mileage(self, mileage):
        self.__mileage = mileage

    def get_mileage(self):
        return self.__mileage

    def set_price(self, price):
        self.__price = price

    def get_price(self):
        return self.__price

class Car(Automobile):
    def __init__(self, make, model, mileage, price, doors):
        Automobile.__init__(self, make, model, mileage, price)

        self.__doors = doors

    def set_doors(self, doors):
        self.__doors = doors

    def get_doors(self):
        return self.__doors

    def __str__(self):
        return f"""
        Make:       {self.get_make()}
        Model:      {self.get_model()}
        Mileage:    {self.get_mileage()}
        Price:      ${self.get_price()}
        Doors:      {self.get_doors()}
        """

class Truck(Automobile):
    def __init__(self, make, model, mileage, price, drive_train):
        Automobile.__init__(self, make, model, mileage, price)

        self.__drive_train = drive_train

    def set_drive_train(self, drive_train):
        self.__drive_train = drive_train

    def get_drive_train(self):
        return self.__drive_train

    def __str__(self):
        return f"""
        Make:       {self.get_make()}
        Model:      {self.get_model()}
        Mileage:    {self.get_mileage()}
        Price:      ${self.get_price()}
        Drivetrain: {self.get_drive_train()}
        """

def print_automobile(automobile: Automobile):
    print(automobile)


def main():
    sams_car = Car("Honda", "EX", 125000, 3000, 2)
    kates_truck = Truck("GMC", "Sierra", 20000, 35000, "4x4")
    kaylee_car = Car("Toyota", "Camry", 45000, 18000, 4)

    print_automobile(sams_car)
    print_automobile(kates_truck)
    print_automobile(kaylee_car)

if __name__ == "__main__":
    main()