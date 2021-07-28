from realEstate import realEstateModel
from mortgage import Mortgage
from stockMarket import stockMarketModel
from simulator import Simulator

'''
How many years to model?
'''
sim_years = 5

'''
What is the percentage of the downpayemnt?
'''
downpayment = 0.2

'''
What is the downpayement amount
'''
down_pay = 40000
total = down_pay / downpayment

'''
What is the yearly rate for the mortgage?
'''
intr_rate = 0.02875
years = 30

'''
One time costs associated with the mortgage, such as bank fees, etc.
'''
one_time_costs = 5800

'''
What is the miscaleanous cost of the mortgage that does not go towards the mortgage?
For example tax and hazardous insurance
'''
misc_emi = 310

'''
If you were to rent out the house what is the expected rent?
'''
expted_house_rent = 1200

'''
How much rent are saving when you stay in the house
'''
self_rent = 1350

'''
Paramter sets how many years do you plan on staying in the house
FOr example if sim_years = 5, and self_rent_years = 3, 
then you will be stay in the house for 3 years, but will own the house for 5 years
'''
self_rent_years = 3

'''
Expected annual return on the investment for the house 
'''
real_estate_roi = 0.03


'''
Expected annual return on the investment for the stock market
'''
stock_market_roi = 0.1


'''
If you are renting out the house, what percentage of the time is it likely to be occupied?
'''
rent_occupancy_rate = 0.7

'''
Rent's inflation rate
'''
rent_inflation = 0.02

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
                               roi=stock_market_roi,
                               rent_inflation_rate=rent_inflation)

simulator = Simulator(realEstate, stockMarket)
simulator.run(months=(sim_years*12))
