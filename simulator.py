class Simulator():
    def __init__(self, model1, model2):
        self.model1 = model1
        self.model2 = model2
    
    def run(self, months):
        for month in range(months):
            assets1 = self.model1.get_assets_for_month(month)
            liability1 = self.model1.get_liability_for_month(month)

            assets2 = self.model2.get_assets_for_month(month)
            liability2 = self.model2.get_liability_for_month(month)
            print("Month: {} Assets {}: ${:.2f}  Liability {}: $ {:.2f} |  Assets {}: ${:.2f}  Liability {}: ${:.2f}".format(month,
                                                                                                                                self.model1.name,
                                                                                                                                assets1,
                                                                                                                                self.model1.name, 
                                                                                                                                liability1,
                                                                                                                                self.model2.name,
                                                                                                                                assets2,
                                                                                                                                self.model2.name,
                                                                                                                                liability2))
            

        gain1 = assets1 - liability1
        gain2 = assets2 - liability2
        print("Net Gain {} : ${:.2f}   \t {} : ${:.2f}".format(self.model1.name, gain1, self.model2.name, gain2))
        print("Diff Real Estate - Stock Market Performance: ${:.2f}".format(gain1 - gain2))