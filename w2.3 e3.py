high = 100
low = 0
answer = ''

guess = 50

print('Please think of a number between 0 and 100!')

while answer != 'c':
    print('Is your secret number ' + str(guess) + '?')
    #answer = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    answer = input("Enter 'h' to indicate the guess is too high. \n"
                    "Enter 'l' to indicate the guess is too low. \n"
                    "Enter 'c' to indicate I guessed correctly.")

    if answer == 'h':
        high = guess
        guess = round((high+low)//2,0)

    elif answer == 'l':
        low = guess
        guess = round((high+low)//2)

    elif answer == 'c':
        print('Game over. Your secret number was: ' + str(guess))

    else:
        print('Sorry, I did not understand your input.')
