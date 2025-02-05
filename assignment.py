# 1. A simple python program to
#check whether a year is a leap year or not
year = 2024
if year % 4 == 0 and year % 100 !=0:
    print(year, "Is a leap year")
else:print(year, "Is not a leap year")


#2. A python program that checks whether a letter is a vowel or a consonant
letter = "a"
vowels = "aAeEiIoOuU"
if letter in vowels:
    print(letter, "is a vowel")
else:print(letter, "is not a vowel")