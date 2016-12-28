# Guess a number

from random import randint

print('-------------------------')
print('    GUESS \'LE NUMBER\'')
print('-------------------------')

def guess():
    myRand = randint(0,100)
    guess  = -1
    tries  = 0
    
    while myRand != guess:
        guess_s = input("Your guess: ")
        guess = int(guess_s)
    
        if guess < myRand:
            print("Your guess {} is low".format(guess_s))
        elif guess > myRand:
            print("Your guess {} is hi ".format(guess_s))
        else:
            print()
        tries += 1
            
    print ("Got it! It was {}. It took you {} tries.".format(myRand,tries))

    
guess()    
