class Customer:
    def __init__(self,name,age):
        self.name = name
        self.age = age

        # Getters
    def getName(self):
        return self.name

    def getAge(self):
        return self.age

        # Setters
    def setName(self, value):
        self.name = value

    def setAge(self, value):
        self.age = value



class Bike:
    def __init__(self,name,price,maxSpeed):
        self.name = name
        self.price = price
        self.maxSpeed = maxSpeed

        # Getters
    def getName(self):
        return self.name

    def getPrice(self):
        return self.price

    def maxSpeed(self):
        return self.maxSpeed

        # Setters
    def setName(self, value):
        self.name = value

    def setPrice(self, value):
        self.price = value

    def setmaxSpeed(self, value):
        self.maxSpeed = value

    def __repr__(self):
        return f"user({self.name})"


class ElectricBike(Bike):
    def __init__(self,name, price, maxSpeed , batteryTime):
        super().__init__(name, price, maxSpeed )
        self.batteryTime = batteryTime
     #Getter
    def getMaxSpeed(self):
        return self.maxSpeed()
     #Setter
    def setMaxSpeed(self,value):
         self.maxSpeed= value

class NormalBike(Bike):
    def __init__(self,name, price, maxSpeed , numberOfWheels):
        super().__init__(name, price, maxSpeed )
        self.numberOfWheels = numberOfWheels
        # Getter

    def getNumberOfWheels(self):
        return self.numberOfWheels()
        # Setter
    def setNumberOfWheels(self, value):
        self.numberOfWheels = value

    def __repr__(self):
        return f"Normal({self.name})"

data = [NormalBike("Bike1",1000,180,2),ElectricBike("Bike2",1000,200,24)]

for i in data:
    print (i.getName())



class MainBikeRental:
    def __init__(self):
        self.listOfBikes=[]
        self.listOfRentals=[]

    def getListOfBikes(self):
        return self.listOfBikes

    def getListOfRentals(self):
        return self.listOfRentals

    def setListOfBikes(self,value):
         self.listOfBikes.append(value)

    def setListOfRentals(self, value):
        self.listOfRentals.append(value)

    def requestBike(self,numberOfBikes,user):
        if(user.getAge() > 6):
            if len(self.listOfBikes)>= numberOfBikes:
                for i in range(numberOfBikes):
                    self.listOfBikes.pop()
                self.listOfRentals.append(user)
            else:
                print("wait 10 mins")
        else:
            print("You cant rent a bike")

    def returnBike(self,rentalTime,nunOfBikes,user):
        cost = rentalTime * nunOfBikes * 40
        for i in range(nunOfBikes):
            self.listOfBikes.append(NormalBike("Bike1",1000,180,2))

        for i,v in enumerate(self.listOfRentals):
            if v.getName() == user.getName():
                self.listOfRentals.pop(i)

        return cost





system = MainBikeRental()
#[NormalBike("Bike1",1000,180,2),ElectricBike("Bike2",1000,200,24)]
system.setListOfBikes(NormalBike("Bike1",1000,180,2))
system.setListOfBikes(ElectricBike("Bike2",1000,200,24))
c = Customer("Ahmed",10 )
c2 = Customer("Ahmed2",10 )

system.requestBike(1,c)
system.requestBike(1,c2)

system.returnBike(3,1,c)

print(system.getListOfBikes())
print(system.getListOfRentals())




class User:
    def __init__(self, name,id, bookBorrowed,email ):
        self.name = name
        self.id = id
        self.bookBorrowed = bookBorrowed
        self.email = email
    def borrowBook (self, book):
        print (f"{self.name} has booroed the book {book.title}")

    def returnBook (self, book):
        print(f"{self.name} has booroed the book {book.title}")

    def searchBook(self,booktitle):

        print(f"this Book {booktitle} is not found")
        print(f"this Book {booktitle} is  found")
        return None









