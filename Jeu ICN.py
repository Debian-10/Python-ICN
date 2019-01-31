# -*- coding: utf-8 -*-
import random
import urllib.request
import os
import hashlib
import unicodedata
from pathlib import Path

#question = 1
word_length = 4 # minimum word length
custom_path_name = 'wordlist' # path where word lists are stored
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
    if md5_a != md5_b:
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
            if false < max_false :
                print("Lettre non trouvée !")
                false += 1
            else:
                print("")
        if "*" not in hidden:
            print("Et le mot est : \n")
            print(*hidden, sep=" ")
            print("Vous avez gagné en", c, "tentatives ! \n")
            guess = True
        if max_false == false:
            print(hangman[false])
            print("Perdu ! le mot à deviner était :",word)
            #question = 1
            guess = True
            #question = 1

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