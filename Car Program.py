class Car:
    def __init__ (self, make, model, year, price, sixty_time, coupe, has_launch):
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        self.sixty_time = sixty_time
        self.coupe = coupe
        self.has_launch = has_launch

    @property
    def modelGet(self):
        print("Getting model: ")
        print(self.model)
    
    @modelGet.setter
    def modelGet(self, model):
        print("Setting model...")
        self.model = model
        print(self.model)
    
    def go_vroom(self):
        print(self.model + " go vroom!")  
    
    def __str__(self):
        return "The " + self.make +" car that you are interested in is the " + str(self.year) + ' ' + self.model + " " + self.coupe + ". It has a 0-60 time of " + str(self.sixty_time) + " seconds and costs $" + str(self.price) +"."


class Crossover:
    def __init__ (self, make, model, year, price, for_vegans):
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        self.for_vegans = for_vegans
    def go_vroom(self):
        print("Crossovers don't go vroom :(")
    def __str__(self):
        return "The " + self.make +" crossover that you are interested in is the " + str(self.year) + ' ' + self.model + ". It costs $" + str(self.price) +"."



class Truck:
    def __init__(self, make, model, year, price, american):
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        self.american = american

    @property
    def go_vroom(self):
        print(self.model + " go vroom!")

    def __str__(self):
        return "The " + self.make +" truck that you are interested in is the " + str(self.year) + ' ' + self.model + ". It costs $" + str(self.price) +"."

toyotaCar = Car("Toyota", "Corolla", 2006, 4000, 8.6, "sedan ", False )
mercedesCar = Car("Mercedes", "C43 AMG", 2019, 45000, 4.5, "coupe", False)
bmw1Car = Car("BMW", "M240i", 2019, 45000, 4.3, "coupe", True)

mercedesCrossover = Crossover("Mercedes", "GLC 300 4Matic", 2019, 40000, True)
bmw1Crossover = Crossover("BMW", "X3 M40i", 2019, 44000, False)
audiCrossover = Crossover("Audi", "Q5 Premium 45 TSFi", 2019, 39500, True)

fordTruck = Truck("Ford", "F150 Raptor", 2018, 65000, True)
chevroletTruck = Truck("Chevrolet", "Silverado 1500 RST", 2018, 42000, True)

#print(mercedesCar.go_vroom) #using property Getter
#mercedesCar.modelGet = "Hyundai" #using property Getter and Setter

# Review My Car Options

print("Do you want to review a car, truck, or crossover?")
typeselector = input()

if typeselector == "car":
    print("Mercedes, Toyota, BMW, or All?")
    modelselect1 = input()
    if modelselect1 == 'Mercedes':
        print(mercedesCar)
    elif modelselect1 == 'Toyota':
        print(toyotaCar)
    elif modelselect1 == 'BMW':
        print(bmw1Car)
    elif modelselect1 == 'All':
        print(str(mercedesCar) +  '\n' +  str(bmw1Car) + '\n' + str(toyotaCar) )
    else:
        print("Please type Mercedes, Toyota, BMW, or All exactly as written (caps)")

elif typeselector == "truck":
    print("Ford or Chevrolet?")
    modelselect2 = input()
    if modelselect2 == "Ford":
        print(fordTruck)
    elif modelselect2 == "Chevrolet":
        print(chevroletTruck)
    elif modelselect2 == "All":
        print(str(chevroletTruck) + '\n' + str(fordTruck))
    else:
        print("Please type Ford, Chevrolet or All exactly as written.")

elif typeselector == "crossover":
    print("Mercedes, BMW, or Audi?")
    modelselect3 = input()
    if modelselect3 == "Mercedes":
        print(mercedesCrossover)
    elif modelselect3 == "Audi":
        print(audiCrossover)
    elif modelselect3 == "BMW":
        print(bmw1Crossover)
    elif modelselect3 == "All":
        print(str(bmw1Crossover) + '\n' + str(audiCrossover) + '\n' + str(mercedesCrossover))
    else:
        print("Please type Audi, BMW, Mercedes, or All exactly as written.")

else:
    print("Please type car, truck, crossover exactly as written.")

print("Nice job with the car.")