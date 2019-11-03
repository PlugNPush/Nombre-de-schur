import random

from classes import Color
from classes import Element
from classes import Triplet

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
    
    
# exo2()


def exo3():
    colors = Color()
    
    aa = Element(8, colors.red)
    ba = Element(5, colors.red)
    ca = Element(13, colors.red)
    
    ab = Element(9, colors.purple)
    bb = Element(1, colors.blue)
    cb = Element(10, colors.green)
    
    tripletrouge = Triplet(aa, ba, ca)
    tripletrandom = Triplet(ab, bb, cb)
    
    if tripletrouge.isSameColor():
        print("Le triplet rouge est de la même couleur.")
    else:
        print("Le triplet rouge n'est pas de la même couleur.")
        
    if tripletrandom.isSameColor():
        print("Le triplet random est de la meme couleur.")
    else:
        print("Le triplet random n'est pas de la même couleur.")

exo3()


def exo4():
    print("TBD")
