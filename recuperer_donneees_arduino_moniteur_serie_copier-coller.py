import matplotlib.pyplot as plt

donnees=[
(0,24.80),
(1000,24.72),
(2001,24.72),
(3003,24.80),
(4003,24.72),
(5005,24.72),
(6006,25.61),
(7007,26.18),
(8008,26.51),
(9010,26.84),
(10010,27.01),
(11012,27.17),
(12013,27.17),
(13014,27.50),
(14015,27.42),
(15016,27.67),
(16018,27.75),
(17018,27.67),
(18020,27.84),
(19021,27.67),
(20022,27.92),
(21023,27.92),
(22025,27.84),
(23026,27.92),
(24027,27.84),
]

liste_t=[mesure[0] for mesure in donnees]
iste_T=[mesure[1] for mesure in donnees]

plt.figure(1)
plt.plot(liste_t,liste_T,'r+')
plt.xlabel('t (s)')
plt.ylabel('Température (°C)')
plt.title('T(t)')
plt.show()
