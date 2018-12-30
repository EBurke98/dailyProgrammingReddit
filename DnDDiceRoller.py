#! python3

#Link:  https://www.reddit.com/r/dailyprogrammer/comments/8s0cy1/20180618_challenge_364_easy_create_a_dice_roller/?ref=share&ref_source=link

import random

dice = input("input dices to be rolled:")

getNum= dice.split('d')

total = 0

for DiceNum in range(0, int(getNum[0])):
    total += random.randint(1, int(getNum[1]))
 
print(total) 
