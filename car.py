from main import Vehicle

class Car(Vehicle):
    
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors
        
#overriding method
    def __str__(self):
        return super().__str__() + "doors: " + str(self.num_doors)