import random
rock = '''
...     _______
... ---'   ____)
...       (_____)
...       (_____)
...       (____)
... ---.__(___)
... '''
paper = '''
...     _______
... ---'   ____)____
...           ______)
...           _______)
...          _______)
... ---.__________)
... '''

scissors = '''
...     _______
... ---'   ____)____
...           ______)
...        __________)
...       (____)
... ---.__(___)
... '''

choices=[rock,paper,scissors]
len_choices=len(choices)
user_choice=int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.'))

user_selected=choices[user_choice]
print(user_selected)

computer_choice=random.randint(0,len_choices-1)
computer_selected=choices[computer_choice]
print("Computer chose: "+computer_selected)

if user_choice==computer_choice:
    print("its a draw")
elif user_choice==0 and computer_choice==2:
    print("You won!")
elif user_choice==2 and computer_choice==1:
    print("You won!")
elif user_choice==1 and computer_choice==0:
    print("You won!")
else:
    print('you loose!')