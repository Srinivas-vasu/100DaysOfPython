print("Welcome to Pizza Deliveries!")
size=input('What size pizza do you want? s,m,l')
add_pepproni=input("Do you want pepperoni? Y or N")
extra_chese=input("Do you want extra cheese? Y or N")
bill=0

if size=='s':
    bill=15
elif size=='m':
    bill=20
else:
    bill=25

if add_pepproni=='Y':
    bill+=2


if extra_chese=='Y':
    bill+=1

print(f'Your final bill is ${bill}')
