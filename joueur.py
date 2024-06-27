import numpy as np
import matplotlib.pyplot as plt
import random as rd

class Joueur(objet):
    def __init__(self, name, id):
        super().__init__()
        self.name = name
        self.id = id

    def action(self, state):
        return state
    
class Joueur_niv0(Joueur):
    def __init__(self, name, id):
        super().__init__(name, id)

    def action(self, state):
        old_state = state.copy()
        
        n = state.shape[1]
        possibilites = np.linspace(1, n-2)
        choice = rd.choice(possibilites)
        
        while np.all(old_state == state):
            zero_indices = np.where(state[choice] == 0)[0]
            # Check if there are any zeros in the array
            if zero_indices.size == 0:
                possibilites.remove(choice)
                if possibilites.size == 0:
                    return state
                else:
                    choice = rd.choice(possibilites)
            else:
                state[choice][zero_indices[-1]] = self.id
                return state
        