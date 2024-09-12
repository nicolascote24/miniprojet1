#importation du random
import random

#boolean du programme (quand ils deviens false le programme s'arrête)
programme = True

#boucle tant que le programme ne deviens pas FALSE dans votre code
while programme == True :
    
    #affichage du menu
    print("que voulez vous faire :")
    print("(0) entrer mes informations")
    print("(1) ajouter une transactions")
    print("(2) afficher les trois dernières opérations")
    print("(3) cotisation au REER/CELI")
    print("(4) calculer mes placements")
    print("(5) solde du compte")
    
    #choix de l'utilisateur
    choix = int(input("entrez votre réponse : "))
    
    #votre code (pour les différentes options)