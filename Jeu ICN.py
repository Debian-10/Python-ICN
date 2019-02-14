# -*- coding: utf-8 -*-
import random
import urllib.request
import os
import hashlib
import unicodedata
from pathlib import Path
from stat import S_IREAD, S_IRGRP, S_IROTH, S_IWUSR

#question = 1
word_length = 4 # minimum word length
custom_path_name = 'game_data' # path where word lists are stored
points_score_letter = 7
points_score_false = 3

def checksum(file_checksum, md5):
    hasher1 = hashlib.md5()
    afile1 = open(file_checksum, 'rb')
    buf1 = afile1.read()
    a = hasher1.update(buf1)
    md5_a = (str(hasher1.hexdigest()))
    # Base-checksum already defined on section 'selector'

    # Compare md5
    if md5_a != md5:
        print(md5_a)
        print(md5)
        print("Checksums WRONG \n")
        try:
            os.remove(file_checksum)
        except OSError as e:  # if failed, report it back to the user #
            print("Error: %s - %s." % (e.filename, e.strerror))
            download()

def jeu():
    question = 0

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
                print("Valeur saisie non valide.", end=" ")
                continue
            else:
                break
        except ValueError:
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
        print("")
    else:
        print("")
    my_file = Path(folder, file_name)
    os.chdir(folder)
    try:
        my_path = my_file.resolve(strict=True)
    except FileNotFoundError:
        # Download the wordlist
        download()
    else:
        print("")

    #########################################
    # Ask player's name and check his score #
    #########################################

    os.chdir(folder)
    save_name = input('Entrez votre nom. ').title()


    # Checking of the checksum
    # Downloaded or already existing file
    checksum(my_file, md5_b)

    ####################
    # The Game himself #
    ####################

    def strip_accents(text):

        try:
            text = unicode(text, 'utf-8')
        except NameError:  # unicode is a default on python 3
            pass

        text = unicodedata.normalize('NFD', text) \
            .encode('ascii', 'ignore') \
            .decode("utf-8")

        return str(text)

    # Choose random word to guess
    c = 0
    c1 = 1
    noprint = 0
    existe = 0
    false = 0
    while True:
        word = random.choice(open(file_name).read().split()).strip()
        if len(word) > word_length:
            word = word
            length = len(word)
            break
    word = list(strip_accents(word))
    if "-" in word:
        word.remove("-")
    print(word)
    hangman = (
    """
        
        
        
        
        
        
        ___                 
        """,

    """
    
        |        
        |              
        |                
        |                 
        |               
        |                   
        |___                 
        """,

    """
        _________
        |/        
        |              
        |                
        |                 
        |               
        |                   
        |___                 
        """,

    """
        _________
        |/   |      
        |              
        |                
        |                 
        |               
        |                   
        |___                 
        """,

    """
        _________       
        |/   |              
        |   (_)
        |                         
        |                       
        |                         
        |                          
        |___                       
    """,

    """
        ________               
        |/   |                   
        |   (_)                  
        |    |                     
        |    |                    
        |                           
        |                            
        |___                    
        """,

    """
        _________             
        |/   |               
        |   (_)                   
        |   /|                     
        |    |                    
        |                        
        |                          
        |___                          
        """,


    """
        _________              
        |/   |                     
        |   (_)                     
        |   /|\                    
        |    |                       
        |                             
        |                            
        |___                          
        """,


    """
        ________                   
        |/   |                         
        |   (_)                      
        |   /|\                             
        |    |                          
        |   /                            
        |                                  
        |___                              
        """,


    """
        ________
        |/   |     
        |   (_)    
        |   /|\           
        |    |        
        |   / \        
        |                  
        |___           
        """)

    print("Mot trouvé dans le dictionnaire...Le jeu commence !\n \n")
    deja_saisie = []
    max_false = len(hangman) - 1
    guess = False
    hidden = []
    for i in range(0, length):
        hidden.append("*")
    print("Le mot à deviner est :", *hidden, sep=" ")
    while guess == False:
        while True:
            c += 1
            if c>1 and noprint==0:
                print(*hidden, sep=" ")
            print(hangman[false])
            print("Rentrez la lettre n°",c1)
            choice1 = input("\n> ")
            if choice1.isalpha() == True:
                if len(choice1) > 1:
                    print("Trop de charactères saisis.", end=" ")
                    continue
                else:
                    break
            else:
                print("Valeur saisie non valide.", end=" ")
                noprint = 1
                continue

        if choice1 in word:
            for i in range(len(word)):
                if hidden[i] == choice1.upper():
                    existe = 1
                    break
                if word[i] == choice1:
                    hidden[i] = choice1.upper()
                    existe = 0
            if existe == 1:
                print("lettre déjà saisie !")
            else:
                print("Lettre trouvée !")
                c1 += 1
            noprint=0

        if choice1 not in word:
            if false < max_false and choice1 not in deja_saisie:
                print("Lettre non trouvée !")
                deja_saisie.append(choice1)
                false += 1
            else:
                print("")

        if "*" not in hidden:
            print("Et le mot est : \n")
            print(*hidden, sep=" ")
            print("Vous avez gagné en", c, "tentatives ! \n")

            ################
            # Scores etc...#
            ################
            score_file = Path(folder, "score")
            try:
                score_path = score_file.resolve(strict=True)
            except FileNotFoundError:
                print("")
            else:
                print("")
                os.chmod("score", S_IWUSR | S_IREAD)

            total_score = c1 * points_score_letter - false * points_score_false
            save_score = total_score
            meilleur = 0

            # look for highscore
            try:
                fichier = open("score", "r")
                for line in fichier.readlines():

                    line_parts = line.split(" a un score de ")
                    if len(line_parts) > 1:
                        line_parts = line_parts[-1].split("\n")
                        score = line_parts[0]
                        # compare scores
                        if score.isdigit() and int(score) > meilleur:
                            meilleur = int(score)
            except FileNotFoundError:
                pass

            if int(save_score) > meilleur:
                fichier = open("score", "a")
                fichier.write("\n" + str(save_name) + ' a un score de ' + str(save_score) + "\n")
                fichier.close()

            print("\n")
            fichier = open("score", "r")
            tout_lire = fichier.read()
            print(tout_lire)
            fichier.close()
            guess = True
        if max_false == false:
            print(hangman[false])
            print("Perdu ! le mot à deviner était :", *word, sep=" ")
            #question = 1
            guess = True
            #question = 1
    os.chmod("score", S_IREAD)
# Ask if player wants to play again
#
#while question == 1:
#    jouer = str(input("voulez-vous jouer ? (oui / non) \n"))
#    if jouer == "oui" or jouer == "o" or jouer == "O":
#        jeu()
#    elif jouer == "non" or jouer == "n" or jouer == "N":
#        input("Appuyez sur une touche pour continuer... ")
#        question = 0
jeu()