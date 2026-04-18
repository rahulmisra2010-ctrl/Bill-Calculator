print("Welcome to the tip Calculator")
Total = float(input("What was the total bill? "))
Tip = float(input("How much tip would you like to give? "))
Share_between = float(input("How many people to split the bill? "))

Total_Tip = Total * Tip / 100
Amount_per_person = (Total + Total_Tip) / Share_between

print(f"Each person should pay: ${Amount_per_person:.2f}")