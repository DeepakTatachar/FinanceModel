from baseModel import BaseModel

class realEstateModel(BaseModel):
    def __init__(self,
                 name,
                 mortgage,
                 roi=0.03,
                 sale_comm=0.03,
                 sale_tax=0.15,
                 sale_year=5,
                 self_rent_period=3,
                 exp_rent=1200,
                 inflation=0.02,
                 occupancy_rate=0.8):

            self.name = name
            self.mortgage = mortgage
            self.roi = roi
            self.sale_comm = sale_comm
            self.sale_tax = sale_tax
            self.sale_year = sale_year
            self.self_rent_period = self_rent_period * 12
            self.exp_rent = exp_rent
            self.inflation = inflation
            self.monthly_roi = self.get_monthly_rate_for_annual_rate(self.roi)
            self.occupancy_rate = occupancy_rate

    def get_assets_for_month(self, month):
        '''
        returns the interest rate for a given month
        '''
        property_value = self.mortgage.total_amount * ((1 + self.monthly_roi) ** month)
        assets = property_value

        if(month > self.self_rent_period):
            rent_out_period = month - self.self_rent_period
            assets = assets  + self.exp_rent * rent_out_period * self.occupancy_rate
            
        return assets

    def get_liability_for_month(self, month):
        '''
        returns the interest rate for a given month
        '''
        liability = (self.mortgage.emi + self.mortgage.misc_emi) * month   + self.mortgage.one_time
        outstanding_principal = self.mortgage.principal
        
        for i in range(month):
            pr, ir = self.mortgage.get_amortization_for_payment(i + 1)
            outstanding_principal = outstanding_principal - pr

        liability = liability + outstanding_principal
        return liability
        