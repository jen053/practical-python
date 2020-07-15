# pcost.py
import os
import csv
import numpy as np


def portfolio_value(filename):
    """
    Function to calculate the total portfolio value.
    Input of type string defining a file location.
    File at file location of the form nx3 (stock name,
    stock price, total shares owned),                                                                                                                              n being the number of stocks within the profile
	"""

    f = open(filename)
    rows = csv.reader(f)
    headers = next(rows)
    total_cost = 0.0
    record = []
    for rowno, row in enumerate(rows, start=1):
        r = dict(zip(headers, row))
        try:
            nshares = int(r['shares'])
            price = float(r['price'])
            total_cost += nshares * price
        except ValueError:
            print(f'Row {rowno}: Bad row: {row}')
        record.append(r)
    print('Total portfolio valued at ${}'.format(total_cost))
    f.close()

    return total_cost, record


cost, record = portfolio_value('Data/portfoliodate.csv')

print(cost)
print(record)
# Exercise 1.27
