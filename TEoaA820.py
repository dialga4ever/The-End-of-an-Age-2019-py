#Créé par Thibault Delgrande, Robin Riss et Nathan Lambert-Hintzy
from tkinter import *
from random import *
import math,random


PosX = 230
PosY = 760
longueur = 820
largeur = 480
rayon = 24
score=0
vitesse1 = random.uniform(1.8,2)*3
angle1 = random.uniform(0,2*math.pi)
DX1 = vitesse1*math.cos(angle1)
DY1 = vitesse1*math.sin(angle1)
X1 = largeur/2
Y1 = 0
vitesse2 = random.uniform(1.8,2)*3
angle2 = random.uniform(0,2*math.pi)
DX2 = vitesse2*math.cos(angle2)
DY2 = vitesse2*math.sin(angle2)
X2 = largeur/2
Y2 = 0
vitesse3 = random.uniform(1.8,2)*3
angle3 = random.uniform(0,2*math.pi)
DX3 = vitesse3*math.cos(angle3)
DY3 = vitesse3*math.sin(angle3)
X3 = largeur/2
Y3 = 0
vitesse4 = random.uniform(1.8,2)*3
angle4 = random.uniform(0,2*math.pi)
DX4 = vitesse4*math.cos(angle4)
DY4 = vitesse4*math.sin(angle4)
X4 = largeur/2
Y4 = 0
vitesse5 = random.uniform(1.8,2)*3
angle5 = random.uniform(0,2*math.pi)
DX5 = vitesse5*math.cos(angle5)
DY5 = vitesse5*math.sin(angle5)
X5 = largeur/2
Y5 = 0


def Clic(event):
    X = event.x
    Y = event.y
    if 205<=X<=275 and 304<=Y<=336:
        Canevas.delete(bouton_jouer)
        Canevas.delete(bouton_quitter)
        play()
    if 205<=X<=275 and 624<=Y<=656:
        fenetre.destroy()

def deplacement(event):
    global PosX
    touche = event.keysym
    if touche == "Right" and PosX<=largeur-25:
        PosX = PosX+10
    if touche == "Left" and PosX>=25:
        PosX = PosX-10
    Canevas.coords(dino,PosX,PosY)

def play():
    m1()
    m2()
    m3()
    m4()
    m5()

def m1():
    global X1,Y1,DX1,DY1,score
    if X1+rayon+DX1 > largeur:
        X1 = 2*(largeur-rayon)-X1
        DX1 = -DX1
    if X1-rayon+DX1 < 0:
        X1 = 2*rayon-X1
        DX1 = -DX1
    if Y1+rayon+DY1 > longueur:
        Y1 = 2*(longueur-rayon)-Y1
        DY1 = -DY1
        score=score+1
    if Y1-rayon+DY1 < 0:
        Y1 = 2*rayon-Y1
        DY1 = -DY1
    X1 = X1+DX1
    Y1 = Y1+DY1
    Canevas.coords(meteorite1,X1-rayon,Y1-rayon,X1+rayon,Y1+rayon)
    DX1=DX1*1.0009765625
    DY1=DY1*1.0009765625
    if X1+rayon>=PosX>=X1-rayon and Y1+rayon>=PosY>=Y1-rayon:
        gameover()
    fenetre.after(25,m1)

def m2():
    global X2,Y2,DX2,DY2,score
    if X2+rayon+DX2 > largeur:
        X2 = 2*(largeur-rayon)-X2
        DX2 = -DX2
    if X2-rayon+DX2 < 0:
        X2 = 2*rayon-X2
        DX2 = -DX2
    if Y2+rayon+DY2 > longueur:
        Y2 = 2*(longueur-rayon)-Y2
        DY2 = -DY2
        score=score+1
    if Y2-rayon+DY2 < 0:
        Y2 = 2*rayon-Y2
        DY2 = -DY2
    X2 = X2+DX2
    Y2 = Y2+DY2
    Canevas.coords(meteorite2,X2-rayon,Y2-rayon,X2+rayon,Y2+rayon)
    DX2=DX2*1.0009765625
    DY2=DY2*1.0009765625
    if X2+rayon>=PosX>=X2-rayon and Y2+rayon>=PosY>=Y2-rayon:
        gameover()
    fenetre.after(25,m2)

