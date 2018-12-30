#! python3

#link to challenge: https://www.reddit.com/r/dailyprogrammer/comments/6jr76h/20170627_challenge_321_easy_talking_clock/?ref=share&ref_source=link

from num2words import num2words
from time  import strftime

hours = []

hour = int(strftime("%I"))
minute = int(strftime("%M"))
amPm = strftime("%p")

if int(minute) <= 10:
    print(num2words(hour) + " oh" + num2words(minute) + "  " + amPm)
else:
    print(num2words(hour) + " " + num2words(minute) + " " + amPm)
