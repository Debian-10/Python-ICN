from math import *
import os
import time
c = 1
liste = []
print("""
              _  __ _           _                        _            _      
__   _____ _ __(_)/ _(_) ___ __ _| |_ ___ _   _ _ __    __| | ___      | | ___ 
\ \ / / _ \ '__| | |_| |/ __/ _` | __/ _ \ | | | '__|  / _` |/ _ \  / _` |/ _ |
 \ V /  __/ |  | |  _| | (_| (_| | ||  __/ |_| | |    | (_| |  __/ | (_| |  __/
  \_/ \___|_|  |_|_| |_|\___\__,_|\__\___|\__,_|_|     \__,_|\___|  \__,_|\___|                                                                                                                    
""")
while True:
    # variable pour vérifier la saisie du nombre de saisie voulues
    r = input("Avec combien de lancers voulez-vous vérifier le dé ? (minimum 36) ")
    try:
        r = int(r)
        if r < 36:
            print("Le nombre de lancers est inférieur au minimum requis.", end=" ")
            continue
        else:
            break
    except ValueError:
        print("Valeur saisie non valide. Recommencez")
        continue
print("entrer le numéro du dé")
while r >= len(liste):
    # boucle pour rentrer les numéros dans une liste
    if r > len(liste):
        while True:
            try:
                print('n°', c, end=" ")
                a = input()
                a = int(a)
                if 6 >= a and a > 0:
                    c = c + 1
                    liste.append(a)
                    break
                else:
                    print('Donnez une valeur entre 1 et 6')
                    continue
            except ValueError:
                print('Donnez une valeur entre 1 et 6')
                continue
    else:
        break   
# Calculs statistiques
n=[0,0,0,0,0,0,0]
for i in range (1,7):
    n[i] = round(liste.count(i)/r,4)
print("Ok ,données prises en compte")
time.sleep(1)
print("Calcul et vérification en cours")
print('')
stat1 = round((1/6)-(1/sqrt(r)),4)
stat2 = round((1/6)+(1/sqrt(r)),4)
print('Intervalle de fluctuation:', '[', stat1, ',', stat2,']')
for i in range (1,7):
    if not (not (stat1 <= n[i]) or not (stat2 >= n[i])):
        print("La face", i, "a une fréquence ", n[i], "normale")
    else:
        if n[i] < stat1:
            print("La face", i, "a une fréquence", n[i], "inférieure à la normale")
        else:
            print("La face", i, "a une fréquence", n[i], "supérieure à la normale")
time.sleep(60)