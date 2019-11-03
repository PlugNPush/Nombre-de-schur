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

# exo3()


def exo4():
    colors = Color()
    p = int(input("Donnez p <= 100: "))
    t = []
    for i in range(1, p):
        for s in range(i, p):
            if i+s <= p:
                t.append(Triplet(Element(i, colors.white), Element(s, colors.white), Element(i+s, colors.white)))
    
    for i in range(0, len(t)):
        t[i].print()
    

# exo4()


def exo5():
    colors = Color()
    p = int(input("Donnez p <= 100: "))
    t = []
    colorselection = random.sample(colors.colors, 2)
    for i in range(1, p):
        for s in range(i, p):
            if i+s <= p:
                t.append(Triplet(Element(i, random.choice(colorselection)), Element(s, random.choice(colorselection)), Element(i+s, random.choice(colorselection))))

    for i in range(0, len(t)):
        t[i].print()

    returned = False
    cnt = 0
    for i in range(0, len(t)):
        if t[i].isSameColor() == False:
            cnt += 1
    if cnt == len(t):
        returned = True
    
    if returned:
        print("VRAI")
    else:
        print("FAUX")

#exo5()

def exo6():
    colors = Color()
    p = int(input("Donnez p <= 100: "))
    n = int(input("Combien de couleurs ? (n <= 6): "))
    t = []
    colorselection = random.sample(colors.colors, n)
    for i in range(1, p+1):
        t.append(Element(random.choice(colorselection), i))
    
    print(t)
    
    listedcolor = []
    for color in colorselection:
        stop = False
        cnt = 1
        while stop == False and cnt <= (p+1):
        # ICI ON A UN PROBLEME, ELEMENT N'EST PAS RECONNU DANS T.
            if Element(color, cnt) in t:
                listedcolor.append(color)
                stop = True
            else:
                cnt += 1
    
    print(listedcolor)
    if len(listedcolor) == n:
        print("Vrai")
    else:
        print("Faux")
    
exo6()
