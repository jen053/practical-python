# pcost.py
import csv
# Exercise 3.14
import report


def portfolio_value(filename):
    """
    Function to calculate the total portfolio value.
    Input of type string defining a file location.
    File at file location of the form nx3 (stock name,
    stock price, total shares owned),
    """

    port = report.read_portfolio(filename)
    return sum([s['shares'] * s['price'] for s in port])

# Exercise 3.15
def main(args):
    if len(args) != 2:
        raise SystemExit('Usage: %s portfoliofile' % args[0])
    portfolio_value(args[1])

# Exercise 3.16
if __name__ == '__main__':
    import sys
    main(sys.argv)

cost = portfolio_value('Data/portfoliodate.csv')
print('Total cost: {}'.format(cost))
# Exercise 1.27
