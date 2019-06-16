
# coding:utf-8
# Le but de l'exercice est de définir un programme qui pour toute équation aX^2 + bX + c = 0, a,b,c étant réels, nous donne les solutions réelles.

from math import *

print("Le but de cet exercice est de définir un programme qui pour toute équation aX^2 + bX + c = 0 nous donne les solutions réelles.")

while True :
    try :
        a = float(input("Soit a = "))
        break
    except ValueError :
        print(" a doit être un nombre réel ;)  Try again...")

while True :
    try :
        b = float(input("Soit b = "))
        break
    except ValueError :
        print(" b doit être un nombre réel ;) Try again...")

while True :
    try :
        c = float(input("Soit c = "))
        break
    except ValueError :
        print("c doit être un nombre réel ;)  Try again...")

if a!=0 :
    print("Soit l\'équation: ", a, "*X^2 +", b, "*X +", c, "=0")
    delta = b**2-4*a*c
    print("le discriminant a pour valeur", delta,".")

    if delta < 0 :
	    print("Il n y a pas de racine réelle à cette équation.")

    elif delta == 0:
	    X1 = -b/(2*a)
	    print("la solution de cette équation est une racine double nommée X1 qui a pour valeur ", X1,".") 

    else:
	    X1 = -b - sqrt(delta)/(2*a)
	    X2 = -b + sqrt(delta)/(2*a)
	    print("il y a deux racines distinctes à cette équation nommées X1 et X2 qui ont pour valeurs respectives ", X1, "et ", X2,".")

else :
    if b != 0 :
        print( "Soit l\'équation:", b, "*X +", c, "=0")
        X1 = -c/b
        print("la solution de cette équation est une racine simple nommée X1 qui a pour valeur ", X1,".")
    else :
        if c != 0 :
            print("Soit l\'équation:", c, "=0")
            print("cette équation n\'a pas de solution.")
        else : 
            print("Soit l\'équation: 0=0")
            print("cela fait la tête à toto !;)")
            
