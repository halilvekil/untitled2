x = 23
epsilon = 0.00000001
step = 0.000001
guess = 0.0

while abs(guess**2-x) >= epsilon:
    if guess <= x:
        guess += step
        #print('guess is at ' + str(guess))
        #print('abs(guess**2-x) is at ' + str(abs(guess**2-x)))
    else:
        print('guess is at '+ str(guess))
        break

if abs(guess**2 - x) >= epsilon:
    print('failed')
else:
    print('succeeded: ' + str(guess))
    print('succeeded: ' + str(guess))