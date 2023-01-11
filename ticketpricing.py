height=int(input("enter your height "))
bill=0
if height>120:
    print('You can ride')
    age=int(input('enter your age'))
    if age<12:
        bill=5
        print('please pay $5')
    elif age>12 and age<18:
        bill=7
        print('please pay $7')
    else:
        bill=12
        print('please pay $12')
    photo=input('Do you want a photo taken Y or N.')
    if photo=='Y':
        bill+=3
    print(f'Please your final bill ${bill}')
else:
    print("You can't ride")