price = 1000000

has_good_credit = False

if has_good_credit:
    down_payment = 0.10 * price
else:
    down_payment = 0.20 * price
print(f"Down Payment: ${down_payment}")
