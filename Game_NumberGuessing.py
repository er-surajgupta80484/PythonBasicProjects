'''Rule: This Game is to guess a number. You need to provide lower and upper number and then you are required to guess a number between those.'''

import random #to use random function
import math #to use log funtion to get number of chances a user must be having to play the game
print(__doc__)
lower=int(input("Enter Lower Bound : "))
upper=int(input("Enter Upper Bound : "))
random_num=random.randint(lower,upper) #get a random number between lower and upper number
chances=round(math.log(upper-lower+1,2))
#log base 2 in mathematics will help you calculate the log2 means a binary number system. How it works
#upper is 100, lower is 1. formula: upper-lower+1 which is 100-1+1 = 100 and ,2 means log base 2. so if u calculate log base 2 (100) = 6.64 and round off would be 7 as we need integer.
#chances cant be in decimals.
print(f"You have {chances} guess available")   #display number of chances

count=0  #counter to count number of tries
while(chances>0):  #start a loop until chances(life in a game) become 0
    count+=1
    guess = int(input(f"Guess {count} number : "))
    chances-=1  #reduce number of chances by 1 after each guess
    if (guess == random_num):
        print(f"Congratulations, You won the game in {count} try")
        break
    elif(guess>random_num):
        print(f"You guessed a bigger number, Try Again\nRemaining chances are {chances}")
    elif(guess<random_num):
        print(f"You guessed a smaller number, Try Again\nRemaining chances are {chances}")
print(f"You Lost All {count} guesses were wrong")