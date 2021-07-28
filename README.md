# Finance Model

Code models two investment strategies
1) Buy real estate
2) Invest in the stock market

Supports a bunch of paramters (does not model inflation) to compare (1) with (2)

* (1) Is modelled in realEstate.py
* (2) Is modelled in stockMarket.py
* 30-year fixed interest rate is modelled in mortgage.py
* compare.py compares the two options and has a buch of paramters that can be set

How to run?
------------
set the parameters in compare.py and use the following command
```
python compare.py
```

The output looks something like this
```
663.8279633217539
Month: 0 Assets Real Estate: $ 200000.00  Liability Real Estate: $ 165800.00 |  Assets Stock Market: $ 45800.00  Liability Stock Market: $ 0.00
Month: 1 Assets Real Estate: $ 200493.25  Liability Real Estate: $ 166493.33 |  Assets Stock Market: $ 46165.22  Liability Stock Market: $ 1350.00
Month: 2 Assets Real Estate: $ 200987.72  Liability Real Estate: $ 167185.99 |  Assets Stock Market: $ 46533.34  Liability Stock Market: $ 2700.00
Month: 3 Assets Real Estate: $ 201483.41  Liability Real Estate: $ 167877.98 |  Assets Stock Market: $ 46904.41  Liability Stock Market: $ 4050.00
.....
.....
.....
Month: 59 Assets Real Estate: $ 260684.41  Liability Real Estate: $ 205502.70 |  Assets Stock Market: $ 73177.83  Liability Stock Market: $ 32400.00
Net Gain Real Estate :$ 55181.71   	 Stock Market : 40777.83
Diff Real - Stock: $14403.88
```

The first line is the calculated EMI per month excluding tax and hazardous insurance (to add this set the mortgage.misc_emi parameter)
