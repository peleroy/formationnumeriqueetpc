import matplotlib.pyplot as plt
import serial


# Caractéristiques de l'acquisition
duree=10000 # (en ms)
nomfichier='recuperer_donnees_arduino_sonar_python'

# Ouverture du port de communication
#ser=serial.Serial('COM3',9600)
ser=serial.Serial('/dev/ttyACM1',9600)

# Pour provoquer une réinitialisation au cas où le port n'est pas fermé (vidage du buffer)
ser.close()
ser.open()

# Acquisition
liste_d=[]
liste_t=[]
t=0
while t<duree:
    try:
        s=ser.readline().decode('utf8').split(' ')
        d=int(s[0])
        t=int(s[1])
        liste_d.append(d)
        liste_t.append(t)
        print(d,t) # Affichage de la valeur et du temps correspondant dans la console
    except:
        t=0 # Pour éviter de sortir de la boucle si une erreur survient suite à l'affectation dans la variable 't'

# Fermeture du port de communication
ser.close()

# Sauvegarde des données dans un fichier extérieur (optionnel)
fichier=open(nomfichier+'.csv','w')
fichier.write('t(ms)'+';'+'d (cm)'+'\n') # Ecriture de la première ligne

for i in range(len(liste_d)):
    fichier.write(str(liste_t[i]).replace('.',',')+';'+str(liste_d[i]).replace('.',',')+'\n') # Ecriture dans le fichier (on remplace le séparateur décimal au passage)

fichier.close() # Fermeture du fichier de sauvegarde des données

# Représentation graphique et sauvegarde de celle-ci
plt.plot(liste_t,liste_d,'r-')
plt.xlabel('t (ms)')
plt.ylabel('d (cm)')
plt.savefig(nomfichier+'.png')
plt.show()
