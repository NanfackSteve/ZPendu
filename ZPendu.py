#! /usr/bin/python3
#-*-coding: utf-8-*

#----- IMPORTATIONS -----------
import fonctions

#-----    DEBUT ---------------

while(1):

  fonctions.cleanScreen()  
  print("""
         +---------------------------------------------+
         |  BIENVENUE DANS 'ZPENDU' version PYTHON3    |
         +---------------------------------------------+
      """)

  print("""
         Le Jeu consiste à trouver un mot qui est caché 
         derrière des <<*>>. Utilise les lettres de ton
         clavier pour essayer de trouver ce mot.\n\n""")

  print(" 1- Nouvelle Partie\n 2- Continuer Partie\n 3- Voir les scores\n 4- Quitter\n")
  choix = input("Votre Choix = ")

  while(choix.isnumeric() is False or int(choix) < 1 or int(choix) > 4  ):
    print("\nSaisissez un nombre compris entre 1 et 4.")
    choix = input("Votre Choix = ")

  choix=int(choix)

  if choix == 1:
    fonctions.newGame()
    #break
  elif choix == 2:
    fonctions.continueGame()

  elif choix == 3:
    fonctions.printScores()

  elif choix == 4:
    exit("\nJ'espere que vous vous etes bien amuse !! ;-)\n")
  else:
    print()
