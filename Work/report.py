# report.py
import csv

# Exercise 2.4
def read_portfolio(filename):
    """
    Program to read a stock portfolio contained in a .csv file of any format.
    """
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            # Exercise 2.16
            record = dict(zip(headers, row))
            stock = {'name': record['name'], 'shares': int(record['shares']),
                     'price': float(record['price'])}
            portfolio.append(stock)

    return portfolio

# Exercise 2.6
def read_prices(filename_prices):
    """
    Program to read stock prices from a .csv file of any format.
    """
    prices = {}
    f = open(filename_prices, 'r')
    rows = csv.reader(f)
    for row in rows:
        try:
            prices[row[0]] = float(row[1])
        except IndexError:
            pass

    return prices

# Exercise 2.7
def cost_value_gain(portfolio, prices):
    """
    Function that provides cost, value and gain for a given portfolio.
    """
    total_value = 0.0
    total_cost = 0.0

    for stock in port:
        total_cost += stock['shares'] * stock['price']
    for stock in port:
        total_value += stock['shares'] * prices[stock['name']]

    gain = total_value - total_cost

    print('The current portfolio is valued at {:.2f}, with a current '
          'gain(loss) of {:.2f}'.format(total_value, gain))

    return gain, total_value, total_cost

# Exercise 2.9
def portfolio_report(portfolio, prices):
    """
    Program to take a given stock portfolio and prices to produce and print a report
    """
    report = []

    for stock in portfolio:
        r = (stock['name'], stock['shares'], prices[stock['name']],
             prices[stock['name']] - stock['price'])
        report.append(r)
    # Exercise 2.10 - 2.11
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)
    print(('-' * 10 + ' ') * len(headers))

    for r in report:
        print('%10s %10d %10.2f %10.2f' % r)

    return report


port = read_portfolio('Data/portfoliodate.csv')
prices = read_prices('Data/prices.csv')
curr_gain, curr_value, curr_cost = cost_value_gain(port, prices)
curr_report = portfolio_report(port, prices)
