#given
#balance
#annualInterestRate: annual interest rate as a decimal
#monthlyPaymentRate: minimum monthly payment rate as a decimal

# Test Case 1:
balance = 42000
annualInterestRate = 0.12
monthlyPaymentRate = 0.02
i = 0
totalint = 0

#while balance > 1000:
for i in range(1,13):
    #i += 1
    minpay = monthlyPaymentRate * balance
    balance -= minpay
    balance = balance + (annualInterestRate/12)*balance
    #totalint += (annualInterestRate/12)*balance

print("Remaining balance: " + "%.2f" % balance)

    #print("Month " + str(i) + " remaining balance is = " + "%.2f" % balance + ", with total interest of: " + "%.2f" % totalint)

