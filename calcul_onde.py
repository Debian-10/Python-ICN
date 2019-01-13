import math
from typing import Any, Union

def calconde():
    while True:
        # variable pour vérifier la saisie du nombre de saisie voulues
        l = input("Quelle est la longueur d'onde à convertir en EléctronVolt ? ")
        try:
            l = int(l)
            if l < 0:
                print("Erreur, valeur inférieure à zéro.", end=" ")
                continue
            else:
                break
        except ValueError:
            print("Valeur saisie non valide. Recommencez")
            continue
    c = 3 * 10 ** 8
    a = l * 10 ** -9
    v = c / l
    h = 6.63 * 10 ** -34
    j = v * h
    ev = 1.6 * 10 ** -19
    t = j/ev
    r =round(t*10**9, 2)
    print("Le résultat est:",r,"eV")

calconde()

input("Appuyez sur ENTREE pour continuer")