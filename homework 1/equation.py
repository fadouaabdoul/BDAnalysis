
class quadraticEquation:
    def __init__(self, a, b, c): 
        self.a = a
        self.b = b
        self.c = c
        

    def getDescrimant(self):
        desc = (self.b**2) - (4 * self.a * self.c)
        return desc 

    def getRoot1(self):
        if self.getDescrimant() >= 0: 
            t1 = (- self.b-(self.getDescrimant()**2) )/(2 * self.a)
            return t1
        else :
            return "none"      
    def getRoot2(self):
        if self.getDescrimant() >= 0:  
            t2 = (-self.b + (self.getDescrimant()**2))/(2 * self.a)
            return t2 
        else : 
            return "none"
        
obj = quadraticEquation(1,-4,3)
print(obj.getDescrimant())
print(obj.getRoot1())
print(obj.getRoot2())