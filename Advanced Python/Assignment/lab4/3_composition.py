class Engine:
    a = 100
    
    def __init__(self):
        self.b = 200
        
    def m1(self):
        print("This is Engine cls method...")
        
class car:
    def __init__(self):
        self.engine = Engine()
    
    def m2(self):
        print("This is Car cls method..")
        print("Static Variable =", self.engine.a)
        print("Instance Variable =", self.engine.b)
        self.engine.m1()
        
        
car1 = car()
car1.m2()