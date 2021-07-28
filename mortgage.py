class Mortgage():
    def __init__(self, 
                 downpayment, 
                 intr_rate, 
                 total_amount,
                 years,
                 one_time=5800,
                 misc_emi=310):

        self.downpayment = downpayment * total_amount
        self.rate = intr_rate
        self.principal = total_amount - self.downpayment
        self.compouding_period = 12
        self.years = years
        self.n = self.years * 12
        self.rate = intr_rate
        self.monthly_rate = self.rate / 12
        self.emi = self.get_emi()
        self.total_amount = total_amount
        self.misc_emi = misc_emi
        self.one_time = one_time

    def get_emi(self):
        '''
            Return periodic payment
        '''
        emi = self.principal * self.monthly_rate * ( (1 + self.monthly_rate) ** self.n ) / ( (1 + self.monthly_rate) ** self.n - 1)
        print(emi)
        return emi

    def get_amortization_for_payment(self, payment):
        '''
        returns the amortization for a given payment
        see # https://www.mortgagesanalyzed.com/gyan/finance/maths/calculating-amortization-schedule
        '''
        balance = self.principal
        principal_contribution = 0
        interest_contribution = None
        for i in range(payment):
            interest_contribution = balance * self.monthly_rate
            new_bal = balance + interest_contribution
            balance = new_bal - self.emi
            principal_contribution = self.emi - interest_contribution

        return principal_contribution, interest_contribution