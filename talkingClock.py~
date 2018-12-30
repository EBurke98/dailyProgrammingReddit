#! python3

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
