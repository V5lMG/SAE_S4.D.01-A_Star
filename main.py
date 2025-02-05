# import generation

def main():
    """
    Afficher le menu principal et permettre à l'utilisateur de choisir une option (Génération, Importation, Quitter).
    - Si l'utilisateur choisit "G" (Génération d'un plateau de jeu) :
        - Demander la longueur du plateau (doit être supérieure ou égal à 3).
        - Demander la largeur du plateau (doit être supérieure ou égal à 3).
        - Demander le taux de cases interdites (doit être compris entre 0 et 100).
        - Demander si l'utilisateur souhaite positionner les cases départ et arrivée automatiquement.
        - Utiliser ces informations pour générer le plateau.
    - Si l'utilisateur choisit "I" (Importation d'un plateau de jeu) :
        - Demander le chemin du fichier à importer (doit être au format .txt).
        - Valider que le fichier se termine bien par ".txt".
    - Si l'utilisateur saisit une option invalide, afficher un message d'erreur et lui redemande uneoption.
    - Quitter l'application si l'utilisateur choisit "Q".
    :return:
    """
    choix = ""
    while choix != "Q":
        print("""
                Bienvenue sur notre application d'analyse de l'algorithme Dijkstra et A* !
                Veuillez saisir la lettre correspondante à l'action que vous voulez réaliser :
                    G - Génération d'un plateau de jeu
                    I - Importation d'un plateau de jeu existant (.txt)
                    Q - Quitter l'application\n\n
              """)
        choix = input().strip().upper()

        if choix == "G":

            # Initialisation
            longueur = largeur = 0
            taux = -1
            placement_D_A = ""

            # Choix de la Longueur du plateau par l'utilisateur
            while longueur < 3 :
                print("""
                    Vous venez de sélectionner la génération aléatoire d'un plateau de jeu.
                    Veuillez entrer la \033[4mLongueur\033[0m du plateau de jeu (un entier est requis supérieur à 2).
                    """)
                longueur = int(input().strip())
                if longueur < 3 :
                    print("Veuillez sélectionner une réponse correcte\n")

            # Choix de la Largeur du plateau par l'utilisateur
            while largeur < 3 :
                print("""
                    Veuillez entrer la \033[4mLargeur\033[0m du plateau de jeu (un entier est requis supérieur à 2).
                    """)
                largeur = int(input().strip())
                if largeur < 3 :
                    print("Veuillez sélectionner une réponse correcte\n")

            # Choix du taux de case interdite du plateau par l'utilisateur
            while 0 > taux > 100 :
                print("""
                    Veuillez entrer le \033[4mTaux\033[0m de case interdite du plateau de jeu (compris entre 0 et 100).
                    """)
                taux = int(input().strip())
                if 0 > taux > 100 :
                    print("Veuillez sélectionner une réponse correcte\n")

            while placement_D_A != "N" and placement_D_A != "O":
                # Choix du placement des case "Départ" et "Arrivé" sur le plateau par l'utilisateur
                print("""
                Souhaitez-vous positionner la case départ "en haut à gauche" et la case arrivée "en bas à droite" ? 
                ( O = "Oui, N = "Non" )
                      """)
                placement_D_A = input().strip().upper()

                if placement_D_A != "N" and placement_D_A != "O":
                    print("Veuillez sélectionner une réponse correcte\n")

            if placement_D_A == "O":
                placement_D_A = False
            if placement_D_A == "N":
                placement_D_A = True

            taux = taux / 100
            # generation.generation_plateau(largeur, longueur, taux, placement_D_A)
        if choix == "I":
            print("""
                Vous venez de sélectionner l'importation d'un plateau de jeu 
                Veuillez saisir le chemin de votre fichier en .txt :""")
            chemin_import = input().strip()

            # Tant que le chemin ne termine pas par ".txt"
            while not chemin_import.endswith(".txt"):
                print("Erreur : le fichier doit être au format .txt.")
                print("Veuillez saisir un chemin valide :")
                chemin_import = input().strip()

             # Appeler la méthode d'importation
        if choix != "Q" and choix != "G" and choix != "I":
            print("""
                Vous venez de saisir un mauvais caractères, vous avez le choix entre G, I et Q.""")

main()