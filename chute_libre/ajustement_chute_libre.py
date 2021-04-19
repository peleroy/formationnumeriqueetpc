from matplotlib.pyplot import * # Pour les graphes'
from scipy.optimize import * # Pour la fonction 'curve_fit'
from scipy import * # Pour la fonction 'linspace'
from tkinter.filedialog import askopenfilename

# Importation des données
liste_x=[]
liste_y=[]

nomfich=askopenfilename(filetypes=(("Fichier CSV","*.csv"),("Tous les fichiers","*.*")),title="Choisir un fichier")

with open(nomfich,'r') as fichier: # Ou remplacer directement 'nomfich' par le nom du fichier à ouvrir et supprimer la ligne précédente
    fichier.readline()
    for ligne in fichier:
        ligne_lue=ligne.split(';')
        liste_x.append(float(ligne_lue[0].replace(',','.'))/1000) # Facteur 1000 pour la conversion en s
        liste_y.append(float(ligne_lue[1].replace(',','.'))/100) # Facteur 100 pour la conversion en m
    fichier.close()

# Ajustement des données expérimentales par une loi donnée
def f_ajust(t,A,t0,B):
    return(-1/2*A*(t-t0)**2+B)

popt,pcov=curve_fit(f_ajust,liste_x,liste_y,[10,5,0.3]) # La liste passée en paramètres correspond à des estimations des coefficients (ça aide...)

print('Équation -1/2*A*(t-t0)**2+B : A=',popt[0],'t0=',popt[1],'B=',popt[2]) # On peut utiliser round(nombre,nb_decimales) pour régler l'affichage

liste_x_ajust=linspace(liste_x[0],liste_x[-1],200) # Liste des abscisses pour le graphe de la fonction ajustée
liste_y_ajust=f_ajust(liste_x_ajust,*popt) # Calcul des ordonnées pour le graphe de la fonction ajustée

# Représentation graphique de la courbe ajustée sur les points expérimentaux, et sauvegarde de celle-ci
figure(1)
plot(liste_x,liste_y,'r+')
plot(liste_x_ajust,liste_y_ajust,'b-')
xlabel('x')
ylabel('y')
title('y=f(x)')
legend(('$y_{exp}$','$y_{ajust}$'))
savefig(nomfich[:-4]+'.png')
show()
