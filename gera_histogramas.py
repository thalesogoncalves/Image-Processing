'''
Name: Thales de Oliveira Goncalves
USP Number: 11383541
Course Code: SCC5830
Year/Semester: 2019/1
Final Project - Detecting Malaria Desease in Cell Images
'''

import os
import numpy as np
import imageio
import matplotlib.pyplot as plt
import time
from ccc import clc, clear
clc(); exec(clear())

# Generate Histogram of the Training Part
bins_num = 50
bins_range = [0, 0.2]
dx = (bins_range[1]-bins_range[0])/bins_num
path = 'G:/Thales/Documents/Acadêmico/Doutorado/Processamento de Imagem/Trabalho Final/cell_images'

classes = ['0 - Uninfected' , '1 - Parasitized']
hist = np.zeros([len(classes), bins_num])
bins_edges = np.linspace(bins_range[0], bins_range[1], bins_num+1)
bins_means = np.mean(np.stack([bins_edges[:-1], bins_edges[1:]]),0)
for i in range(len(classes)):
    N = len(os.listdir(path + '/' + classes[i]))-1
    N0, N = 0, int(0.9*N)
    for num in range(N0,N):
        if num%500 == 0: clc(); print('Classe ' + classes[i] + ': ' + str(round((num-N0)/(N-N0)*100,2)) + '%'); time.sleep(0.1)
        img_path = path + '/' + classes[i] + '/' + str(num) + '.png'
        img = np.array(imageio.imread(img_path))/255
        pos = np.where(np.sum(img,2)!=0)
        for j in range(3):
            camada = img[:,:,j]
            camada[pos] = camada[pos]-np.median(camada[pos])
        img[img>0] = 0
        img = np.sqrt(np.sum(img**2,2))
        hist[i,:] += np.histogram(img[img>0], bins=bins_num, range=bins_range)[0]

clc()
plt.figure(figsize=[14,10])
plt.plot([0,0],[0,0.01],'blue')
plt.plot([0.05,0.15],[0.05,0],'red')
plt.legend(['Uninfected', 'Parasitized'])
plt.stem(bins_means,hist[0,:], 'blue')
plt.stem(bins_means+dx/3,hist[1,:], 'red')
plt.show()
            