def m3():
    global X3,Y3,DX3,DY3,score
    if X3+rayon+DX3 > largeur:
        X3 = 2*(largeur-rayon)-X3
        DX3 = -DX3
    if X3-rayon+DX3 < 0:
        X3 = 2*rayon-X3
        DX3 = -DX3
    if Y3+rayon+DY3 > longueur:
        Y3 = 2*(longueur-rayon)-Y3
        DY3 = -DY3
        score=score+1
    if Y3-rayon+DY3 < 0:
        Y3 = 2*rayon-Y3
        DY3 = -DY3
    X3 = X3+DX3
    Y3 = Y3+DY3
    Canevas.coords(meteorite3,X3-rayon,Y3-rayon,X3+rayon,Y3+rayon)
    DX3=DX3*1.0009765625
    DY3=DY3*1.0009765625
    if X3+rayon>=PosX>=X3-rayon and Y3+rayon>=PosY>=Y3-rayon:
        gameover()
    fenetre.after(25,m3)

def m4():
    global X4,Y4,DX4,DY4,score
    if X4+rayon+DX4 > largeur:
        X4 = 2*(largeur-rayon)-X4
        DX4 = -DX4
    if X4-rayon+DX4 < 0:
        X4 = 2*rayon-X4
        DX4 = -DX4
    if Y4+rayon+DY4 > longueur:
        Y4 = 2*(longueur-rayon)-Y4
        DY4 = -DY4
        score=score+1
    if Y4-rayon+DY4 < 0:
        Y4 = 2*rayon-Y4
        DY4 = -DY4
    X4 = X4+DX4
    Y4 = Y4+DY4
    Canevas.coords(meteorite4,X4-rayon,Y4-rayon,X4+rayon,Y4+rayon)
    DX4=DX4*1.0009765625
    DY4=DY4*1.0009765625
    if X4+rayon>=PosX>=X4-rayon and Y4+rayon>=PosY>=Y4-rayon:
        gameover()
    fenetre.after(25,m4)

def m5():
    global X5,Y5,DX5,DY5,score
    if X5+rayon+DX5 > largeur:
        X5 = 2*(largeur-rayon)-X5
        DX5 = -DX5
    if X5-rayon+DX5 < 0:
        X5 = 2*rayon-X5
        DX5 = -DX5
    if Y5+rayon+DY5 > longueur:
        Y5 = 2*(longueur-rayon)-Y5
        DY5 = -DY5
        score=score+1
    if Y5-rayon+DY5 < 0:
        Y5 = 2*rayon-Y5
        DY5 = -DY5
    X5 = X5+DX5
    Y5 = Y5+DY5
    Canevas.coords(meteorite5,X5-rayon,Y5-rayon,X5+rayon,Y5+rayon)
    DX5=DX5*1.0009765625
    DY5=DY5*1.0009765625
    if X5+rayon>=PosX>=X5-rayon and Y5+rayon>=PosY>=Y5-rayon:
        gameover()
    fenetre.after(25,m5)

def gameover():
    fenetre.destroy()
    gameover= Tk()
    gameover.title("Game Over")
    label1 = Label(gameover, text = "Vous avez perdu. Votre score est de " + str(score))
    label1.pack()
    quitter = Button(gameover, text = 'Quitter', command = gameover.destroy)
    quitter.pack()
    gameover.mainloop()

fenetre = Tk()
fenetre.title("The End of an Age")
Canevas = Canvas(fenetre, width = largeur, height = longueur)
fond = PhotoImage(file="background.png")
personnage = PhotoImage(file="character.png")
jouer = PhotoImage(file="bouton_jouer.png")
quitter = PhotoImage(file="bouton_quitter.png")
item = Canevas.create_image(0,0,anchor=NW, image=fond)
dino = Canevas.create_image(PosX,PosY, image=personnage)
Canevas.focus_set()
meteorite1 = Canevas.create_oval(X1-rayon,Y1-rayon,X1+rayon,Y1+rayon,width=1,fill='orange')
meteorite2 = Canevas.create_oval(X2-rayon,Y2-rayon,X2+rayon,Y2+rayon,width=1,fill='orange')
meteorite3 = Canevas.create_oval(X3-rayon,Y3-rayon,X3+rayon,Y3+rayon,width=1,fill='orange')
meteorite4 = Canevas.create_oval(X4-rayon,Y4-rayon,X4+rayon,Y4+rayon,width=1,fill='orange')
meteorite5 = Canevas.create_oval(X1-rayon,Y5-rayon,X5+rayon,Y5+rayon,width=1,fill='orange')
bouton_jouer = Canevas.create_image(240,320, image=jouer)
bouton_quitter = Canevas.create_image(240,640, image=quitter)
Canevas.bind('<Button-1>',Clic)
Canevas.bind("<Key>",deplacement)
Canevas.pack(padx =5, pady =5)

fenetre.mainloop()