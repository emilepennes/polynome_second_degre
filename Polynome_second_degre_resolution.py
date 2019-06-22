# coding:utf-8
""" Le but de l'exercice est de définir un programme qui pour toute équation
aX^2 + bX + c = 0, a,b,c étant réels, nous donne les solutions réelles."""

from math import sqrt

print("Le but de cet exercice est de définir un programme qui",
      " pour toute équation aX^2 + bX + c = 0 nous donne les solutions réelles.")

def input_value(x):
    """Input float value"""
    while True:
        try:
            x = float(input("Soit "+ x +" = "))
            return x
        except ValueError:
            print(x, "doit être un nombre réel ;)  Try again...")

A = "a"
B = "b"
C = "c"
A = input_value(A)
B = input_value(B)
C = input_value(C)


if A != 0:
    print("Soit l\'équation: ", A, "*X^2 +", B, "*X +", C, "=0")
    DELTA = B**2-4*A*C
    print("le discriminant a pour valeur", DELTA, ".")

    if DELTA < 0:
        print("Il n y a pas de racine réelle à cette équation.")

    elif DELTA == 0:
        X1 = -B/(2*A)
        print("la solution de cette équation",
	      " est une racine double nommée X1 qui a pour valeur ", X1, ".")

    else:
        X1 = -B - sqrt(DELTA)/(2*A)
        X2 = -B + sqrt(DELTA)/(2*A)
        print("il y a deux racines distinctes à cette équation",
              " nommées X1 et X2 qui ont pour valeurs respectives ", X1, "et ", X2, ".")

else:
    if B != 0:
        print("Soit l\'équation:", B, "*X +", C, "=0")
        X1 = -C/B
        print("la solution de cette équation est",
              " une racine simple nommée X1 qui a pour valeur ", X1, ".")
    else:
        if C != 0:
            print("Soit l\'équation:", C, "=0")
            print("cette équation n\'a pas de solution.")
        else:
            print("Soit l\'équation: 0=0")
            print("cela fait la tête à toto !;)")
