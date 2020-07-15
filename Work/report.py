# report.py
import csv

def read_portfolio(filename):
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            record = dict(zip(headers, row))
            stock = {'name': record['name'], 'shares': int(record['shares']),
                     'price': float(record['price'])}
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


port = read_portfolio('Data/portfoliodate.csv')
prices = read_prices('Data/prices.csv')

total_cost = 0.0
for stock in port:
    total_cost += stock['shares'] * stock['price']


total_value = 0.0
for stock in port:
    total_value += stock['shares'] * prices[stock['name']]

gain = total_value - total_cost

print('The current portfolio is valued at {:.2f}, with a current '
      'gain(loss) of {:.2f}'.format(total_value, gain))

def mk_report(portfolio, prices):
    report = []
    for stock in portfolio:
        r = (stock['name'], stock['shares'], prices[stock['name']],
             prices[stock['name']]- stock['price'])
        report.append(r)
    return report

report = mk_report(port, prices)
headers = ('Name', 'Shares', 'Price', 'Change')
print('%10s %10s %10s %10s' % headers)
print(('-' * 10 + ' ') * len(headers))

for r in report:
    print('%10s %10d %10.2f %10.2f' % r)

