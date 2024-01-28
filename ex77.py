class Rectangle:
    def __init__(self,length,widht):
        self.lenght = length
        self.widht  = widht
        
class Square(Rectangle):
    
    def __init__(self,length,widht):
        super().__init__(length,widht)
    
    def area(self):
        return self.lenght*self.widht
    
class Cube(Rectangle):
    def __init__(self, length, widht,height):
        super().__init__(length, widht)
        self.height = height
        
    def volume(self):
        return self.lenght*self.widht*self.height

square = Square(3,3)
cube   = Cube(3,3,3)

print(square.area())
print(cube.volume())