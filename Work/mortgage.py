# mortgage.py
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0
month = 0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    month = month + 1
    principal = principal * (1 + rate / 12) - payment
    total_paid = total_paid + payment

    if (month >= extra_payment_start_month) and (month <= extra_payment_end_month):
        principal = principal - extra_payment
        total_paid = total_paid + extra_payment

    if principal < 0:
        total_paid = total_paid + principal
        principal = 0

    print(f'Month: {month}, Principal: ${principal:0.2f}, Total_paid: ${total_paid:0.2f}')


# Exercise 1.7
