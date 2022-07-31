# Victoria Bates
# CIS245 7.1

class vehicles:
  def __init__(self):
    self.vehicle_options = {'make': '', 'model': ''}

  def setMake(self, make):
    self.vehicle_options['make'] = make

  def setModel(self, model):
    self.vehicle_options['model'] = model
    
  def displayOptions(self):
    print(f"You have added the following vehicle to your inventory: ")
    print("Make: " + {self.vehicle_options['make']})
    print("Model: " + {self.vehicle_options['model']})

#car subclass
class car(vehicles):
  def __init__(self):
    super().__init__()
    

  def setCarDoorNum(self, carDoorNum):
    self.vehicle_options['carDoorNum'] = carDoorNum

  def displayOptions(self):
    print("")
    print("You have added the following vehicle to your inventory: ")
    print(f"Make: {self.vehicle_options['make']}")
    print(f"Model: {self.vehicle_options['model']}")
    print(f"Number of doors: {self.vehicle_options['carDoorNum']}")
    print("")


#truck subclass - I changed it from "pickup" to "truck" for my own sanity
class truck(vehicles):
  def __inti__(self):
    super().__init__()

  def setBedLength(self, bedLength):
    self.vehicle_options['bedLength'] = bedLength

  def displayOptions(self):
     print("")
     print("You have added the following vehicle to your inventory: ")
     print(f"Make: {self.vehicle_options['make']}")
     print(f"Model: {self.vehicle_options['model']}")
     print(f"Bed Length: {self.vehicle_options['bedLength']}")
     print("")


print("Welcome to Vroom Vroom Garage!")
print("")

vehicle_type = "0"

while vehicle_type != "3":
  vehicle_type = input("Please enter 1 to add a car to your inventory, 2 to add a truck, or enter 3 to quit. ")
  if (vehicle_type == "1"):
    new_vehicle = car()
    carMake = input("Enter make: ")
    carModel = input("Enter model: ")
    carDoorNum = input("Enter number of doors: ")
    new_vehicle.setMake(carMake)
    new_vehicle.setModel(carModel)
    new_vehicle.setCarDoorNum(carDoorNum)
    new_vehicle.displayOptions()
  elif (vehicle_type == "2"):
    new_vehicle = truck()
    truckMake = input("Enter Make: ")
    truckModel = input("Enter Model: ")
    truckBedLength = input("Enter Bed Length: ")
    new_vehicle.setMake(truckMake)
    new_vehicle.setModel(truckModel)
    new_vehicle.setBedLength(truckBedLength)
    new_vehicle.displayOptions()
  elif (vehicle_type == "3"):
    print("")
    print("Bye! Nyooooommmmm")
  
  
    
  