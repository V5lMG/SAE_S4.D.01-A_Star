# Classe permettant de comparer Dijkstra et A* à l'aide d'un graphique,
# en abscisse le taux de cause interdite, en ordonnée le nombre de case visité

import matplotlib.pyplot as plt
import parcours
import time

def comparaison(choix):
    # Données d'exemple
    taux_cases_interdites = range(30)  # Tableau du taux de cases interdites
    cases_visitees_Dijkstra =     []   # Tableau des cases visitées par Dijkstra
    moy_cases_visitees_Dijkstra = []   # Tableau des moyennes des cases visitées par Dijkstra
    cases_visitees_a_star =       []   # Tableau des cases visitées par A_star
    moy_cases_visitees_a_star =   []   # Tableau des moyennes des cases visitées par A_star
    temps_dijkstra = [] # Stocke les temps d'exécution
    temps_a_star   = [] # Stocke les temps d'exécution
    moy_temps_dijkstra = []
    moy_temps_a_star   = []

    for i in range(len(taux_cases_interdites)):

        # Réinitialisation des tableaux
        cases_visitees_dijkstra = []
        cases_visitees_a_star = []

        for j in range(50):
            # Génère un plateau identique pour les 2 algorithmes
            plateau = generation_plateau(50, 125, taux_cases_interdites[i]/100, True)

            # Récupérer les chemins à l'aide de dijkstra
            start = time.time()
            chemin, explorees = dijkstra(plateau)
            end = time.time()
            ecart = end - start

            # Affichage de tous les plateaux
            plateau_avec_chemin, nbr_cases_visitees = affichage_chemin(plateau, chemin, explorees, choix)

            cases_visitees_Dijkstra.append(nbr_cases_visitees)
            temps_dijkstra.append(ecart)

            # Récupérer les chemins à l'aide de a_star
            start = time.time()
            chemin, explorees = parcours.a_star(plateau)
            end = time.time()
            ecart = end - start

            # Affichage de tous les plateaux
            plateau_avec_chemin, nbr_cases_visitees = parcours.affichage_chemin(plateau, chemin, explorees, choix)

            cases_visitees_a_star.append(nbr_cases_visitees)
            temps_a_star.append(ecart)

        moyenne = sum(cases_visitees_Dijkstra) / len(cases_visitees_Dijkstra)
        moy_cases_visitees_Dijkstra.append(moyenne)

        moyenne = sum(temps_dijkstra) / len(temps_dijkstra)
        moy_temps_a_star.append(moyenne)

        moyenne = sum(cases_visitees_a_star) / len(cases_visitees_a_star)
        moy_cases_visitees_a_star.append(moyenne)

        moyenne = sum(temps_a_star) / len(temps_a_star)
        moy_temps_a_star.append(moyenne)

    plt.plot(taux_cases_interdites, moy_cases_visitees_Dijkstra)
    plt.plot(taux_cases_interdites, moy_cases_visitees_a_star)
    plt.ylabel('Nombre de case visitées pour relier D à A \n'
               'Moyenne obtenue sur 50 plateaux')
    plt.xlabel('Taux de cases interdites(en %)')
    plt.title("Comparaison A* et Dijkstra en fonction du taux de cases interdites \n"
              "Plateaux de dimensions fixes (largeur=50, longueur=125)")

    plt.plot(taux_cases_interdites, moy_temps_dijkstra)
    plt.plot(taux_cases_interdites, moy_temps_a_star)
    plt.ylabel('Nombre de case visitées pour relier D à A \n'
               'Moyenne obtenue sur 50 plateaux')
    plt.xlabel('Taux de cases interdites(en %)')
    plt.title("Comparaison A* et Dijkstra en fonction du taux de cases interdites \n"
              "Plateaux de dimensions fixes (largeur=50, longueur=125)")
    plt.show()


comparaison("C")