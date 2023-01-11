#TIP calculator
print("Welcome to tip calculator.")
bill=input('What was the total bill? $')
tip=input('What percentage tip ould you like to give?10, 12, or 15?')
split_bill=input('How many people to split the bill?')
split=float(bill)/int(split_bill)
tip_calc=split*(12/100)
tip_and_bill=(split)+tip_calc
print(f'Each person should pay: ${round(tip_and_bill,2)}')