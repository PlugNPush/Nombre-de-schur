import random

class Color:
    def __init__(self):
        self.white = '\033[0m'
        self.red = '\033[31m'
        self.green = '\033[32m'
        self.orange = '\033[33m'
        self.blue = '\033[34m'
        self.purple = '\033[35m'
        self.colors = [""] * 6
        self.colors[0] = self.white
        self.colors[1] = self.red
        self.colors[2] = self.green
        self.colors[3] = self.orange
        self.colors[4] = self.blue
        self.colors[5] = self.purple
                

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
    for i in range(1, n+1):
        if i%2 == 0:
            print(colors.red, i)
        else:
            print(colors.blue, i)

# exo1()



def exo2():
    colors = Color()
    x = int(input("Combien de nombres: "))
    n = int(input("Combien de couleurs ? (n <= 6): "))
    colorselection = [""] * 6
    colorselection = random.sample(colors.colors, n)
    for i in range(1, x+1):
        print(random.choice(colorselection), i)
    
    
exo2()
