'''
Prints the liability and assets after each month of all the models
Observers the simulator and prints the results 
'''
from observers.baseObserver import BaseObserver
import matplotlib.pyplot as plt
import numpy as np

class GraphObserver(BaseObserver):
    '''
    Prints the liability and assets after each month of all the models
    '''
    def __init__(self):
        super().__init__()
        self.string_format = " {} Assets: ${:.2f}\t - Liability: ${:.2f}\t"
        self.gain_format = "  {} Gains: ${:.2f}\t\t\t\t\t"

    def notify(self, models, assets, liabilities, month):
        max_month = assets.shape[1] - 1
        if(month < max_month):
            return

        gains = assets - liabilities
        months = np.arange(max_month + 1)
        for model_idx, model in enumerate(models):
            plt.plot(months, gains[model_idx], label=model.name)

        plt.legend(loc='upper left')
        plt.show()



