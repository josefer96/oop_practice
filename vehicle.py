# parent Class
class Vehicle:
    
    wheels = 4 # class level attribute assigned to all objects from the class
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        
        
        def __str__(self):
            #return a string representing the vehcile object
            return f"vehicle: {self.make}, Model {self.model}, year: {self.year}"