# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 11:28:38 2018

@author: Anonymousgod
"""

#guess ny number
#
#the computer picks a random number between 1 and 100
#the player tries to guess it and the computer lets
#the player know if the guess is too high, too low
#or right on the money

import random
print "\tWelcome to 'Guess My Number'!"
print "\nI'm thinking of a number between 1 and 10."
print "Try to guess it in as few attempts as posible.\n"

#set the initial values
the_number =  random.randrange(10) + 1
guess = int(raw_input("Take a guess: "))
tries = 1

#guessing loop
while (guess != the_number):
  if (guess > the_number):
    print "Lower..."
  else:
    print "Higher..."

  guess = int(raw_input("Take a guess: "))
  tries += 1

while (guess == the_number):
  print "You guessed it! The number was", the_number
  print "And it only took", tries, "tries!\n"
  
if tries > 5:
        print "Too bad. You tried one too many times." 
        print "The number was", the_number


raw_input("\n\nPress the enter to exit.")
