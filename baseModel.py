from abc import ABC

class BaseModel(ABC):
    def __init__(self):
        pass

    def get_assets_for_month(self, month):
        '''
        returns the interest rate for a given month
        '''
        pass

    def get_liability_for_month(self, month):
        '''
        returns the interest rate for a given month
        '''
        pass

    def get_monthly_rate_for_annual_rate(self, annual_rate):
        '''
        returns the monthly compund rate for an annual rate
        '''
        monthly_rate = (1 + annual_rate) ** (1 / 12) - 1
        return monthly_rate