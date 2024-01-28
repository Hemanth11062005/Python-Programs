class Car:
    
    def __init__(self,model,make,year,color):
        self.model = model
        self.make = make
        self.year = year
        self.color = color
    
    def drive(self):
        print(self.model+"is driving")
    
    def stop(self):
        print(self.model+"is stopped")