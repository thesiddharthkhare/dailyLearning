# How to take int as an input
# by default it will be string

avail_bal = 150
amount = int(input("Please enter your amount : "))
print("*"*12)

if amount <= avail_bal:
    avail_bal = avail_bal - amount
    print("Transaction processed succesfully")
    print("Balance", avail_bal)
else:
    print("Insufficient balance, dedso rupaye dega")


value = float(input("Please enter your weight: "))
print("Your weight is ", value)