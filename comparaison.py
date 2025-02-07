# Classe permettant de comparer Dijkstra et A* à l'aide d'un graphique,
# en abscisse le taux de cause interdite, en ordonnée le nombre de case visité

import matplotlib.pyplot as plt
import generation
import parcours

# Données d'exemple
taux_cases_interdites = range(30)  # Tableau du taux de cases interdites
cases_visitees_Dijkstra =     []   # Tableau des cases visitées par Dijkstra
moy_cases_visitees_Dijkstra = []   # Tableau des moyennes des cases visitées par Dijkstra
cases_visitees_A_star =       []   # Tableau des cases visitées par A_star
moy_cases_visitees_A_star =   []   # Tableau des moyennes des cases visitées par A_star

for i in range(len(taux_cases_interdites)):

    # Réinitialisation des tableaux
    cases_visitees_dijkstra = []
    cases_visitees_A_star = []

    for j in range(50):
        # Génère un plateau identique pour les 2 algorithmes
        plateau = generation.generation_plateau(50, 125, taux_cases_interdites[i]/100, True)

        # Lancement de l'algorithme de Dijkstra
        nbr_cases_visitees = parcours.dijkstra(plateau)
        cases_visitees_Dijkstra.append(nbr_cases_visitees)

        # Lancement de l'algorithme de Dijkstra
        #nbr_cases_visitees = parcours.a_star(plateau)
        #cases_visitees_A_star.append(nbr_cases_visitees)

    moyenne = sum(cases_visitees_Dijkstra) / len(cases_visitees_Dijkstra)
    moy_cases_visitees_Dijkstra.append(moyenne)

    # moyenne = sum(cases_visitees_A_star) / len(cases_visitees_A_star)
    # moy_cases_visitees_A_star.append(moyenne)

plt.plot(taux_cases_interdites,moy_cases_visitees_Dijkstra)
#plt.plot(taux_cases_interdites,moy_cases_visitees_A_star)
plt.ylabel('Nombre de case visitées pour relier D à A \n'
           'Moyenne obtenue sur 50 plateaux')
plt.xlabel('Taux de cases interdites(en %)')
plt.title("Comparaison A* et Dijkstra en fonction du taux de cases interdites \n"
          "Plateaux de dimensions fixes (largeur=50, longueur=125)")
plt.show()