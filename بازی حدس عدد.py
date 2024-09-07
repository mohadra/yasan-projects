from sys import *
from random import *


print()
print("             * * * * * * * * * * * * * *")
print("             *      Guess a number     *")
print("             *         between         *")
print("             *        10 and 99        *")
print("             * * * * * * * * * * * * * *")
print()

n = 6
 
print()
print("             * * * * * * * * * * * * * *")
print("             *       You have :",n,"     *")
print("             *         Chances         *")
print("             * * * * * * * * * * * * * *")
print()
  
number = randint(10, 99)

for i in range(n,0,-1):
    guess_number = int(input("             Enter your guess : "))
    print()
    if guess_number == number:
        print("             Congratulations You Win ! :)")
        exit()
    elif guess_number < number:
        print("             My number is greater than " ,guess_number," !  You have ",i-1,"other chances")
    else:
        print("             My number is lower than ",guess_number," !  You have ",i-1,"other chances")
        
print("             You Lose ! :(")
print("             My Number is ",number)
