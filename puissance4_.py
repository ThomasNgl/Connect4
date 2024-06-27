# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 11:05:08 2024

@author: julie
"""

#%% debut de la partie
import numpy as np
import matplotlib.pyplot as plt
import random as rd
def debut(N=9):
    tab=np.zeros((N,N))
    for i in range (0,N):
        tab[i][-2:]=3
        tab[0][i]=3
        tab[N-1][i]=3
    print(tab)
        
    fig,ax=plt.subplots(figsize=(N+np.sqrt(N),N+np.sqrt(N)))
    
    cax=ax.matshow(tab,cmap='Greys',vmin=0,vmax=0)
    ax.set_xticks(np.arange(tab.shape[0])-.5, minor=True)
    ax.set_yticks(np.arange(tab.shape[1])-.5, minor=True)
    ax.grid(which='minor',color='black')
    
    ax.tick_params(which='minor',size=0)
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    for i in range(0,N):
        for j in range(0,N):
            if tab[i][j]==3:
                ax.text(i,j,'+', ha='center',va='center', color='black',fontsize=120)
    plt.show()
    return(tab)
#%% Ton tour

def joueur(N,tab,j):
    stop=False
    print ('choisi une colonne en rentrant son numero ')
    x=input('n=')
    x=int(x)
    
    y=0
    if tab[x][y+1]==0:
        while tab[x][y+1]==0:
            y=y+1
            if tab[x][y+1]!=0:
                tab[x][y]=j   
    else:
        if tab[x][y]==0:
            tab[x][y]=j
    return (tab,stop)

#%% PLOT DES TABLEAU
def plot(tab,N):
    
    fig,ax=plt.subplots(figsize=(N+np.sqrt(N),N+np.sqrt(N)))
    
    cax=ax.matshow(tab,cmap='Greys',vmin=0,vmax=0)
    ax.set_xticks(np.arange(tab.shape[0])-.5, minor=True)
    ax.set_yticks(np.arange(tab.shape[1])-.5, minor=True)
    ax.grid(which='minor',color='black')
    
    ax.tick_params(which='minor',size=0)
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    for i in range(0,N):
        for j in range(0,N):
            if tab[i][j]==1:
                ax.text(i,j,'o', ha='center',va='center', color='blue',fontsize=60)
            if tab[i][j]==2:
                ax.text(i,j,'o', ha='center',va='center', color='red',fontsize=60)
            if tab[i][j]==3:
                ax.text(i,j,'+', ha='center',va='center', color='black',fontsize=120)
    
    return
#%% ordi random niv 0
import numpy as np
import matplotlib.pyplot as plt
import random as rd
def niv0(N,tab,j_):
    stop=False
    a=rd.randint(1,N-2)
    
    reste=[]
    for i in range (1,N-1):
        reste.append(i)
    y=0
    tab2=np.zeros((N,N))
    for i in range (0,N):
        tab2[i][N-1]=3
        tab2[i][N-2]=3
        tab2[0][i]=3
        tab2[N-1][i]=3
    sumtab=0
    sumtab2=0
    for (i,j), val in np.ndenumerate(tab):
        tab2[i][j]=tab[i][j]
        sumtab+=tab[i][j]
        sumtab2+=tab2[i][j]
    while sumtab==sumtab2:
        if tab[a][y+1]==0:
            while tab[a][y+1]==0:
                y=y+1
                if tab[a][y+1]!=0:
                    tab[a][y]=j_
                    sumtab+=tab[a][y]
                else:
                    if reste:
                        a=rd.choice(reste)
                        reste.remove(a)
                    else:
                        stop=True
                        break
    
        else:
            if tab[a][y]==0:
                tab[a][y]=j_
                sumtab+=tab[a][y]
            else:
                 if reste:
                     a=rd.choice(reste)
                     reste.remove(a)
                 else:
                     stop=True
                     break
        if stop:
            break
        
    

    return(tab,stop)
#%% ordi raisonnement des paires niv 1 (pas stable)
import numpy as np
import matplotlib.pyplot as plt
import random as rd
def niv1(N,tab,j_):
    
    place=[]
    for i in range (1,N-1):
        for j in range (0,N-2):
            if tab[i][j]!=0:
                if tab[i][j]==tab[i+1][j]:
                    if (i+2)<N-1:
                        place.append(i+2)
                    if (i-1)!=0:
                        place.append(i-1)
                if tab[i][j]==tab[i][j+1]:
                    place.append(i)
    
    
                
    print(place)
    if place:
        a=rd.choice(place)
    else:
        a=rd.randint(1,7)
    x=a
    y=0
    tab2=np.zeros((N,N))
    for i in range (0,N):
        tab2[i][N-1]=3
        tab2[i][N-2]=3
        tab2[0][i]=3
        tab2[N-1][i]=3
    sumtab=0
    sumtab2=0
    for (i,j), val in np.ndenumerate(tab):
        tab2[i][j]=tab[i][j]
        sumtab+=tab[i][j]
        sumtab2+=tab2[i][j]
    while sumtab==sumtab2:
        if tab[x][y+1]==0:
            while tab[x][y+1]==0:
                y=y+1
                if tab[x][y+1]!=0:
                    tab[x][y]=j_
                    sumtab+=tab[x][y]
                else:
                    x=a
    
        else:
            if tab[x][y]==0:
                tab[x][y]=j_
                sumtab+=tab[x][y]
            else:
                x=a
        
    
    
    return(tab)
#%% ordi raisonement des paires + des triples niv 2 (pas stable)
def niv2(N,tab,j_):
    
    place=[]
    for i in range (1,N-1):
        for j in range (0,N-2):
            if tab[i][j]!=0:
                if tab[i][j]==tab[i+1][j]:
                    if (i+2)<N-1:
                        place.append(i+2)
                    if (i-1)!=0:
                        place.append(i-1)
                if tab[i][j]==tab[i][j+1]:
                    place.append(i)
    
    
    triple=[]
    for i in range (1,N-1):
        for j in range (0,N-2):
            if tab[i][j]!=0:
                if tab[i][j]==tab[i+1][j]==tab[i+2][j]:
                    if (i+3)<N-1:
                        triple.append(i+3)
                    if (i-1)!=0:
                        triple.append(i-1)
                if tab[i][j]==tab[i][j+1]==tab[i][j+2]:
                    triple.append(i)
                if tab[i][j]==tab[i+1][j+1]==tab[i+2][j+2]:
                    if (i+3)<N-1:
                        triple.append(i+3)
                    if (i-1)!=0:
                        triple.append(i-1)
                if tab[i+2][j]==tab[i+1][j+1]==tab[i][j+2]:
                    if (i+3)<N-1:
                        triple.append(i+3)
                    if (i-1)!=0:
                        triple.append(i-1)
    print(triple)
    print(place)
    if triple:
        a=rd.choice(triple)
    elif place:
        a=rd.choice(place)
    else:
        a=rd.randint(3,5)
        
    x=a
    y=0
    tab2=np.zeros((N,N))
    for i in range (0,N):
        tab2[i][N-1]=3
        tab2[i][N-2]=3
        tab2[0][i]=3
        tab2[N-1][i]=3
    sumtab=0
    sumtab2=0
    for (i,j), val in np.ndenumerate(tab):
        tab2[i][j]=tab[i][j]
        sumtab+=tab[i][j]
        sumtab2+=tab2[i][j]
    while sumtab==sumtab2:
        if tab[x][y+1]==0:
            while tab[x][y+1]==0:
                y=y+1
                if tab[x][y+1]!=0:
                    tab[x][y]=j_
                    sumtab+=tab[x][y]
                else:
                    x=a
    
        else:
            if tab[x][y]==0:
                tab[x][y]=j_
                sumtab+=tab[x][y]
            else:
                x=a
        
    
    # fig,ax=plt.subplots(figsize=(N+np.sqrt(N),N+np.sqrt(N)))
    
    # cax=ax.matshow(tab,cmap='Greys',vmin=0,vmax=0)
    # ax.set_xticks(np.arange(tab.shape[0])-.5, minor=True)
    # ax.set_yticks(np.arange(tab.shape[1])-.5, minor=True)
    # ax.grid(which='minor',color='black')
    
    # ax.tick_params(which='minor',size=0)
    # ax.set_xticklabels([])
    # ax.set_yticklabels([])
    # for i in range(0,N):
    #     for j in range(0,N):
    #         if tab[i][j]==1:
    #             ax.text(i,j,'o', ha='center',va='center', color='blue',fontsize=60)
    #         if tab[i][j]==2:
    #             ax.text(i,j,'o', ha='center',va='center', color='red',fontsize=60)
    #         if tab[i][j]==3:
    #             ax.text(i,j,'+', ha='center',va='center', color='black',fontsize=120)
    return(tab)
#%% ordi raisonement des paires + des triples + se defend mal niv 3 (pas stable)
def niv3(N,tab,j_):
    
    place=[]
    for i in range (1,N-1):
        for j in range (0,N-2):
            if tab[i][j]!=0:
                if tab[i][j]==tab[i+1][j]:
                    if (i+2)<N-1:
                        place.append(i+2)
                    if (i-1)!=0:
                        place.append(i-1)
                if tab[i][j]==tab[i][j+1]:
                    place.append(i)
    
    
    triple=[]
    for i in range (1,N-1):
        for j in range (0,N-2):
            if tab[i][j]!=0:
                if tab[i][j]==tab[i+1][j]==tab[i+2][j]:
                    if (i+3)<N-1:
                        triple.append(i+3)
                    if (i-1)!=0:
                        triple.append(i-1)
                if tab[i][j]==tab[i][j+1]==tab[i][j+2]:
                    triple.append(i)
                if tab[i][j]==tab[i+1][j+1]==tab[i+2][j+2]:
                    if (i+3)<N-1:
                        triple.append(i+3)
                    if (i-1)!=0:
                        triple.append(i-1)
                if tab[i+2][j]==tab[i+1][j+1]==tab[i][j+2]:
                    if (i+3)<N-1:
                        triple.append(i+3)
                    if (i-1)!=0:
                        triple.append(i-1)
                        
    place_smart=[]
    for i in range (1,N-1):
        for j in range (0,N-2):
            if tab[i][j]!=0:
                if tab[i][j]==tab[i+1][j]:
                    if tab[i+2][j]==0:
                        place_smart.append(i+2)
                    if tab[i-1][j]==0:
                        place_smart.append(i-1)
                if tab[i][j]==tab[i][j+1]:
                    if tab[i][j-1]==0:
                        place_smart.append(i)
    
    
    triple_smart=[]
    for i in range (1,N-3):
        for j in range (0,N-2):
            if tab[i][j]!=0:
                if tab[i][j]==tab[i+1][j]==tab[i+2][j]:
                    if tab[i+3][j]==0:
                        triple_smart.append(i+3)
                    if tab[i-1][j]==0:
                        triple_smart.append(i-1)
                if tab[i][j]==tab[i][j+1]==tab[i][j+2]:
                    if tab[i][j-1]==0:
                        triple_smart.append(i)
                if tab[i][j]==tab[i+1][j+1]==tab[i+2][j+2]:
                    if tab[i+3][j+3]==0:
                        triple_smart.append(i+3)
                    if tab[i-1][j-1]==0:
                        triple_smart.append(i-1)
                if tab[i+2][j]==tab[i+1][j+1]==tab[i][j+2]:
                    if tab[i+3][j-1]==0:
                        triple_smart.append(i+3)
                    if tab[i-1][j+3]==0:
                        triple_smart.append(i-1)
    print(triple_smart)
    print(place_smart)
    print(triple)
    print(place)
    if triple_smart:
        a=rd.choice(triple_smart)
    elif place_smart:
        a=rd.choice(place_smart)
    elif triple:
        a=rd.choice(triple)
    elif place:
        a=rd.choice(place)
    else:
        a=rd.randint(3,5)
        
    x=a
    y=0
    tab2=np.zeros((N,N))
    for i in range (0,N):
        tab2[i][N-1]=3
        tab2[i][N-2]=3
        tab2[0][i]=3
        tab2[N-1][i]=3
    sumtab=0
    sumtab2=0
    for (i,j), val in np.ndenumerate(tab):
        tab2[i][j]=tab[i][j]
        sumtab+=tab[i][j]
        sumtab2+=tab2[i][j]
    while sumtab==sumtab2:
        if tab[x][y+1]==0:
            while tab[x][y+1]==0:
                y=y+1
                if tab[x][y+1]!=0:
                    tab[x][y]=j_
                    sumtab+=tab[x][y]
                else:
                    x=a
    
        else:
            if tab[x][y]==0:
                tab[x][y]=j_
                sumtab+=tab[x][y]
            else:
                x=a
        
    
    # fig,ax=plt.subplots(figsize=(N+np.sqrt(N),N+np.sqrt(N)))
    
    # cax=ax.matshow(tab,cmap='Greys',vmin=0,vmax=0)
    # ax.set_xticks(np.arange(tab.shape[0])-.5, minor=True)
    # ax.set_yticks(np.arange(tab.shape[1])-.5, minor=True)
    # ax.grid(which='minor',color='black')
    
    # ax.tick_params(which='minor',size=0)
    # ax.set_xticklabels([])
    # ax.set_yticklabels([])
    # for i in range(0,N):
    #     for j in range(0,N):
    #         if tab[i][j]==1:
    #             ax.text(i,j,'o', ha='center',va='center', color='blue',fontsize=60)
    #         if tab[i][j]==2:
    #             ax.text(i,j,'o', ha='center',va='center', color='red',fontsize=60)
    #         if tab[i][j]==3:
    #             ax.text(i,j,'+', ha='center',va='center', color='black',fontsize=120)
    return(tab)
#%% ordi se defend assez bien niv 4
def niv4(N,tab,j_):
    stop=False
    place=[]
    for i in range (1,N-1):
        for j in range (0,N-2):
            if tab[i][j]!=0:
                if tab[i][j]==tab[i+1][j]:
                    if (i+2)<N-1:
                        place.append(i+2)
                    if (i-1)!=0:
                        place.append(i-1)
                if tab[i][j]==tab[i][j+1]:
                    place.append(i)
    
    
    triple=[]
    for i in range (1,N-2):
        for j in range (0,N-2):
            if tab[i][j]!=0:
                if tab[i][j]==tab[i+1][j]==tab[i+2][j]:
                    if (i+3)<N-1:
                        triple.append(i+3)
                    if (i-1)!=0:
                        triple.append(i-1)
                if tab[i][j]==tab[i][j+1]==tab[i][j+2]:
                    triple.append(i)
                if tab[i][j]==tab[i+1][j+1]==tab[i+2][j+2]:
                    if (i+3)<N-1:
                        triple.append(i+3)
                    if (i-1)!=0:
                        triple.append(i-1)
                if tab[i+2][j]==tab[i+1][j+1]==tab[i][j+2]:
                    if (i+3)<N-1:
                        triple.append(i+3)
                    if (i-1)!=0:
                        triple.append(i-1)
                        
    place_smart=[]
    for i in range (1,N-2):
        for j in range (0,N-2):
            if tab[i][j]!=0:
                if tab[i][j]==tab[i+1][j]:
                    if tab[i+2][j]==0:
                        place_smart.append(i+2)
                    if tab[i-1][j]==0:
                        place_smart.append(i-1)
                if tab[i][j]==tab[i+1][j+1]:
                    if tab[i-1][j-1]==0:
                        place_smart.append(i-1)
                    if tab[i+2][j+2]==0:
                        place_smart.append(i+2)
                if tab[i][j+1]==tab[i+1][j]:
                    if tab[i-1][j]==0:
                        place_smart.append(i-1)
                    if tab[i+2][j+1]==0:
                        place_smart.append(i+2)
    for i in range (1,N-1):
        for j in range (0,N-2):
            if tab[i][j]!=0:    
                if tab[i][j]==tab[i][j+1]:
                    if tab[i][j-1]==0:
                        place_smart.append(i)
    
    
                        
    gagne=[]    
    for i in range (1,N-3):
        for j in range (0,N-2):
            if tab[i][j]!=0:
                if tab[i][j]==tab[i+1][j]==tab[i+2][j]:
                    if tab[i+3][j]==0 and tab[i+3][j+1]!=0:
                        gagne.append(i+3)
                    if tab[i-1][j]==0 and tab[i-1][j+1]!=0:
                        gagne.append(i-1)
    for i in range (1,N-1):
        for j in range (0,N-2):
            if tab[i][j]!=0:
                if tab[i][j]==tab[i][j+1]==tab[i][j+2]:
                    if tab[i][j-1]==0:
                        gagne.append(i)
    for i in range (1,N-3):
        for j in range (0,N-4):
            if tab[i][j]!=0:               
                if tab[i][j]==tab[i+1][j+1]==tab[i+2][j+2]:
                    if tab[i+3][j+3]==0 and tab[i+3][j+4]!=0:
                        gagne.append(i+3)
                    if tab[i-1][j-1]==0 and tab[i-1][j]!=0:
                        gagne.append(i-1)
    for i in range (3,N-1):
        for j in range (0,N-4):
            if tab[i][j]!=0:
                if tab[i-2][j+2]==tab[i-1][j+1]==tab[i][j]:
                    if tab[i+1][j-1]==0 and tab[i+1][j]!=0:
                        gagne.append(i+1)
                    if tab[i-3][j+3]==0 and tab[i-3][j+4]!=0:
                        gagne.append(i-3)
                        
    defense=[]              
    for i in range (1,N-2):
        for j in range (0,N-2):
            if tab[i][j]!=0:
                if tab[i][j]==tab[i+1][j]:
                    if tab[i+2][j]==0 and tab[i+2][j+1]!=0:
                        defense.append(i+2)
                    if tab[i-1][j]==0 and tab[i-1][j+1]!=0:
                        defense.append(i-1)
                if tab[i][j]==tab[i+1][j+1]:
                    if tab[i-1][j-1]==0 and tab[i-1][j]!=0:
                        defense.append(i-1)
                    if tab[i+2][j+2]==0 and tab[i+2][j+1]!=0:
                        defense.append(i+2)
                if tab[i][j+1]==tab[i+1][j]:
                    if tab[i-1][j]==0 and tab[i-1][j+1]!=0:
                        defense.append(i-1)
                    if tab[i+2][j-1]==0 and tab[i+2][j]!=0:
                        defense.append(i+2)
    for i in range (1,N-1):
        for j in range (0,N-2):
            if tab[i][j]!=0:    
                if tab[i][j]==tab[i][j+1]:
                    if tab[i][j-1]==0:
                        defense.append(i)
    reste=[]
    for i in range (1,N-1):
        reste.append(i)
    if gagne:
        a=rd.choice(gagne)
    elif defense:
        a=rd.choice(defense)
    elif place_smart:
        a=rd.choice(place_smart)
    elif triple:
        a=rd.choice(triple)
    elif place:
        a=rd.choice(place)
    else:
        a=rd.randint(3,5)
        
    y=0
    tab2=np.zeros((N,N))
    for i in range (0,N):
        tab2[i][N-1]=3
        tab2[i][N-2]=3
        tab2[0][i]=3
        tab2[N-1][i]=3
    sumtab=0
    sumtab2=0
    for (i,j), val in np.ndenumerate(tab):
        tab2[i][j]=tab[i][j]
        sumtab+=tab[i][j]
        sumtab2+=tab2[i][j]
    while sumtab==sumtab2:
        if tab[a][y+1]==0:
            while tab[a][y+1]==0:
                y=y+1
                if tab[a][y+1]!=0:
                    tab[a][y]=j_
                    sumtab+=tab[a][y]
                else:
                    if gagne:
                        a=rd.choice(gagne)
                    elif defense:
                        a=rd.choice(defense)
                    elif place_smart:
                        a=rd.choice(place_smart)
                        place_smart.remove(a)
                    elif triple:
                        a=rd.choice(triple)
                        triple.remove(a)
                    elif place:
                        a=rd.choice(place)
                        place.remove(a)
                    elif reste:
                        a=rd.choice(reste)
                        reste.remove(a)
                    else:
                        stop=True
                        break
    
        else:
            if tab[a][y]==0:
                tab[a][y]=j_
                sumtab+=tab[a][y]
            else:
                 if gagne:
                     a=rd.choice(gagne)
                 elif defense:
                     a=rd.choice(defense)
                 elif place_smart:
                     a=rd.choice(place_smart)
                     place_smart.remove(a)
                 elif triple:
                     a=rd.choice(triple)
                     triple.remove(a)
                 elif place:
                     a=rd.choice(place)
                     place.remove(a)
                 elif reste:
                     a=rd.choice(reste)
                     reste.remove(a)
                 else:
                     stop=True
                     break
        if stop:
            break
    print(gagne)
    print(defense)
    print(place_smart)
    print(triple)
    print(place)
    return(tab,stop)
#%% ordi se defend bien niv 5 (pas stable)
def niv5(N,tab,j_):
    
    place=[]
    for i in range (1,N-1):
        for j in range (0,N-2):
            if tab[i][j]!=0:
                if tab[i][j]==tab[i+1][j]:
                    if (i+2)<N-1:
                        place.append(i+2)
                    if (i-1)!=0:
                        place.append(i-1)
                if tab[i][j]==tab[i][j+1]:
                    place.append(i)
    
                        
    gagne=[]    
    for i in range (1,N-3):
        for j in range (0,N-2):
            if tab[i][j]!=0:
                if tab[i][j]==tab[i+1][j]==tab[i+2][j]:
                    if tab[i+3][j]==0 and tab[i+3][j+1]!=0:
                        gagne.append(i+3)
                    if tab[i-1][j]==0 and tab[i-1][j+1]!=0:
                        gagne.append(i-1)
                if tab[i][j]==tab[i+1][j]==tab[i+3][j]:
                    if tab[i+2][j]==0 and tab[i+2][j+1]!=0:
                        gagne.append(i+2)
                if tab[i][j]==tab[i+2][j]==tab[i+3][j]:
                    if tab[i+1][j]==0 and tab[i+1][j+1]!=0:
                        gagne.append(i+1)
    for i in range (1,N-1):
        for j in range (0,N-2):
            if tab[i][j]!=0:
                if tab[i][j]==tab[i][j+1]==tab[i][j+2]:
                    if tab[i][j-1]==0:
                        gagne.append(i)
    for i in range (1,N-3):
        for j in range (0,N-4):
            if tab[i][j]!=0:               
                if tab[i][j]==tab[i+1][j+1]==tab[i+2][j+2]:
                    if tab[i+3][j+3]==0 and tab[i+3][j+4]!=0:
                        gagne.append(i+3)
                    if tab[i-1][j-1]==0 and tab[i-1][j]!=0:
                        gagne.append(i-1)
                if tab[i][j]==tab[i+1][j+1]==tab[i+3][j+3]:
                    if tab[i+2][j+2]==0 and tab[i+2][j+3]!=0:
                        gagne.append(i+2)
                if tab[i][j]==tab[i+2][j+2]==tab[i+3][j+3]:
                    if tab[i+1][j+1]==0 and tab[i+1][j+2]!=0:
                        gagne.append(i+1)
    for i in range (3,N-1):
        for j in range (0,N-4):
            if tab[i][j]!=0:
                if tab[i-2][j+2]==tab[i-1][j+1]==tab[i][j]:
                    if tab[i+1][j-1]==0 and tab[i+1][j]!=0:
                        gagne.append(i+1)
                    if tab[i-3][j+3]==0 and tab[i-3][j+4]!=0:
                        gagne.append(i-3)
                if tab[i][j]==tab[i-1][j+1]==tab[i-3][j+3]:
                    if tab[i-2][j+2]==0 and tab[i-2][j+3]!=0:
                        gagne.append(i-2)
                if tab[i][j]==tab[i-2][j+2]==tab[i-3][j+3]:
                    if tab[i-1][j+1]==0 and tab[i-1][j+2]!=0:
                        gagne.append(i-1)
    defense_smart=[]              
    for i in range (1,N-2):
        for j in range (0,N-2):
            if tab[i][j]!=0:
                if tab[i][j]==tab[i+1][j]:
                    if tab[i+2][j]==0 and tab[i+2][j+1]!=0:
                        defense_smart.append(i+2)
                    if tab[i-1][j]==0 and tab[i-1][j+1]!=0:
                        defense_smart.append(i-1)
                if tab[i][j]==tab[i+1][j+1]:
                    if tab[i-1][j-1]==0 and tab[i-1][j]!=0:
                        defense_smart.append(i-1)
                    if tab[i+2][j+2]==0 and tab[i+2][j+1]!=0:
                        defense_smart.append(i+2)
                if tab[i][j]==tab[i-1][j+1]:
                    if tab[i-1][j+2]==0 and tab[i-1][j+3]!=0:
                        defense_smart.append(i-1)
                    if tab[i+1][j-1]==0 and tab[i+1][j]!=0:
                        defense_smart.append(i+1)
    for i in range (1,N-1):
        for j in range (0,N-2):
            if tab[i][j]!=0:    
                if tab[i][j]==tab[i][j+1]:
                    if tab[i][j-1]==0:
                        defense_smart.append(i)

                
    print(gagne)
    print(defense_smart)
    print(place)
    if gagne:
        a=rd.choice(gagne)
    elif defense_smart:
        a=rd.choice(defense_smart)
    elif place:
        a=rd.choice(place)
    else:
        a=rd.randint(1,7)
        
    x=a
    y=0
    tab2=np.zeros((N,N))
    for i in range (0,N):
        tab2[i][N-1]=3
        tab2[i][N-2]=3
        tab2[0][i]=3
        tab2[N-1][i]=3
    sumtab=0
    sumtab2=0
    for (i,j), val in np.ndenumerate(tab):
        tab2[i][j]=tab[i][j]
        sumtab+=tab[i][j]
        sumtab2+=tab2[i][j]
    while sumtab==sumtab2:
        if tab[x][y+1]==0:
            while tab[x][y+1]==0:
                y=y+1
                if tab[x][y+1]!=0:
                    tab[x][y]=j_
                    sumtab+=tab[x][y]
                else:
                    x=a
    
        else:
            if tab[x][y]==0:
                tab[x][y]=j_
                sumtab+=tab[x][y]
            else:
                x=a
        

    return(tab)



#%%
def victoire(N,tab,stop):
    v=[]    
    for i in range (1,N-3):
        for j in range (0,N-2):
            if tab[i][j]!=0:
                if tab[i][j]==tab[i+1][j]==tab[i+2][j]==tab[i+3][j]:
                    v.append(tab[i][j])
    for i in range (1,N-1):
        for j in range (0,N-4):
            if tab[i][j]!=0:
                if tab[i][j]==tab[i][j+1]==tab[i][j+2]==tab[i][j+3]:
                    v.append(tab[i][j])
    for i in range (1,N-3):
        for j in range (0,N-4):
            if tab[i][j]!=0:               
                if tab[i][j]==tab[i+1][j+1]==tab[i+2][j+2]==tab[i+3][j+3]:
                    v.append(tab[i][j])
    for i in range (3,N-1):
        for j in range (0,N-4):
            if tab[i][j]!=0:
                if tab[i-2][j+2]==tab[i-1][j+1]==tab[i][j]==tab[i-3][j+3]:
                    v.append(tab[i][j])
    if v:
        victoire=1
        print('partie terminé')
    elif stop:
        victoire=2
        print('partie terminé')
    else:
        victoire=0
    return(victoire)
#%% niv6 commence a attaqué (pas stable)
def niv6(N,tab,j_):
                     
    gagne=[]    
    for i in range (1,N-3):
        for j in range (0,N-2):
            if tab[i][j]!=0:
                if tab[i][j]==tab[i+1][j]==tab[i+2][j]:
                    if tab[i+3][j]==0 and tab[i+3][j+1]!=0:
                        gagne.append(i+3)
                    if tab[i-1][j]==0 and tab[i-1][j+1]!=0:
                        gagne.append(i-1)
                if tab[i][j]==tab[i+1][j]==tab[i+3][j]:
                    if tab[i+2][j]==0 and tab[i+2][j+1]!=0:
                        gagne.append(i+2)
                if tab[i][j]==tab[i+2][j]==tab[i+3][j]:
                    if tab[i+1][j]==0 and tab[i+1][j+1]!=0:
                        gagne.append(i+1)
    for i in range (1,N-1):
        for j in range (0,N-2):
            if tab[i][j]!=0:
                if tab[i][j]==tab[i][j+1]==tab[i][j+2]:
                    if tab[i][j-1]==0:
                        gagne.append(i)
    for i in range (1,N-3):
        for j in range (0,N-4):
            if tab[i][j]!=0:               
                if tab[i][j]==tab[i+1][j+1]==tab[i+2][j+2]:
                    if tab[i+3][j+3]==0 and tab[i+3][j+4]!=0:
                        gagne.append(i+3)
                    if tab[i-1][j-1]==0 and tab[i-1][j]!=0:
                        gagne.append(i-1)
                if tab[i][j]==tab[i+1][j+1]==tab[i+3][j+3]:
                    if tab[i+2][j+2]==0 and tab[i+2][j+3]!=0:
                        gagne.append(i+2)
                if tab[i][j]==tab[i+2][j+2]==tab[i+3][j+3]:
                    if tab[i+1][j+1]==0 and tab[i+1][j+2]!=0:
                        gagne.append(i+1)
    for i in range (3,N-1):
        for j in range (0,N-4):
            if tab[i][j]!=0:
                if tab[i-2][j+2]==tab[i-1][j+1]==tab[i][j]:
                    if tab[i+1][j-1]==0 and tab[i+1][j]!=0:
                        gagne.append(i+1)
                    if tab[i-3][j+3]==0 and tab[i-3][j+4]!=0:
                        gagne.append(i-3)
                if tab[i][j]==tab[i-1][j+1]==tab[i-3][j+3]:
                    if tab[i-2][j+2]==0 and tab[i-2][j+3]!=0:
                        gagne.append(i-2)
                if tab[i][j]==tab[i-2][j+2]==tab[i-3][j+3]:
                    if tab[i-1][j+1]==0 and tab[i-1][j+2]!=0:
                        gagne.append(i-1)
    defense_smart=[]              
    for i in range (1,N-2):
        for j in range (0,N-2):
            if tab[i][j]!=0:
                if tab[i][j]==tab[i+1][j]:
                    if tab[i+2][j]==0 and tab[i+2][j+1]!=0:
                        defense_smart.append(i+2)
                    if tab[i-1][j]==0 and tab[i-1][j+1]!=0:
                        defense_smart.append(i-1)
                if tab[i][j]==tab[i+1][j+1]:
                    if tab[i-1][j-1]==0 and tab[i-1][j]!=0:
                        defense_smart.append(i-1)
                    if tab[i+2][j+2]==0 and tab[i+2][j+1]!=0:
                        defense_smart.append(i+2)
                if tab[i][j]==tab[i-1][j+1]:
                    if tab[i-1][j+2]==0 and tab[i-1][j+3]!=0:
                        defense_smart.append(i-1)
                    if tab[i+1][j-1]==0 and tab[i+1][j]!=0:
                        defense_smart.append(i+1)
    for i in range (3,N-1):
        for j in range (0,N-4):
            if tab[i][j]!=0:
                if tab[i-2][j+2]==tab[i][j]:
                    if tab[i-1][j+1]==0 and tab[i-1][j+2]!=0:
                        defense_smart.append(i-1)
    for i in range (1,N-3):
        for j in range (0,N-2):
            if tab[i][j]!=0:               
                if tab[i][j]==tab[i+2][j+2]:
                    if tab[i+1][j+1]==0 and tab[i+1][j+2]!=0:
                        defense_smart.append(i+1)
    for i in range (1,N-1):
        for j in range (0,N-2):
            if tab[i][j]!=0:    
                if tab[i][j]==tab[i][j+1]:
                    if tab[i][j-1]==0:
                        defense_smart.append(i)
    attaque=[] 
    tour=0          
    for i in range (2,N-2):
        for j in range (0,N-2):
            if tab[i][j]!=0:
                if tour<4:
                    if tab[i][j]==1:
                        attaque.append(i+1)
                        attaque.append(i-1)
                if tour>3:
                    if tab[i][j]==2 and tab[i+1][j]==0:
                        attaque.append(i+1)
                    if tab[i][j]==2 and tab[i-1][j]==0:
                        attaque.append(i-1)
                    if tab[i][j]==2 and tab[i+1][j+1]==0:
                        attaque.append(i+1)
                    if tab[i][j]==2 and tab[i-1][j+1]==0:
                        attaque.append(i-1)
                    if tab[i][j]==2 and tab[i][j+1]==0:
                        attaque.append(i)
                
    print(gagne)
    print(defense_smart)
    print(attaque)
    if gagne:
        a=rd.choice(gagne)
    elif defense_smart:
        a=rd.choice(defense_smart)
    elif attaque:
        a=rd.choice(attaque)
    else:
        a=rd.randint(1,7)
        
    x=a
    y=0
    tab2=np.zeros((N,N))
    for i in range (0,N):
        tab2[i][N-1]=3
        tab2[i][N-2]=3
        tab2[0][i]=3
        tab2[N-1][i]=3
    sumtab=0
    sumtab2=0
    for (i,j), val in np.ndenumerate(tab):
        tab2[i][j]=tab[i][j]
        sumtab+=tab[i][j]
        sumtab2+=tab2[i][j]
    while sumtab==sumtab2:
        if tab[x][y+1]==0:
            while tab[x][y+1]==0:
                y=y+1
                if tab[x][y+1]!=0:
                    tab[x][y]=j_
                    sumtab+=tab[x][y]
                else:
                    x=a
    
        else:
            if tab[x][y]==0:
                tab[x][y]=j_
                sumtab+=tab[x][y]
            else:
                x=a
        

    return(tab)

#%% niv7 ne donne pas la victoire

def niv7(N,tab,j_):
    stop=False
    place=[]
    for i in range (1,N-1):
        for j in range (0,N-2):
            if tab[i][j]!=0:
                if tab[i][j]==tab[i+1][j]:
                    if (i+2)<N-1:
                        place.append(i+2)
                    if (i-1)!=0:
                        place.append(i-1)
                if tab[i][j]==tab[i][j+1]:
                    place.append(i)
    gagne=[]    
    for i in range (1,N-3):
        for j in range (0,N-2):
            if tab[i][j]!=0:
                if tab[i][j]==tab[i+1][j]==tab[i+2][j]:
                    if tab[i+3][j]==0 and tab[i+3][j+1]!=0:
                        gagne.append(i+3)
                    if tab[i-1][j]==0 and tab[i-1][j+1]!=0:
                        gagne.append(i-1)
                if tab[i][j]==tab[i+1][j]==tab[i+3][j]:
                    if tab[i+2][j]==0 and tab[i+2][j+1]!=0:
                        gagne.append(i+2)
                if tab[i][j]==tab[i+2][j]==tab[i+3][j]:
                    if tab[i+1][j]==0 and tab[i+1][j+1]!=0:
                        gagne.append(i+1)
    for i in range (1,N-1):
        for j in range (0,N-2):
            if tab[i][j]!=0:
                if tab[i][j]==tab[i][j+1]==tab[i][j+2]:
                    if tab[i][j-1]==0:
                        gagne.append(i)
    for i in range (1,N-3):
        for j in range (0,N-4):
            if tab[i][j]!=0:               
                if tab[i][j]==tab[i+1][j+1]==tab[i+2][j+2]:
                    if tab[i+3][j+3]==0 and tab[i+3][j+4]!=0:
                        gagne.append(i+3)
                    if tab[i-1][j-1]==0 and tab[i-1][j]!=0:
                        gagne.append(i-1)
                if tab[i][j]==tab[i+1][j+1]==tab[i+3][j+3]:
                    if tab[i+2][j+2]==0 and tab[i+2][j+3]!=0:
                        gagne.append(i+2)
                if tab[i][j]==tab[i+2][j+2]==tab[i+3][j+3]:
                    if tab[i+1][j+1]==0 and tab[i+1][j+2]!=0:
                        gagne.append(i+1)
    for i in range (3,N-1):
        for j in range (0,N-4):
            if tab[i][j]!=0:
                if tab[i-2][j+2]==tab[i-1][j+1]==tab[i][j]:
                    if tab[i+1][j-1]==0 and tab[i+1][j]!=0:
                        gagne.append(i+1)
                    if tab[i-3][j+3]==0 and tab[i-3][j+4]!=0:
                        gagne.append(i-3)
                if tab[i][j]==tab[i-1][j+1]==tab[i-3][j+3]:
                    if tab[i-2][j+2]==0 and tab[i-2][j+3]!=0:
                        gagne.append(i-2)
                if tab[i][j]==tab[i-2][j+2]==tab[i-3][j+3]:
                    if tab[i-1][j+1]==0 and tab[i-1][j+2]!=0:
                        gagne.append(i-1)
    defense_smart=[]              
    for i in range (1,N-2):
        for j in range (0,N-2):
            if tab[i][j]!=0:
                if tab[i][j]==tab[i+1][j]:
                    if tab[i+2][j]==0 and tab[i+2][j+1]!=0:
                        defense_smart.append(i+2)
                    if tab[i-1][j]==0 and tab[i-1][j+1]!=0:
                        defense_smart.append(i-1)
                if tab[i][j]==tab[i+1][j+1]:
                    if tab[i-1][j-1]==0 and tab[i-1][j]!=0:
                        defense_smart.append(i-1)
                    if tab[i+2][j+2]==0 and tab[i+2][j+3]!=0:
                        defense_smart.append(i+2)
                if tab[i][j]==tab[i-1][j+1]:
                    if tab[i-2][j+2]==0 and tab[i-2][j+3]!=0:
                        defense_smart.append(i-2)
                    if tab[i+1][j-1]==0 and tab[i+1][j]!=0:
                        defense_smart.append(i+1)
    for i in range (3,N-1):
        for j in range (0,N-4):
            if tab[i][j]!=0:
                if tab[i-2][j+2]==tab[i][j]:
                    if tab[i-1][j+1]==0 and tab[i-1][j+2]!=0:
                        defense_smart.append(i-1)
    for i in range (1,N-3):
        for j in range (0,N-2):
            if tab[i][j]!=0:               
                if tab[i][j]==tab[i+2][j+2]:
                    if tab[i+1][j+1]==0 and tab[i+1][j+2]!=0:
                        defense_smart.append(i+1)
    for i in range (1,N-1):
        for j in range (0,N-2):
            if tab[i][j]!=0:    
                if tab[i][j]==tab[i][j+1]:
                    if tab[i][j-1]==0:
                        defense_smart.append(i)
    attaque=[]     
    for i in range (1,N-1):
        for j in range (0,N-2):
            if tab[i][j]!=0:
                if tab[i][j]==j_:
                    if tab[i+1][j]==0 and tab[i+1][j+1]!=0:
                        attaque.append(i+1)
                    if tab[i-1][j]==0 and tab[i-1][j+1]!=0:
                        attaque.append(i-1)
    for i in range (1,N-1):
        for j in range (1,N-2):
            if tab[i][j]!=0:
                if tab[i][j]==j_:
                    if tab[i][j]==0 and tab[i][j-1]==0:
                        attaque.append(i)
                        
    
         
    for i in range (1,N-3):
        for j in range (0,N-3):
            if tab[i][j]!=0:
                if tab[i][j]==tab[i+1][j]==tab[i+2][j]==1:
                    if tab[i+3][j]==0 and tab[i+3][j+2]!=0:
                        while i+3 in defense_smart:
                            defense_smart.remove(i+3)
                        while i+3 in attaque:
                            attaque.remove(i+3)
                    if tab[i-1][j]==0 and tab[i-1][j+2]!=0:
                        while i-1 in defense_smart:
                            defense_smart.remove(i-1)
                        while i-1 in attaque:
                            attaque.remove(i-1)
                if tab[i][j]==tab[i+1][j]==tab[i+3][j]==1:
                    if tab[i+2][j]==0 and tab[i+2][j+2]!=0:
                        while i+2 in defense_smart:
                            defense_smart.remove(i+2)
                        while i+2 in attaque:
                            attaque.remove(i+2)
                if tab[i][j]==tab[i+2][j]==tab[i+3][j]==1:
                    if tab[i+1][j]==0 and tab[i+1][j+2]!=0:
                        while i+1 in defense_smart:
                            defense_smart.remove(i+1)
                        while i+1 in attaque:
                            attaque.remove(i+1)
    for i in range (1,N-3):
        for j in range (0,N-5):
            if tab[i][j]!=0:               
                if tab[i][j]==tab[i+1][j+1]==tab[i+2][j+2]==1:
                    if tab[i+3][j+3]==0 and tab[i+3][j+5]!=0:
                        while i+3 in defense_smart:
                            defense_smart.remove(i+3)
                        while i+3 in attaque:
                            attaque.remove(i+3)
                    if tab[i-1][j-1]==0 and tab[i-1][j]!=0:
                        while i-1 in defense_smart:
                            defense_smart.remove(i-1)
                        while i-1 in attaque:
                            attaque.remove(i-1)
                if tab[i][j]==tab[i+1][j+1]==tab[i+3][j+3]==1:
                    if tab[i+2][j+2]==0 and tab[i+2][j+4]!=0:
                        while i+2 in defense_smart:
                            defense_smart.remove(i+2)
                        while i+2 in attaque:
                            attaque.remove(i+2)
                if tab[i][j]==tab[i+2][j+2]==tab[i+3][j+3]==1:
                    if tab[i+1][j+1]==0 and tab[i+1][j+3]!=0:
                        while i+1 in defense_smart:
                            defense_smart.remove(i+1)
                        while i+1 in attaque:
                            attaque.remove(i+1)
    for i in range (3,N-1):
        for j in range (0,N-4):
            if tab[i][j]!=0:
                if tab[i-2][j+2]==tab[i-1][j+1]==tab[i][j]==1:
                    if tab[i+1][j-1]==0 and tab[i+1][j+1]!=0:
                        while i+1 in defense_smart:
                            defense_smart.remove(i+1)
                        while i+1 in attaque:
                            attaque.remove(i+1)
                if tab[i][j]==tab[i-1][j+1]==tab[i-3][j+3]==1:
                    if tab[i-2][j+2]==0 and tab[i-2][j+4]!=0:
                        while i-2 in defense_smart:
                            defense_smart.remove(i-2)
                        while i-2 in attaque:
                            attaque.remove(i-2)
                if tab[i][j]==tab[i-2][j+2]==tab[i-3][j+3]==1:
                    if tab[i-1][j+1]==0 and tab[i-1][j+3]!=0:
                        while i-1 in defense_smart:
                            defense_smart.remove(i-1)
                        while i-1 in attaque:
                            attaque.remove(i-1)  
    for i in range (3,N-1):
        for j in range (0,N-5):
            if tab[i][j]!=0:
                if tab[i-2][j+2]==tab[i-1][j+1]==tab[i][j]==1:
                    if tab[i-3][j+3]==0 and tab[i-3][j+5]!=0:
                        while i-3 in defense_smart:
                            defense_smart.remove(i-3)
                        while i-3 in attaque:
                            attaque.remove(i-3)
                     
    reste=[]
    for i in range (1,N-1):
        reste.append(i)
    if gagne:
        a=rd.choice(gagne)
    elif defense_smart:
        a=rd.choice(defense_smart)
    elif attaque:
        a=rd.choice(attaque)
    elif place:
        a=rd.choice(place)
    else:
        a=rd.randint(2,6)
            

    y=0
    tab2=np.zeros((N,N))
    for i in range (0,N):
        tab2[i][N-1]=3
        tab2[i][N-2]=3
        tab2[0][i]=3
        tab2[N-1][i]=3
    sumtab=0
    sumtab2=0
    for (i,j), val in np.ndenumerate(tab):
        tab2[i][j]=tab[i][j]
        sumtab+=tab[i][j]
        sumtab2+=tab2[i][j]
    while sumtab==sumtab2:
        if tab[a][y+1]==0:
            while tab[a][y+1]==0:
                y=y+1
                if tab[a][y+1]!=0:
                    tab[a][y]=j_
                    sumtab+=tab[a][y]
                else:
                    if gagne:
                        a=rd.choice(gagne)
                    elif defense_smart:
                        a=rd.choice(defense_smart)
                    elif attaque:
                        a=rd.choice(attaque)
                    elif place:
                        a=rd.choice(place)
                        place.remove(a)
                    elif reste:
                        a=rd.choice(reste)
                        reste.remove(a)
                    else:
                        stop=True
                        break
        else:
            if tab[a][y]==0:
                tab[a][y]=j_
                sumtab+=tab[a][y]
            else:
                if gagne:
                    a=rd.choice(gagne)
                elif defense_smart:
                    a=rd.choice(defense_smart)
                elif attaque:
                    a=rd.choice(attaque)
                elif place:
                    a=rd.choice(place)
                    place.remove(a)
                elif reste:
                    a=rd.choice(reste)
                    reste.remove(a)
                else:
                    stop=True
                    break
        if stop:
            break
    print(gagne)
    print(defense_smart)
    print(attaque)
    print(place)
    return(tab,stop)

#%% niv8

def niv8(N,tab,j_):
    stop=False
    place=[]
    for i in range (1,N-1):
        for j in range (0,N-2):
            if tab[i][j]!=0:
                if tab[i][j]==tab[i+1][j]:
                    if (i+2)<N-1:
                        place.append(i+2)
                    if (i-1)!=0:
                        place.append(i-1)
                if tab[i][j]==tab[i][j+1]:
                    place.append(i)
    gagne=[]    
    for i in range (1,N-3):
        for j in range (0,N-2):
            if tab[i][j]!=0:
                if tab[i][j]==tab[i+1][j]==tab[i+2][j]:
                    if tab[i+3][j]==0 and tab[i+3][j+1]!=0:
                        gagne.append(i+3)
                    if tab[i-1][j]==0 and tab[i-1][j+1]!=0:
                        gagne.append(i-1)
                if tab[i][j]==tab[i+1][j]==tab[i+3][j]:
                    if tab[i+2][j]==0 and tab[i+2][j+1]!=0:
                        gagne.append(i+2)
                if tab[i][j]==tab[i+2][j]==tab[i+3][j]:
                    if tab[i+1][j]==0 and tab[i+1][j+1]!=0:
                        gagne.append(i+1)
    for i in range (1,N-1):
        for j in range (0,N-2):
            if tab[i][j]!=0:
                if tab[i][j]==tab[i][j+1]==tab[i][j+2]:
                    if tab[i][j-1]==0:
                        gagne.append(i)
    for i in range (1,N-3):
        for j in range (0,N-4):
            if tab[i][j]!=0:               
                if tab[i][j]==tab[i+1][j+1]==tab[i+2][j+2]:
                    if tab[i+3][j+3]==0 and tab[i+3][j+4]!=0:
                        gagne.append(i+3)
                    if tab[i-1][j-1]==0 and tab[i-1][j]!=0:
                        gagne.append(i-1)
                if tab[i][j]==tab[i+1][j+1]==tab[i+3][j+3]:
                    if tab[i+2][j+2]==0 and tab[i+2][j+3]!=0:
                        gagne.append(i+2)
                if tab[i][j]==tab[i+2][j+2]==tab[i+3][j+3]:
                    if tab[i+1][j+1]==0 and tab[i+1][j+2]!=0:
                        gagne.append(i+1)
    for i in range (3,N-1):
        for j in range (0,N-4):
            if tab[i][j]!=0:
                if tab[i-2][j+2]==tab[i-1][j+1]==tab[i][j]:
                    if tab[i+1][j-1]==0 and tab[i+1][j]!=0:
                        gagne.append(i+1)
                    if tab[i-3][j+3]==0 and tab[i-3][j+4]!=0:
                        gagne.append(i-3)
                if tab[i][j]==tab[i-1][j+1]==tab[i-3][j+3]:
                    if tab[i-2][j+2]==0 and tab[i-2][j+3]!=0:
                        gagne.append(i-2)
                if tab[i][j]==tab[i-2][j+2]==tab[i-3][j+3]:
                    if tab[i-1][j+1]==0 and tab[i-1][j+2]!=0:
                        gagne.append(i-1)
    defense_smart=[]              
    for i in range (1,N-2):
        for j in range (0,N-2):
            if tab[i][j]!=0:
                if tab[i][j]==tab[i+1][j]:
                    if tab[i+2][j]==0 and tab[i+2][j+1]!=0:
                        defense_smart.append(i+2)
                    if tab[i-1][j]==0 and tab[i-1][j+1]!=0:
                        defense_smart.append(i-1)
                if tab[i][j]==tab[i+1][j+1]:
                    if tab[i-1][j-1]==0 and tab[i-1][j]!=0:
                        defense_smart.append(i-1)
                    if tab[i+2][j+2]==0 and tab[i+2][j+3]!=0:
                        defense_smart.append(i+2)
                if tab[i][j]==tab[i-1][j+1]:
                    if tab[i-2][j+2]==0 and tab[i-2][j+3]!=0:
                        defense_smart.append(i-2)
                    if tab[i+1][j-1]==0 and tab[i+1][j]!=0:
                        defense_smart.append(i+1)
    for i in range (3,N-1):
        for j in range (0,N-4):
            if tab[i][j]!=0:
                if tab[i-2][j+2]==tab[i][j]:
                    if tab[i-1][j+1]==0 and tab[i-1][j+2]!=0:
                        defense_smart.append(i-1)
    for i in range (1,N-3):
        for j in range (0,N-2):
            if tab[i][j]!=0:               
                if tab[i][j]==tab[i+2][j+2]:
                    if tab[i+1][j+1]==0 and tab[i+1][j+2]!=0:
                        defense_smart.append(i+1)
    for i in range (1,N-1):
        for j in range (0,N-2):
            if tab[i][j]!=0:    
                if tab[i][j]==tab[i][j+1]:
                    if tab[i][j-1]==0:
                        defense_smart.append(i)
    attaque=[]     
    for i in range (1,N-1):
        for j in range (0,N-2):
            if tab[i][j]!=0:
                if tab[i][j]==j_:
                    if tab[i+1][j]==0 and tab[i+1][j+1]!=0:
                        attaque.append(i+1)
                    if tab[i-1][j]==0 and tab[i-1][j+1]!=0:
                        attaque.append(i-1)
    for i in range (1,N-1):
        for j in range (1,N-2):
            if tab[i][j]!=0:
                if tab[i][j]==j_:
                    if tab[i][j]==0 and tab[i][j-1]==0:
                        attaque.append(i)
                        
    
         
    for i in range (1,N-3):
        for j in range (0,N-3):
            if tab[i][j]!=0:
                if tab[i][j]==tab[i+1][j]==tab[i+2][j]==1:
                    if tab[i+3][j]==0 and tab[i+3][j+2]!=0:
                        while i+3 in defense_smart:
                            defense_smart.remove(i+3)
                        while i+3 in attaque:
                            attaque.remove(i+3)
                    if tab[i-1][j]==0 and tab[i-1][j+2]!=0:
                        while i-1 in defense_smart:
                            defense_smart.remove(i-1)
                        while i-1 in attaque:
                            attaque.remove(i-1)
                if tab[i][j]==tab[i+1][j]==tab[i+3][j]==1:
                    if tab[i+2][j]==0 and tab[i+2][j+2]!=0:
                        while i+2 in defense_smart:
                            defense_smart.remove(i+2)
                        while i+2 in attaque:
                            attaque.remove(i+2)
                if tab[i][j]==tab[i+2][j]==tab[i+3][j]==1:
                    if tab[i+1][j]==0 and tab[i+1][j+2]!=0:
                        while i+1 in defense_smart:
                            defense_smart.remove(i+1)
                        while i+1 in attaque:
                            attaque.remove(i+1)
    for i in range (1,N-3):
        for j in range (0,N-5):
            if tab[i][j]!=0:               
                if tab[i][j]==tab[i+1][j+1]==tab[i+2][j+2]==1:
                    if tab[i+3][j+3]==0 and tab[i+3][j+5]!=0:
                        while i+3 in defense_smart:
                            defense_smart.remove(i+3)
                        while i+3 in attaque:
                            attaque.remove(i+3)
                    if tab[i-1][j-1]==0 and tab[i-1][j]!=0:
                        while i-1 in defense_smart:
                            defense_smart.remove(i-1)
                        while i-1 in attaque:
                            attaque.remove(i-1)
                if tab[i][j]==tab[i+1][j+1]==tab[i+3][j+3]==1:
                    if tab[i+2][j+2]==0 and tab[i+2][j+4]!=0:
                        while i+2 in defense_smart:
                            defense_smart.remove(i+2)
                        while i+2 in attaque:
                            attaque.remove(i+2)
                if tab[i][j]==tab[i+2][j+2]==tab[i+3][j+3]==1:
                    if tab[i+1][j+1]==0 and tab[i+1][j+3]!=0:
                        while i+1 in defense_smart:
                            defense_smart.remove(i+1)
                        while i+1 in attaque:
                            attaque.remove(i+1)
    for i in range (3,N-1):
        for j in range (0,N-4):
            if tab[i][j]!=0:
                if tab[i-2][j+2]==tab[i-1][j+1]==tab[i][j]==1:
                    if tab[i+1][j-1]==0 and tab[i+1][j+1]!=0:
                        while i+1 in defense_smart:
                            defense_smart.remove(i+1)
                        while i+1 in attaque:
                            attaque.remove(i+1)
                if tab[i][j]==tab[i-1][j+1]==tab[i-3][j+3]==1:
                    if tab[i-2][j+2]==0 and tab[i-2][j+4]!=0:
                        while i-2 in defense_smart:
                            defense_smart.remove(i-2)
                        while i-2 in attaque:
                            attaque.remove(i-2)
                if tab[i][j]==tab[i-2][j+2]==tab[i-3][j+3]==1:
                    if tab[i-1][j+1]==0 and tab[i-1][j+3]!=0:
                        while i-1 in defense_smart:
                            defense_smart.remove(i-1)
                        while i-1 in attaque:
                            attaque.remove(i-1)  
    for i in range (3,N-1):
        for j in range (0,N-5):
            if tab[i][j]!=0:
                if tab[i-2][j+2]==tab[i-1][j+1]==tab[i][j]==1:
                    if tab[i-3][j+3]==0 and tab[i-3][j+5]!=0:
                        while i-3 in defense_smart:
                            defense_smart.remove(i-3)
                        while i-3 in attaque:
                            attaque.remove(i-3)
                     
    reste=[]
    for i in range (1,N-1):
        reste.append(i)
    if gagne:
        a=rd.choice(gagne)
    elif defense_smart:
        a=rd.choice(defense_smart)
    elif attaque:
        a=rd.choice(attaque)
    elif place:
        a=rd.choice(place)
    else:
        a=rd.randint(2,6)
            

    y=0
    tab2=np.zeros((N,N))
    for i in range (0,N):
        tab2[i][N-1]=3
        tab2[i][N-2]=3
        tab2[0][i]=3
        tab2[N-1][i]=3
    sumtab=0
    sumtab2=0
    for (i,j), val in np.ndenumerate(tab):
        tab2[i][j]=tab[i][j]
        sumtab+=tab[i][j]
        sumtab2+=tab2[i][j]
    while sumtab==sumtab2:
        if tab[a][y+1]==0:
            while tab[a][y+1]==0:
                y=y+1
                if tab[a][y+1]!=0:
                    tab[a][y]=j_
                    sumtab+=tab[a][y]
                else:
                    if gagne:
                        a=rd.choice(gagne)
                    elif defense_smart:
                        a=rd.choice(defense_smart)
                    elif attaque:
                        a=rd.choice(attaque)
                    elif place:
                        a=rd.choice(place)
                        place.remove(a)
                    elif reste:
                        a=rd.choice(reste)
                        reste.remove(a)
                    else:
                        stop=True
                        break
        else:
            if tab[a][y]==0:
                tab[a][y]=j_
                sumtab+=tab[a][y]
            else:
                if gagne:
                    a=rd.choice(gagne)
                elif defense_smart:
                    a=rd.choice(defense_smart)
                elif attaque:
                    a=rd.choice(attaque)
                elif place:
                    a=rd.choice(place)
                    place.remove(a)
                elif reste:
                    a=rd.choice(reste)
                    reste.remove(a)
                else:
                    stop=True
                    break
        if stop:
            break
    print(gagne)
    print(defense_smart)
    print(attaque)
    print(place)
    return(tab,stop)

#%% Utility functions for AI
def niv8(N, tab, j_):
    stop = False

    def score_position(tab, joueur):
        score = 0
        # Évaluation horizontale
        for r in range(N):
            row_array = [int(i) for i in list(tab[r])]
            for c in range(N-3):
                window = row_array[c:c+4]
                score += evaluate_window(window, joueur)
        
        # Évaluation verticale
        for c in range(N):
            col_array = [int(tab[r][c]) for r in range(N)]
            for r in range(N-3):
                window = col_array[r:r+4]
                score += evaluate_window(window, joueur)
        
        # Évaluation diagonale positive
        for r in range(N-3):
            for c in range(N-3):
                window = [tab[r+i][c+i] for i in range(4)]
                score += evaluate_window(window, joueur)
        
        # Évaluation diagonale négative
        for r in range(N-3):
            for c in range(N-3):
                window = [tab[r+3-i][c+i] for i in range(4)]
                score += evaluate_window(window, joueur)
        
        return score

    def evaluate_window(window, joueur):
        score = 0
        opponent = 1 if joueur == 2 else 2
        
        if window.count(joueur) == 4:
            score += 100
        elif window.count(joueur) == 3 and window.count(0) == 1:
            score += 5
        elif window.count(joueur) == 2 and window.count(0) == 2:
            score += 2

        if window.count(opponent) == 3 and window.count(0) == 1:
            score -= 4

        return score

    def is_valid_location(tab, col):
        return tab[col][0] == 0

    def get_next_open_row(tab, col):
        for r in range(N-1, -1, -1):
            if tab[col][r] == 0:
                return r

    def minimax(tab, depth, alpha, beta, maximizingPlayer):
        valid_locations = [c for c in range(1, N-1) if is_valid_location(tab, c)]
        is_terminal = len(valid_locations) == 0
        if depth == 0 or is_terminal:
            if is_terminal:
                return (None, 100000000000000 if maximizingPlayer else -10000000000000)
            else:
                return (None, score_position(tab, j_ if maximizingPlayer else (1 if j_ == 2 else 2)))
        
        if maximizingPlayer:
            value = -float('inf')
            column = rd.choice(valid_locations)
            for col in valid_locations:
                row = get_next_open_row(tab, col)
                b_copy = tab.copy()
                b_copy[col][row] = j_
                new_score = minimax(b_copy, depth-1, alpha, beta, False)[1]
                if new_score > value:
                    value = new_score
                    column = col
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
            return column, value

        else:  # Minimizing player
            value = float('inf')
            column = rd.choice(valid_locations)
            for col in valid_locations:
                row = get_next_open_row(tab, col)
                b_copy = tab.copy()
                b_copy[col][row] = 1 if j_ == 2 else 2
                new_score = minimax(b_copy, depth-1, alpha, beta, True)[1]
                if new_score < value:
                    value = new_score
                    column = col
                beta = min(beta, value)
                if alpha >= beta:
                    break
            return column, value

    col, minimax_score = minimax(tab, 4, -float('inf'), float('inf'), True)
    
    if is_valid_location(tab, col):
        row = get_next_open_row(tab, col)
        tab[col][row] = j_

    return tab, stop
