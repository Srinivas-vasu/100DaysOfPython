import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list=['word','wrong','right','animal']
lives=6
chosen_word=random.choice(word_list)
print(chosen_word)
lst=[]

for i in range(len(chosen_word)):
    lst.append('_')


end_of_game=False
while not end_of_game:
    guess=input('guess a letter: ').lower()
    for j in range(len(chosen_word)):
        i=chosen_word[j]
        if i==guess:
            lst[j]=i
            print(lst)
    if guess not in chosen_word:
        lives-=1
        if lives==0:
            end_of_game=True
            print('you lose')
    if'_' not in lst:
        end_of_game=True
        print('you win')
    print(stages[lives])
