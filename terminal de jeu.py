3# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 07:53:20 2024

@author: julie
"""

import numpy as np
import matplotlib.pyplot as plt
import random as rd
from puissance4_ import (plot,victoire,debut,joueur,niv0,niv1,niv2,niv3,niv4,niv5,niv6,niv7,)
N=9
j1=0
j2=0
for i in range (0,100):
    tab=debut(N)
    
    vic=0
    tour=0
    gagnant=0
    stop=False
    while vic==0:
        tour+=1
        tab,stop=niv0(N,tab,1)
        vic=victoire(N,tab,stop)
        if vic==1:
            gagnant=1
            break
            
        tab,stop=niv7(N,tab,2)
        vic=victoire(N,tab,stop)
        if vic==1:
            gagnant=2
            break

        
        if vic==2:
            break
            print ('égalité')
        # plot(tab,N)
        # plt.show()

    if gagnant==1:
        print('joueur1 a gagné !')
        plot(tab,N)
        plt.show()
        j1+=1
    if gagnant==2:
        print('joueur2 a gagné !')
        j2+=1
print('le score est de ',j1, 'à',j2)