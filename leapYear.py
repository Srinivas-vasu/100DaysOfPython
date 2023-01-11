year=int(input('Which year do you want to check'))

if year%4==0:
    if year%100!=0:
        print('Leap year')
    elif year%400:
        print('Leap Year')
else:
    print('Not a leap year')