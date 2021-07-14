
from typing import Counter


x = int(input("Please input a number here: "))
count = 0
def numbers_to_words(): 
    digits = { 1:  "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}
    teens = {11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen",19: "nineteen"}
    tens = {10: "ten", 20: "twenty", 30: "thirty", 40: "fourty", 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninty"}
    etc = {100: "hundred", 1000: "thousand", 10000: "thousand", 100000: "thousand", 1000000: "million", 10000000: "trillion"}

    if x >= 1 and x <= 9: 
        print(digits[x]) 

    elif x >= 11 and x <= 19:
        print(teens[x])

    elif x % 10==0: 
        print(tens[x]) 

    elif x % 10 != 0 and x > 20 and x < 100: 
        print('')
numbers_to_words()