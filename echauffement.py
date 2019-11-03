class Color:
    def __init__(self):
        self.white = '\033[0m'
        self.red = '\033[31m'
        self.green = '\033[32m'
        self.orange = '\033[33m'
        self.blue = '\033[34m'
        self.purple = '\033[31m'
        
class Element:
    def __init__(self, a, b):
        self.value = a
        self.color = b
        
class Triplet:
    def __init__(self, a, b, c):
        self.element = a
        self.element2 = b
        self.element3 = c
    
    def isSameColor(self):
        if self.element.color == self.element2.color and self.element.color == self.element3.color:
            return True
        else:
            return False
        
def exo1():
    colors = Color()
    n = int(input("Donnez n: "))
    for i in range(0, n):
        if i%2 == 0:
            print(colors.red, i)
        else:
            print(colors.blue, i)
    
exo1()
