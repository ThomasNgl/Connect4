import numpy as np
import matplotlib.pyplot as plt
import random as rd

class Tab(objet):
    def __init__(self, n_cases = 7):
        super(objet, self).__init__()
        self.n_cases = n_cases
        self.state = np.zeros((n_cases + 2,n_cases + 2))
        self.state[1:-1, -2:] = 3 * np.ones(self.state[1:-1, -2:].shape)
        self.state[0, :] = 3 * np.ones(self.n_cases)
        self.state[-1, :] = 3 * np.ones(self.n_cases)

    def plot_tab(self):
        fig, ax = plt.subplots(figsize = (self.n_cases+np.sqrt(self.n_cases), 
                                          self.n_cases + np.sqrt(self.n_cases)
                                )
                    )
        # plot is white
        ax.matshow(self.state, cmap='Greys',vmin=0,vmax=0)
        # grid is black 
        ax.set_xticks(np.arange(self.state.shape[0])-.5, minor=True)
        ax.set_yticks(np.arange(self.state.shape[1])-.5, minor=True)
        ax.grid(which='minor',color='black')
        
        ax.tick_params(which='minor',size=0)
        # remove label
        ax.set_xticklabels([])
        ax.set_yticklabels([])
        
        for i in range(0,self.state.shape[0]):
            for j in range(0,self.state.shape[1]):
                if self.state[i][j] == 1:
                    s = 'o'
                    color = 'blue'
                    fontsize = 60
                elif self.stat[i][j] == 2:
                    s = 'o'
                    color = 'red',
                    fontsize = 60
                elif self.stat[i][j]==3:
                    s = '+'
                    color = 'black'
                    fontsize = 120
                if self.stat[i][j] == 0:
                    ax.text(i, j,
                            s, 
                            ha = 'center',va = 'center', 
                            color = color, 
                            fontsize = fontsize
                    )

        plt.show()