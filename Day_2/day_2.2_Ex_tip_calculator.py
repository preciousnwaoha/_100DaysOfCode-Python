print("Wlcome to the tip calculator.")
total_bill = float(input("What was th total bill? $"))

percent_tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

split = int(input("How many people to split the ball? "))

each_bill = (total_bill/split)

each_tip = (percent_tip / 100) * each_bill

each_pay = round((each_bill + each_tip), 2)

messege = f"Each person should pay: ${each_pay}"
print(messege)