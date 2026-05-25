class parent:
    def __init__(self):
        self.speed=100
        print("cash,gold")

    def bike(self):
        print("splendor",self.speed)

class child(parent):
    def __init__(self):
        self.speed=150
    def bike(self):
        print("HB",self.speed)
    
obj=child()
obj.bike()