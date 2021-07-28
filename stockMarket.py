from baseModel import BaseModel

class stockMarketModel(BaseModel):
    def __init__(self,
                 name,
                 init_capital,
                 roi=0.1,
                 sale_tax=0.3,
                 sale_year=5,
                 rent_years=3,
                 rent=1350):
        '''
        Initializes the model with the given parameters
        '''

        self.name = name
        self.init_capital = init_capital
        self.roi = roi
        self.monthly_roi = self.get_monthly_rate_for_annual_rate(self.roi)
        self.rent_years = rent_years
        self.rent = rent


    def get_assets_for_month(self, month):
        '''
        returns the interest rate for a given month
        '''
        assets = self.init_capital * ((1 + self.monthly_roi) ** month)          
        return assets

    def get_liability_for_month(self, month):
        '''
        returns the interest rate for a given month
        '''
        liability = 0
        if(month < self.rent_years * 12):
            liability = self.rent * month
        else:
            liability = self.rent * (self.rent_years * 12)
        
        return liability