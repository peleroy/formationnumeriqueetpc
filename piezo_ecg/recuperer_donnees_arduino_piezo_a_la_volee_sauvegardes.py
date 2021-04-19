import matplotlib.pyplot as plt
from matplotlib import animation
import serial


# Caractéristiques de l'acquisition
duree=5000 # (en ms)
Amax=100 # Amplitude maximale à afficher

# Représentation graphique
fig=plt.figure(1)
plt.xlabel('t (ms)')
plt.ylabel('A (u.s.i)')
plt.xlim(0,duree)
plt.ylim(0,Amax)

line,=plt.plot([],[],'r-')

# Ouverture du port de communication
#ser=serial.Serial('COM3',9600)
ser=serial.Serial('/dev/ttyACM0',9600)

# Pour provoquer une réinitialisation au cas où le port n'est pas fermé (vidage du buffer)
ser.flushInput()

# Initialisation des listes
liste_A=[]
liste_t=[]
t0=0

def mesure():
    global liste_A # On doit préciser que ces variables sont globales (cf. partie réinitialisation du graphe)
    global liste_t
    global t0
    
    try:
        ser.open()
    except:
        pass
    
    try:
        s=ser.readline().decode('utf8').split(' ')
        A=int(s[0])
        t=int(s[1])
        liste_A.append(A)
        liste_t.append(t-t0)
        
        if t-t0>duree: # Fin du processus
            # Sauvegarde des données au préalable
            fichier=open(nomfichier+'.csv','w')
            
            fichier.write('t (ms)'+';'+'A (u.s.i)'+'\n') # Ecriture de la première ligne
            for i in range(len(liste_t)):
                fichier.write(str(liste_t[i]).replace('.',',')+';'+str(liste_A[i]).replace('.',',')+'\n')
            
            fichier.close() # Fermeture du fichier de sauvegarde des données
            
            # Fin du processus
            anim.event_source.stop()
    except:
        pass
    
    return(liste_t,liste_A)

def animate(i):
    line.set_data(mesure())
    return(line,)

anim=animation.FuncAnimation(fig,animate,frames=1,interval=0,blit=True)
plt.show()

# Fermeture du port de communication
ser.close()
