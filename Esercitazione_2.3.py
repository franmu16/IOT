class IntPair:
    a = 0
    b = 0
    
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __str__ (self):
        print("ip(%d,%d)" %(self.a,self.b))
    
    def mul (self):
        return self.a*self.b
    
class IntPairK(IntPair):
    k = 0
    
    def __init__ (self,a,b,k):
        IntPair.__init__(self,k*a,k*b)
        self.k = k
        
    
    def __str__ (self):
        return("ip(%d,%d)" %(self.a,self.b))

    
i = IntPairK(4,3,2)
print(i.__str__(),i.mul())