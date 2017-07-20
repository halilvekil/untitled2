# Test Case 1:
# The following variables contain values as described below:
# balance - the outstanding balance on the credit card
# annualInterestRate - annual interest rate as a decimal+
balance = 33529
annualInterestRate = 0.2

# aprxint = balance * annualInterestRate
# totalpay = balance + aprxint
# aprxmonthlypay = int(round(totalpay/12, 0))             #increased divider from 12->14 so we start with a lesser aprxmonthlypay value and adjust from there
aprxmonthlypay = int(round(balance, 0))                 #removed totalpay, instead just starting with total balance (since not dividing totalpay anymore(for accuracy)
totaliter = 0
print(aprxmonthlypay)
aprxmonthlypay = int(round(aprxmonthlypay, -1))

print(aprxmonthlypay)
while aprxmonthlypay > 0:
    iterbalance = balance
    for i in range(1,13):
        totaliter += 1
        iterbalance -= aprxmonthlypay
        iterbalance = iterbalance + (annualInterestRate / 12) * iterbalance
        print("Month " + str(i) + " remaining balance is = " + "%.2f" % iterbalance)
    if iterbalance + aprxmonthlypay < 0 or iterbalance < -120:         #the 12th month payment will result in a positive balance (ie. the balance is OVERPAID)
        print("Decreasing monthpay from: " + str(aprxmonthlypay) + " to " + str(aprxmonthlypay - 10))
        aprxmonthlypay -= 10
    # elif iterbalance - aprxmonthlypay < 0:      #the 12th month payment will result in a negative balance (ie. the balance is JUST paid)
    #     aprxmonthlypay -= 10
    #     break
    else:
        #aprxmonthlypay -= 10
        break
if iterbalance > aprxmonthlypay:        #FINAL ADJUSTMENT: IF PAYMENT dropped PAST paying BALANCE in full AND NOW IT IS UNDERPAID, EXECUTES ONLY ONCE
    print("Final adjustment needed, increasing monthpay from: " + str(aprxmonthlypay) + " to " + str(aprxmonthlypay + 10))
    aprxmonthlypay += 10
    print("Lowest Payment: " + str(aprxmonthlypay))
elif aprxmonthlypay == 0:                  #cannot make zero payments...
    aprxmonthlypay += 10
    print("Lowest Payment: " + str(aprxmonthlypay))
elif iterbalance > 0:                         #cannot leave positive balance
    aprxmonthlypay += 10
    print("Lowest Payment: " + str(aprxmonthlypay))
else:
    print("Lowest Payment: " + str(aprxmonthlypay))

print(str(totaliter/12) + " # of iterations")

#totalint += (annualInterestRate/12)*balance

#print("Remaining balance: " + "%.2f" % iterbalance)