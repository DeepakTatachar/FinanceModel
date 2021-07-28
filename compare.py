from realEstate import realEstateModel
from mortgage import Mortgage
from stockMarket import stockMarketModel

class sim():
    def __init__(self, model1, model2):
        self.model1 = model1
        self.model2 = model2
    
    def run(self, months):
        for month in range(months):
            assets1 = self.model1.get_assets_for_month(month)
            liability1 = self.model1.get_liability_for_month(month)

            assets2 = self.model2.get_assets_for_month(month)
            liability2 = self.model2.get_liability_for_month(month)
            print("Month: {} Assets {}: $ {:.2f}  Liability {}: $ {:.2f} |  Assets {}: $ {:.2f}  Liability {}: $ {:.2f}".format(month,
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
        print("Net Gain {} :$ {:.2f}   \t {} : {:.2f}".format(self.model1.name, gain1, self.model2.name, gain2))
        print("Diff Real - Stock: ${:.2f}".format(gain1 - gain2))

downpayment = 0.2
down_pay = 40000
total = down_pay / downpayment
intr_rate = 0.02875
years = 30
one_time_costs = 5800
expted_house_rent = 1200
self_rent = 1350
self_rent_years = 2
real_estate_roi = 0.03
stock_market_roi = 0.1
rent_occupancy_rate = 0.7

fixed_30_year_mortgage = Mortgage(downpayment=downpayment,
                                  intr_rate=intr_rate,
                                  total_amount=total,
                                  years=years,
                                  one_time=one_time_costs)

inital_capital = fixed_30_year_mortgage.downpayment + fixed_30_year_mortgage.one_time

realEstate = realEstateModel("Real Estate", 
                             fixed_30_year_mortgage,
                             self_rent_period=self_rent_years,
                             exp_rent=expted_house_rent,
                             roi=real_estate_roi,
                             occupancy_rate=rent_occupancy_rate)

stockMarket = stockMarketModel("Stock Market",
                               inital_capital, 
                               rent_years=self_rent_years, 
                               rent=self_rent,
                               roi=stock_market_roi)

simulator = sim(realEstate, stockMarket)
gain = simulator.run(months=(5*12))
