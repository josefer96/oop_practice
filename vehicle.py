# parent Class
class Vehicle:
    
    wheels = 4 # class level attribute assigned to all objects from the class
    all_vehicles = []
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        
        Vehicle.all_vehicles.append(self)
        
    def __str__(self):
        #return a string representing the vehcile object
        return f"Vehicle: {self.make}, Model {self.model}, year: {self.year}"
        
        
    @classmethod
    def get_all_vehicles(cls):
        return cls.all_vehicles
        