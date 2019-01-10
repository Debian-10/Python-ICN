import math
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
t = j / ev
r = t * 10 ** 9, 2
print("Le résultat est:",round(t * 10 ** 9, 2), "eV")
lvl_energie = []
print("Rentrez quatre valeurs en eV et dans l'ordre croissant")
for i in range(0, 4):
    while True:
        # variable pour vérifier la saisie du nombre de saisie voulues
        try:
            a = input("Entrer la valeur ")
            a = float(a)
            print(a)
            if a > 0:
                print("Erreur, valeur supérieure à zéro.", end=" ")
                continue
            else:
                lvl_energie.append(a)
                break
        except ValueError:
            print("Valeur saisie non valide. Recommencez")
            continue
print(lvl_energie)
for x in range (1,4):
    for i in range (0je ,4):
        if r == lvl_energie[x]-lvl_energie[i]:
            print("La valeur correspond à la déséxitation entre le niveau d'energie 3 et",i)
            break
        else:
            continue