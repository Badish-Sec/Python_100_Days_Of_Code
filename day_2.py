#A simple bill calculator that calculates tip and splits the bill.

#If the bill was $150.00, split between 5 people, with 12% tip.
print("Welcome to the tip calcuator.")

bill = int(input("What was the total bill?: $"))

percentage = int(input("What percentage of the tip would you like to give? 10, 12 or 15?: "))

people = int(input("How many people are you splitting the bill with?: "))

tip = bill * (percentage/100)

per_head = (bill + tip) / people
cost = round(per_head, 2)
print(f"Each person has to pay: ${cost}")
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
