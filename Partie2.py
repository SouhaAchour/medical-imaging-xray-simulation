import numpy as np
import matplotlib.pyplot as plt

datas = np.load('data_ct.npz')  # Adresse des données
data = datas['arr_0']

I0 = 5

# Définir les Points de Départ et d'Arrivée : Choisir les coordonnées du voxel de départ (source de rayons X) et du voxel d'arrivée (détecteur).
source = [-0,512/2 , 1017/2]
points_detecteur = []

for zplanfinal in range(1017):
    for yplanfinal in range(512):

        detecteur = [512, yplanfinal, zplanfinal]
        points_detecteur.append(detecteur)
Vect_ray = []
for j in range(len(points_detecteur)):
   vecteur = np.array(points_detecteur[j])-np.array(source)
   Vect_ray.append(vecteur)

# Calculer la magnitude maximale
for j in range(len(Vect_ray)):
    amax = Vect_ray[j][0]
    if(amax<abs(Vect_ray[j][1])):
        amax= Vect_ray[j][1]
    elif(amax<abs(Vect_ray[j][1])):
        amax = Vect_ray[j][2]

listvoxeles = []
Isum_list = []

for j in range(len(Vect_ray)):
    Ii = 0
    for i in range(int(amax)):
        Vx = source[0] + i * (Vect_ray[j][0]/amax)
        Vy = source[1] + i * (Vect_ray[j][1]/amax)
        Vz = source[2] + i * (Vect_ray[j][2]/amax)

        # Assurer que les indices sont dans la plage valide
        if 0 <= Vx < 512 and 0 <= Vy < 512 and 0 <= Vz < 1017:
            nu = data[int(Vx), int(Vy), int(Vz)]
            Ii += I0 * (np.exp((-nu) * 0.1))

    Isum_list.append(Ii)

    if j % (int(len(Vect_ray)/200)) == 0:
        print(int((100*j)/len(Vect_ray)), '%')

plt.imshow(np.array(Isum_list).reshape(1017, 512), cmap='viridis')  # Reshape pour une représentation matricielle
plt.show()
