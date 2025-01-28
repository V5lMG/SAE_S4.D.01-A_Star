

def main():
    """
    TODO
    :return:
    """
    choix = ""
    while (choix != "Q"):
        print("""
                Bienvenue sur notre application d'analyse de l'algorithme Dijkstra et A* !
                Veuillez saisir la lettre correspond à l'action que vous voulez réaliser :
                    G - Génération d'un plateau de jeu
                    I - Importation d'un plateau de jeu existant (.txt)
                    Q - Quitter l'application\n\n
              """)
        choix = input().strip()

        if choix == "G":
            # Choix de la Longueur du plateau par l'utilisateur
            print("""
                Vous venez de sélectionner la génération aléatoire d'un plateau de jeu.
                Veuillez entrer la \033[4mLongueur\033[0m du plateau de jeu (un entier est requis).
                """)
            longueur = int(input().strip())

            # Choix de la Largeur du plateau par l'utilisateur
            print("""
                Veuillez entrer la \033[4mLargeur\033[0m du plateau de jeu (un entier est requis).
                """)
            largeur = int(input().strip())

            # Choix du taux de case interdite du plateau par l'utilisateur
            print("""
                Veuillez entrer le \033[4mTaux\033[0m de case interdite du plateau de jeu (un pourcentage est requis).
                """)
            taux = int(input().strip())

            # Choix du placement des case "Départ" et "Arrivé" sur le plateau par l'utilisateur
            print("""
                Souhaitez-vous positionner la case départ "en haut à gauche" et la case arrivée "en bas à droite" ? 
                ( o = "oui, n = "non" )
                """)
            placement_D_A = input().strip()

            # TODO

            # generation_plateau(largeur, longueur, taux, placement_D_A)
        if choix == "I":
            print("""
                Vous venez de sélectionner l'importation d'un plateau de jeu 
                Veuillez saisir le chemin du votre fichier en .txt :""")
            chemin_import = input().strip()
            print(chemin_import)
            # Demande le chemin du fichier
            # Appeler la méthode d'importation
        if choix != "Q" and choix != "G" and choix != "I":
            print("""
                Vous venez de saisir un mauvais caractères, vous avez le choix entre G, I et Q.""")

main()