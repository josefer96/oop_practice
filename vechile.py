# parent Class
class vechile:
    
    wheels = 4 # class level attribute assigned to all objects from the class
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        