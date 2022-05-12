'''
Tip Calculator

Calculates how much each person shoul pay
according number of people and how much you want to tip the waiter
rounded to two decimal places
'''

#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

# Create a print statement
print("Hi, I'm pingu. I will calculate your tips for you.")

# Ask the user for total bill
# And save the data to variable total_bill
# change data type from str to float(money)
total_bill = float(input("What was the total bill? $"))
n_people = int(input("how many people to split the bill? "))
tip = int(input("how much do you want to tip? "))
bill_tip = (tip/100 + 1) * total_bill
amount = bill_tip / n_people

# create final amount variable by creating a string 
# using format function to pass in amount
final_amount = "{:.2f}".format(amount)
print(f"Each person should pay ${final_amount}")

