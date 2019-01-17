9# -*- coding: utf-8 -*-
import random
import urllib.request
import os
import hashlib
from pathlib import Path

word_length = 4 # minimum word length
custom_path_name = 'wordlist' # path where word lists are stored

####################################
# Download and check the word list #
####################################

# Selector to choose the type of the word to guess
while True:
    print('Quel type de mot voulez-vous devinez ? (choisir par un chiffre entre 1-5)')
    print('1. Les noms')
    print('2. Les adjectifs')
    print('3. Les adverbes')
    print("4. Les verbes à l'infinitif")
    choice = input("5. L'ensemble (dictionnaire)\n> ")
    try:
        choice = int(choice)
        if choice > 5 or choice < 1:
            os.system("clear")
            print("Valeur saisie non valide.", end=" ")
            continue
        else:
            break
    except ValueError:
        os.system("clear")
        print("Valeur saisie non valide.", end=" ")
        continue

# url list and checksums of original files
if choice == 1:
    choice = 'nouns.txt'
    md5_b = 'bebdef79615cb1802e484cef6b7193e5'
if choice == 2:
    choice = 'adjectives.txt'
    md5_b = 'cc863fa29842d9e3fb36c191f572ca12'
if choice == 3:
    choice = 'adverbs.txt'
    md5_b = '06e80ad48aa32094ed7f1938759f853d'
if choice == 4:
    choice = 'infinitives.txt'
    md5_b = '6d5edf8b0e0eefe725d10cf9c79cf055'
if choice == 5:
    choice = 'dictionary.txt'
    md5_b = '72baa94546475f2e17a85b3f1134ec9c'

url = 'https://github.com/Debian-10/French-Dictionary/raw/no-genders-types-indicators/dictionary/%s' % choice
file_name = url.split('/')[-1]


def download():
    u = urllib.request.urlopen(url, file_name.encode('utf_8'))
    file_size = eval(u.info()['Content-Length'])
    file_size = int(file_size / 1000)
    print("Téléchargement de: %s Taille: %s Kb" % (file_name, file_size), "dans", my_file, '\n')
    data = u.read()
    f = open(file_name, 'wb')
    f.write(data)
    f.close()


# Check if the file already exists and his path
cwd = os.getcwd()
folder = os.path.join(cwd, custom_path_name)
try:
    os.mkdir(folder)
except OSError:
    print("Répertoire %s déjà existant !" % folder)
else:
    print("Répertoire %s créé avec succès" % folder)
my_file = Path(folder, file_name)
os.chdir(folder)
try:
    my_path = my_file.resolve(strict=True)
except FileNotFoundError:
    # Download the wordlist
    download()
else:
    print(file_name, "existe !\n")

# Checking of the checksum
# Downloaded or already existing file
hasher1 = hashlib.md5()
afile1 = open(my_file, 'rb')
buf1 = afile1.read()
a = hasher1.update(buf1)
md5_a = (str(hasher1.hexdigest()))
# Base-checksum already defined on section 'selector'

# Compare md5
if md5_a == md5_b:
    print(md5_b)
    print("Checksums OK \n")
else:
    print(md5_a)
    print(md5_b)
    print("Checksums WRONG \n")
    try:
        os.remove(my_file)
    except OSError as e:  # if failed, report it back to the user #
        print("Error: %s - %s." % (e.filename, e.strerror))
    # Re-download the file
    download()

####################
# The Game himself #
####################

# Choose random word to guess

while True:
    word = random.choice(open(file_name).read().split()).strip()
    length = len(word)
    if length > word_length:
        word = word
        print(word)
        break

print("Mot trouvé dans le dictionnaire...\nLe jeu commence !")
guess = False
while guess == False:
    while True:
        choice1 = input("Rentrez la première lettre\n> ")
        if choice1.isalpha() == True:
            if len(choice1) > 1:
                print("Trop de charactères saisis.", end=" ")
                continue
            else:
                break
        else:
            os.system("clear")
            print("Valeur saisie non valide.", end=" ")
            continue
print(choice1)
