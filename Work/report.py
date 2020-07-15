# report.py
import csv


def portfolio_value(filename):
    """Function to calculate the total portfolio value.
    Input of type string defining a file location.
    File at file location of the form nx3 (stock name, stock price, total shares owned),
    n being the number of stocks within the profile
    """
    f = open(filename)
    rows = csv.reader(f)
    headers = next(rows)
    prices = []
    shares = []
    for row in rows:
        prices.append(float(row[1]))
        shares.append(float(row[2]))
    prices_array = np.array(prices)
    shares_array = np.array(shares)
    values_array = prices_array * shares_array
    total_value = np.sum(values_array)
    print('Total portfolio valued at ${}'.format(total_value))
    f.close()

    return total_value


def read_portfolio(filename):
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            stock = dict(name=str(row[0]),
                         shares=int(row[1]), price=float(row[2]))
            portfolio.append(stock)
    return portfolio


def read_prices(filename_prices):
    prices = {}
    f = open(filename_prices, 'r')
    rows = csv.reader(f)
    for row in rows:
        try:
            prices[row[0]] = float(row[1])
        except IndexError:
            pass

    return prices


port = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')

total_cost = 0.0
for stock in port:
    total_cost += stock['shares'] * stock['price']


total_value = 0.0
for stock in port:
    total_value += stock['shares'] * prices[stock['name']]

gain = total_value - total_cost

print('The current portfolio is valued at {}, with a current '
      'gain(loss) of {}'.format(total_value, gain))

