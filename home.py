"""
    Write a program that does the following:

Prompt the user for their age. Convert it to a number, add one to it, and tell them 
how old they will be on their next birthday.

Prompt the user for the number of egg cartons they have.
Assume each carton holds 12 eggs, multiply their number by 12, and display the total
number of eggs.

Prompt the user for a number of cookies and a number of people. Then, 
divide the number of cookies by the number of people to determine how many cookies 
each person gets.
"""
    
age = input("How old are you?")
age_digit = int(age)
next_birthday = age_digit + 1
print(f"You will be {next_birthday} on your next birthday.")
print("-----------------------------------------")
number_egg = input("How many egg cartons do you have?")
number_egg_digit = int(number_egg) * 12
print(f"You have {number_egg_digit} eggs.")
print("-----------------------------------------")
number_of_cookies = input("How many cookies do you have?")
number_of_people = input("How many people are there?")
cookies_per_person = int(number_of_cookies) / int(number_of_people)
print(f"Each person gets {cookies_per_person} cookies.")
