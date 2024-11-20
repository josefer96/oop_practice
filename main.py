from vehicle import Vehicle
from car import Car

if __name__ == "__main__":
    
    #Create an instance of the Vechile class
    black_car = Vehicle("tesla", "model 3", 2018)
    red_car = Vehicle("Toyota", "Camry", 2023)
    real_car = car("VW", "Bug", 2012, 2)
    
    all_vehichles = Vehicle.get_all_vehicles()
    for vehicle in all_vehichles:
       print(vehicle)