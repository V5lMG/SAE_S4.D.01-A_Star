# Classe permettant de comparer Dijkstra et A* à l'aide d'un graphique,
# en abscisse le taux de cause interdite, en ordonnée le nombre de case visité

import matplotlib.pyplot as plt
from parcours import A_star
from plateau import Plateau
import time

def comparaison(choix):
    # Données d'exemple
    taux_cases_interdites = range(30)  # Tableau du taux de cases interdites
    tab_cases_visitees_Dijkstra = []   # Tableau des cases visitées par Dijkstra
    moy_cases_visitees_Dijkstra = []   # Tableau des moyennes des cases visitées par Dijkstra
    tab_cases_visitees_a_star =       []   # Tableau des cases visitées par A_star
    moy_cases_visitees_a_star =   []   # Tableau des moyennes des cases visitées par A_star
    temps_dijkstra =              []   # Stocke les temps d'exécution
    temps_a_star   =              []   # Stocke les temps d'exécution
    moy_temps_dijkstra =          []
    moy_temps_a_star   =          []

    for i in range(len(taux_cases_interdites)):

        # Réinitialisation des tableaux
        cases_visitees_dijkstra = []
        cases_visitees_a_star = []

        for j in range(50):
            # Génère un plateau identique pour les 2 algorithmes
            plateau = Plateau(50, 125, taux_cases_interdites[i]/100, True)

            # Récupérer les chemins à l'aide de dijkstra
            algo_dijkstra = A_star(plateau, use_a_star=False)
            start = time.time()
            chemin, cases_visitees_dijkstra = algo_dijkstra.executer()
            end = time.time()
            ecart = end - start

            # Récupération des informations dans des tableaux correspondants
            tab_cases_visitees_Dijkstra.append(len(cases_visitees_dijkstra))
            temps_dijkstra.append(ecart)

            # Récupérer les chemins à l'aide de A*
            algo_a_star = A_star(plateau, use_a_star=True)
            start = time.time()
            algo_a_star.executer()
            end = time.time()
            ecart = end - start

            # Récupération des informations dans des tableaux correspondans
            tab_cases_visitees_a_star.append(len(cases_visitees_a_star))
            temps_a_star.append(ecart)

        moyenne = sum(tab_cases_visitees_Dijkstra) / len(tab_cases_visitees_Dijkstra)
        moy_cases_visitees_Dijkstra.append(moyenne)

        moyenne = sum(temps_dijkstra) / len(temps_dijkstra)
        moy_temps_a_star.append(moyenne)

        moyenne = sum(tab_cases_visitees_a_star) / len(tab_cases_visitees_a_star)
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