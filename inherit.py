class a:
    def showa(self):
        print("I am in class a")

class b(a):
    def showb(self):
        print("I am in class b")

if __name__=='__main__':
    obj=b()
    obj.showa()
    obj.showb()

#multiLevel
class a:
    def showa(self):
        print("I am in class a")

class b(a):
    def showb(self):
        print("I am in class b")

class c(b):
    def showc(self):
        print("I am in class c")

if __name__=='__main__':
    obj=c()
    obj.showa()
    obj.showb()
    obj.showc()