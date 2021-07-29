import numpy as np

class Simulator():
    def __init__(self, models):
        self.models = models
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)
   
    def run(self, months):
        assets = np.zeros((len(self.models), months))
        liability = np.zeros((len(self.models), months))

        for month in range(months):
            for model_idx, model in enumerate(self.models):
                model_assets = model.get_assets_for_month(month)
                model_liability = model.get_liability_for_month(month)

                assets[model_idx, month] = model_assets
                liability[model_idx, month] = model_liability

            for observer in self.observers:
                observer.notify(self.models, assets, liability, month)
