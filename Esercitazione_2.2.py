class IntPair:
    a = 0
    b = 0
    
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __str__ (self):
        return("ip(%d,%d)" %(self.a,self.b))
    
    def mul (self):
        return self.a*self.b
    
i = IntPair(4,3)
print(i.__str__(),i.mul())