# report.py
import csv
# Exercise 3.12
import fileparse


# Exercise 2.4
def read_portfolio(filename):
    """
    Program to read a stock portfolio contained in a .csv file.
    Selects columns 'name', 'shares', and 'price' and converts
    them respectively to date types str, int, and float.
    """
    return fileparse.parse_csv(filename, select=['name', 'shares', 'price'], types=[str, int, float])


# Exercise 2.6
def read_prices(filename_prices):
    """
    Program to read stock prices from a .csv file.
    """
    return dict(fileparse.parse_csv(filename_prices, types=[str, float], has_headers=False))


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


# Exercise 2.9 / 3.1-3.2
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


# Exercise 3.15. This is not exactly how it is done in the solutions because using the solutions, there is no data type
# conversion completed and therefore everything in portfolio.csv and prices.csv is a string. So, I ran the
# read_portfolio and read_prices on arg[1] and arg[2], respectively, first and passed their outputs into
# portfolio_report.

# Exercise 3.15
def main(args):
    if len(args) != 3:
        raise SystemExit('Usage: %s portfile pricefile' % args[0])
    port = read_portfolio(args[1])
    prices = read_prices(args[2])
    portfolio_report(port, prices)

# Exercise 3.16
if __name__ == '__main__':
    import sys
    main(sys.argv)
