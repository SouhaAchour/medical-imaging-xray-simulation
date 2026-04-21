import numpy as np
import matplotlib.pyplot as plt 
import math
datas = np.load('data_ct.npz')#adresse des données
datas.files
data = datas['arr_0']
print(data)
nu = 0
print(data.size)
print(type(data))
print(data.shape)
I0=5


listIf = []
Ifinalforeachrayon = 0
for zplanfinal in range(1017):
    for yplanfinal in range(512):


        Ifinalforeachrayon = 0
        for xpourchaquerayon in range(512):
            
            nu = data[xpourchaquerayon,yplanfinal, zplanfinal]
            #print(nu)
            IX= I0*(np.exp((-nu)*0.1))
            print(IX)
            Ifinalforeachrayon += IX
            
        listIf.append(Ifinalforeachrayon)
        # À intervalles réguliers, le pourcentage d'avancement est affiché pour surveiller le progrès.
        if( zplanfinal%(int(1017/200))) == 0:

            print(int(100*zplanfinal/1017), '%')
        
print(listIf.shape)
listIf = np.array(listIf)
print("listIf",listIf)
plane_shape = (1017, 512)  # Define the shape of 2D plane
#les données sont remodelées sous forme d'une image 2D
listIf_2d = np.reshape(listIf, plane_shape)

sh=listIf.shape
print(sh)
print("listIf_2d",listIf_2d)

plt.imshow(listIf_2d, cmap='viridis')  
plt.colorbar() 
plt.show()


            
        