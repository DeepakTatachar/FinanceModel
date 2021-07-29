'''
Prints the liability and assets after each month of all the models
Observers the simulator and prints the results 
'''
from observers.baseObserver import BaseObserver

class PrintObserver(BaseObserver):
    '''
    Prints the liability and assets after each month of all the models
    '''
    def __init__(self):
        super().__init__()
        self.string_format = " {} Assets: ${:.2f}\t - Liability: ${:.2f}\t"
        self.gain_format = "  {} Gains: ${:.2f}\t\t\t\t\t"

    def notify(self, models, assets, liabilities, month):
        print_string = "{}: -> \t".format(month)
        for model_idx, model in enumerate(models):
            print_string += self.string_format.format(model.name, assets[model_idx, month], liabilities[model_idx, month])

        print(print_string)

        gain_string = "{}: -> \t".format(month)
        gains = assets[:, month] - liabilities[:, month]
        for model_idx, model in enumerate(models):
            gain_string += self.gain_format.format(model.name, gains[model_idx])

        print(gain_string)

