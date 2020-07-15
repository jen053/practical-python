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
    prices = []
    shares = []
    for rowno, row in enumerate(rows, start=1):
        try:
            prices.append(float(row[1]))
            shares.append(float(row[2]))
        except ValueError:
            print(f'Row {rowno}: Bad row: {row}')

    prices_array = np.array(prices)
    shares_array = np.array(shares)
    values_array = prices_array * shares_array
    total_value = np.sum(values_array)
    print('Total portfolio valued at ${}'.format(total_value))
    f.close()

    return total_value


print(portfolio_value('Data/missing.csv'))
# Exercise 1.27
