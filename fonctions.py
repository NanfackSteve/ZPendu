import os, platform, random, pickle

def cleanScreen():
    """Fonction chargée d'effacer le terminal"""
    if platform.system() == "Windows":
        os.system("cls")
    elif platform.system() == "Linux":
        os.system("clear")

def loadDatas():
    """Fonction qui charge les donnees du fichier de donnees"""
    with open("donnees", "rb") as file:
        myDepickler = pickle.Unpickler(file)
        return myDepickler.load()

def saveDatas(players):
    """Fonction qui enregistre les donnees du fichier de donnees"""
    with open("donnees", "wb") as file:
        myPickler = pickle.Pickler(file)
        myPickler.dump(players)

def selectWord():
    """ Cette fonction choisi aleatoirement un mot dans le fichier word.txt"""

    keyWord, i = str(), 0
    with open("word.txt", 'r') as file:
        while(i <= random.randrange(100)):
            keyWord = file.readline()
            i+=1
    keyWord = list(keyWord)    #conversion str -> list
    keyWord.pop(7) #On supprime le caractere \n lu en fin de mot
    return "".join(keyWord) #conversion list -> str

def replay():
    """ Cette fonction test si on rejoue ou pas """

    answer = input("\n\t    Rejouer ? (O)ui / (N)on: ")
    while(answer.isalpha() is False ):
            print('Atention!! Entrez une lettre et pas un chiffre/symbole.\n')
            letter=input('Rejouer ? (O)ui / (N)on: ')
    
    if answer.upper() =='O' or answer.upper() =="OUI":
        cleanScreen()
        return True

def play(keyWord):
    """ Fonction qui execute le jeu"""

    i, trying = 0, 10
    wordFound=['*','*','*','*','*','*','*']
    print("\nVoici le mot à trouver: ", " ".join(wordFound))

    while(0 < trying):
        letter=input('\nSaisissez une lettre: ')    
        while(letter.isalpha() is False ):
            print('Atention!! Entrez une lettre et pas un chiffre/symbole.\n')
            letter=input('Saisissez une lettre: ')
    
        try:
            assert letter.upper() in keyWord #on test si la lettre fait partir du mot
            for i, letterKeyWord in enumerate(keyWord):
                if letterKeyWord == letter.upper():
                    wordFound[i] = letterKeyWord
            print(" ".join(wordFound))

            if ("".join(wordFound)).__eq__(keyWord) : #on test si on trouve le mot
                print("\nFélications !! le mot caché était {} B-)\nVotre Score = {}".format(keyWord, trying) )
                return trying

        except AssertionError :
            trying-=1
            print("Essaies restant: ",trying)
            print(" ".join(wordFound))
    
    print("""\n\t    Desole vos essaies sont finis :-( """)
    return trying

def newGame():
    """ Fonction Qui permet de lancer un Nouveau Jeu"""

    myScore=0
    cleanScreen()
    
    name= input("\nOk! Commencer par Entrer votre nom: ")
    name = name.upper()
    wordChoosed = str()
    
    #Chargement des donnees
    players = loadDatas()
    
    try:
        assert name in players.keys() #on test si le profil existe deja
        answer = input("\n\nAttention !!! Vous avez déja une partie enregistrée.\nVotre Profil sera ecrasé. Continuer ? (O)ui/(N)on: ")
        
        while(answer.isalpha() is False ):
            print('Atention!! Entrez une lettre et pas un chiffre/symbole.\n')
            answer=input('Continuer ? (O)ui / (N)on: ')
    
        if answer.upper() =='N' or answer.upper() =="NON":
            return 0
    except AssertionError:
        print("""
        Heureux de vous compter parmi nos joueurs {}.
        Essayer de deviner le mot caché derriere les *""".format(name.upper()))
       
    #Deroulement de la partie
    while(1):
        alea = selectWord()
        if alea == wordChoosed:
            continue
        wordChoosed = alea
        
        myScore = play(wordChoosed)
        if replay(): continue
        break
    
    #Enregistrement des donnees
    players[name]=myScore
    saveDatas(players)

def continueGame():
    """ Fonction qui permet de continuer une partie Sauvegardée"""

    cleanScreen()
    name = input("\nEntrez votre nom: ")
    name = name.upper()
    wordChoosed = str("")
    players = loadDatas()
    
    try:
        assert name in players.keys() #on test si le profil existe
        print("\nBon retour parmi nous {} !!.\n\nVous avez realisé un score de {} dans votre dernière partie\nEssayez de faire mieux :-p".format(name, players[name]))
        while(1):
            alea = selectWord()
            if alea == wordChoosed: #Ce test verifie que le mot varie à chaque nouvelle partie 
                continue
            wordChoosed = alea

            myScore = play(wordChoosed)
            if replay(): continue
            break
        players[name]=myScore
        saveDatas(players)

    except AssertionError:
        print("\nERROR !!! Désolé vous n'avez débuté aucune partie")
        input("\nAPPUYEZ SUR LA TOUCHE \"ENTREE\"....")    
    
def printScores():
    """ Fonction qui affiche les Scores """

    cleanScreen()
    print("""
             +----------------------------+
             |  SCORES ENREGISTRES /10    |
             +----------------------------+
        """)
    players = loadDatas()
    for score, joueur in sorted([(valeur, cle) for cle, valeur in players.items()], reverse=True):
        print("""----> {} \t= {}""".format( joueur, score ))
    input("\nAPPUYEZ SUR LA TOUCHE \"ENTREE\"....")
