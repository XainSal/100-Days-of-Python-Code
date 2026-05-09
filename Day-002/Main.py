print("Welcome to the tip calculator.")

totalBill = float(input("What was the total bill? $"))
tipPercent = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
billSplit = int(input("how many people to split the bill? "))

totalTip = (totalBill / 100) * tipPercent
finalBill = (totalTip + totalBill) / billSplit

print(f"Each person should pay: {round(finalBill, 2)}")


