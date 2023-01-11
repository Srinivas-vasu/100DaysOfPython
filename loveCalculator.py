print('Welcome to the Love Calculator!')
name1=input('What is your name?\n')
name2=input('what is your mate name ?\n')

names=name1+name2

names=names.lower()
t=names.count('t')
r=names.count('r')
u=names.count('u')
e=names.count('e')

l=names.count('l')
o=names.count('o')
v=names.count('v')
e=names.count('e')

love_score=t+r+u+e+l+o+v+e
if love_score<10 or love_score>90:
    print(f'Your love score {love_score},you go together like coke and mentos')
elif love_score>40 and love_score<50:
    print(f'Your love score {love_score},you are alright together.')
else:
    print(f'Your love score {love_score}')

