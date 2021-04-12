import matplotlib.pyplot as plt
from matplotlib import animation
import serial


# Caractéristiques de l'acquisition
duree=10000 # (en ms)
dmax=200 # Distance maximale à afficher (cm)

# Représentation graphique
fig=plt.figure(1)
plt.xlabel('t (ms)')
plt.ylabel('d (cm)')

plt.xlim(0,duree)
plt.ylim(0,dmax)

line,=plt.plot([],[],'r-')

# Ouverture du port de communication
#ser=serial.Serial('COM3',9600)
ser=serial.Serial('/dev/ttyACM1',9600)

# Pour provoquer une réinitialisation au cas où le port n'est pas fermé (vidage du buffer)
ser.close()
ser.open()

# Acquisition
liste_d=[]
liste_t=[]

def mesure():
    global tmp0 # On doit préciser que ces variables sont globales (cf. partie réinitialisation du graphe)
    global liste_d
    global liste_t
    
    try:
        s=ser.readline().decode('utf8').split(' ')
        d=int(s[0])
        t=int(s[1])
        
        print(t,d)
        
        liste_d.append(d)
        liste_t.append(t)
        
        if t>duree: # Réinitialisation du graphe
            liste_d=[d]
            liste_t=[0]
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
