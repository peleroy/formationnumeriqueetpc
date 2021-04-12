import matplotlib.pyplot as plt
from matplotlib import animation
import serial


# Caractéristiques de l'acquisition
duree=10000 # (en ms)
dmax=210 # Distance maximale à afficher (cm)
nomfichier='recuperer_donnees_arduino_sonar_a_la_volee_sauvegardes'

# Représentation graphique
fig=plt.figure(1)
plt.xlabel('t (ms)')
plt.ylabel('d (cm)')
plt.xlim(0,duree+1000)
plt.ylim(0,dmax)

line,=plt.plot([],[],'r-')

# Ouverture du port de communication
#ser=serial.Serial('COM3',9600)
ser=serial.Serial('/dev/ttyACM1',9600)

# Pour provoquer une réinitialisation au cas où le port n'est pas fermé (vidage du buffer)
ser.close()
ser.open()

# Initialisation des listes
liste_d=[]
liste_t=[]
t0=0

def mesure():
    global liste_d # On doit préciser que ces variables sont globales (cf. partie réinitialisation du graphe)
    global liste_t
    global t0
    
    try:
        ser.open()
    except:
        pass
    
    try:
        s=ser.readline().decode('utf8').split(' ')
        d=int(s[0])
        t=int(s[1])
        liste_d.append(d)
        liste_t.append(t-t0)
        
        if t-t0>duree: # Fin du processus
            # Sauvegarde des données au préalable
            fichier=open(nomfichier+'.csv','w')
            
            fichier.write('t(s)'+';'+'d (m)'+'\n') # Ecriture de la première ligne
            for i in range(len(liste_d)):
                fichier.write(str(liste_t[i]).replace('.',',')+';'+str(liste_d[i]).replace('.',',')+'\n')
            
            fichier.close() # Fermeture du fichier de sauvegarde des données
            
            # Fin du processus
            anim.event_source.stop()
    except:
        pass
    
    return(liste_t,liste_d)

def animate(i):
    line.set_data(mesure())
    return(line,)

anim=animation.FuncAnimation(fig,animate,frames=1,interval=0,blit=True)
plt.show()

# Fermeture du port de communication
ser.close()
