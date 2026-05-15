"""
class stud:
    def display(self):
        print("I am a student")

    def show():
        print("Hello")

s=stud();
s.display();
stud.show() #static method
"""
class Student:
    def __init__(self):
        print("default constructor")
    def __init__(self,a):
        print(a)
    def __init__(self,a,b):
        print(a,b) #this will be considerred
    
    def show(self):
        print("I am in show")

s=Student(11,22);
s.show();