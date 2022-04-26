#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

main_bill = input("What was the total bill? $")

what_tip = input("How much tip would you like to give? 10, 12, or 15?")

bill_split = input("How many people to split the bill?")

# (percent * whole) / 100.0

percentage_tip = (float(main_bill) * (float(what_tip) / 100))

total_amount = float(percentage_tip) + float(main_bill)

split_bill = float(total_amount) / float(bill_split)

format_bill = "{:.2f}".format(split_bill)

# rounded = round(split_bill, 2)
# print(rounded)

print(f"Each person should pay: ${format_bill}")

# float = 2.154327
# format_float = "{:.2f}".format(float)
# print(format_float)