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
     
    for triplet in [tripletrouge, tripletrandom]:
        if triplet.isSameColor():
            print("le triplet "+triplet.printable()+" est monochromatique")
            print("Vrai")
        else:
            print("le triplet "+triplet.printable()+" est polychromatique")
            print("Faux")
            



#exo3()


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
    

#exo4()


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
        t.append(Element(i, random.choice(colorselection)))
    
    listedcolor = []
    for color in colorselection:
        for i in t:
            if color == i.color:
                listedcolor.append(color)
    
    listedcolor = list(set(listedcolor))
    
    print(listedcolor)
    if len(listedcolor) == n:
        print("Vrai")
    else:
        print("Faux")
    
#exo6()


def exo7(a):
    l = []
    while a/2 != 0 :
        l.append(int(a%2))
        a = int(a/2)
    l.reverse()
    if l == []:
        l.append(0)
    print(l)
    
#exo7(11)

def exo8(a, b):
    l = []
    while a/b != 0 :
        l.append(int(a%b))
        a = int(a/b)
    l.reverse()
    if l == []:
        l.append(0)
    print(l)
#exo8(714,2)

def exo9():
    colors = Color()
    p = int(input("Donnez p <= 100: "))
    n = int(input("Combien de couleurs ? (n <= 6): "))
    t = []
    c = []
    color = []
    colorselection = random.sample(colors.colors, n)
    for i in range(1, p+1):
        t.append(i)
    
    for color1 in colorselection:
        for color2 in colorselection:
            for color3 in colorselection:
                for color4 in colorselection:
                    for color5 in colorselection:
                        for color6 in colorselection:
                            c.append([color1, color2, color3, color4, color5, color6])
    
    for i in range(0, len(c)):
        c[i].reverse()
    
    
    for i in range(0, n**p):
        color.append(c[i])
    
    
    for i in range(0, n**p):
        color[i] = color[i][:n+1]
    
    for iteration in range(0, len(color)):
        for s in range(1, p+1):
            print(color[iteration][s-1] + str(t[s-1]), end='')
        print("\n", end='')
        
            
exo9()


def exo10():
    colors = Color()
    p = int(input("Donnez p <= 100: "))
    n = int(input("Combien de couleurs ? (n <= 6): "))
    t = []
    colorselection = random.sample(colors.colors, n)
    for i in range(1, p):
        for s in range(i, p):
            for color1 in colorselection:
                for color2 in colorselection:
                    for color3 in colorselection:

                         if i+s <= p:
                            triple = Triplet(Element(i, color1), Element(s, color2), Element(i+s, color3))
                            t.append(triple)
                            triple.print()
#exo10()
