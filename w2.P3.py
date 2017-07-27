# Test Case 1:
# The following variables contain values as described below:
# balance - the outstanding balance on the credit card
# annualInterestRate - annual interest rate as a decimal+

import math

balance = 320000
annualInterestRate = 0.2

# aprxmonthlypay = int(round(totalpay/12, 0))             #increased divider from 12->14 so we start with a lesser aprxmonthlypay value and adjust from there
totaliter = 0


monthlyint = annualInterestRate/12


LB = balance / 12
totalint = pow(1+monthlyint,12)
UB = round(balance * (pow(1+monthlyint,12)/12),2)

aprxmonthlypay = (LB + UB) / 2
print('STARTING WITH aprxmonthlypay: ' +str(aprxmonthlypay))
aprxmonthlypay = round(aprxmonthlypay, 2)

print('totalint: ' +str(totalint))
print('STARTING WITH aprxmonthlypay: ' +str(aprxmonthlypay))
print('LB: ' +str(LB))
print('UB: ' +str(UB))
#x = input("are you ready?")

wait = ''
wait = input('PRESS ENTER TO CONTINUE.')


while aprxmonthlypay > 0:
    iterbalance = balance

    for i in range(1,13):
        totaliter += 1
        iterbalance -= aprxmonthlypay
        iterbalance = iterbalance + (annualInterestRate / 12) * iterbalance
        print("Month " + str(i) + " remaining balance is = " + "%.2f" % iterbalance)

    if iterbalance < -0.01:         #the 12th month payment will result in a negative balance (ie. the balance is OVERPAID) iterbalance + aprxmonthlypay < 0 or
        UB = aprxmonthlypay
        aprxmonthlypay = (LB + UB) / 2
        print("balance is OVERPAID. New monthly pay is: " + str(aprxmonthlypay) + " within range: " + str(LB) + " and " + str(UB))
        #wait = input('PRESS ENTER TO CONTINUE.')

    elif iterbalance > 0.01:       #UNDERPAID it1erbalance - aprxmonthlypay > 0 or
        LB = aprxmonthlypay
        aprxmonthlypay = (LB + UB) / 2
        print("balance is UNDERPAID. New monthly pay is: " + str(aprxmonthlypay) + " within range: " + str(LB) + " and " + str(UB))
        #wait = input('PRESS ENTER TO CONTINUE.')

    else:
        #wait = input('breaking')
        break

if iterbalance > aprxmonthlypay:        #FINAL ADJUSTMENT: IF PAYMENT dropped PAST paying BALANCE in full AND NOW IT IS UNDERPAID, EXECUTES ONLY ONCE
    print("Final adjustment needed, increasing monthpay from: " + str(aprxmonthlypay) + " to " + str(aprxmonthlypay + 10))
    aprxmonthlypay += .10
    print("Lowest Payment: " + str(aprxmonthlypay))
elif aprxmonthlypay == 0:                  #cannot make zero payments...
    aprxmonthlypay += .10
    print("Lowest Payment: " + str(aprxmonthlypay))
elif iterbalance > 0:                         #cannot leave positive balance
    aprxmonthlypay += .10
    print("Lowest Payment: " + str(aprxmonthlypay))
else:
    print("Lowest Payment: " + str(aprxmonthlypay))

print(str(totaliter/12) + " # of iterations")

#totalint += (annualInterestRate/12)*balance

#print("Remaining balance: " + "%.2f" % iterbalance)