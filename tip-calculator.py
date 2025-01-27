print("Welcome to the tip calculator!")

totalBill = float(input("What was the total bill? "))

tip = int(input("How much tip would you like to give? 10%, 12%, or 15%? (Don't include percent sign) "))

totalPeople = int(input("How many people to split the bill? "))

calculateBill = totalBill * (1 + (tip / 100)) / totalPeople

costPerPerson = round(calculateBill, 2)
costPerPerson = "{:.2f}".format(calculateBill)

print(f"Each person should pay ${costPerPerson}.")
