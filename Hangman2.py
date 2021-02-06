import random

words = ['apple', 'mango', 'pineapple']
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
chosen_word = random.choice(words)
print(f"selected word is {chosen_word}")
display = []
for letter in range(len(chosen_word)):
    display += "_"
print(display)

end_game = False
lives = 6
guess = {}
while not end_game:
    Guess = input("Enter a letter:").lower()
    for i in Guess:
        if i in guess:
            guess[i] += 1
        else:
            guess[i] = 1
        for i in guess.values():
            if i > 1:
                print("Entered letter already exist.please choose a different letter")
                guess = {}

    for position in range(len(chosen_word)):
        if Guess == chosen_word[position]:
            display[position] = chosen_word[position]
            print(f"you Guessed correctly,letter was in the {position} position of the word")
    print(display)
    print(stages[lives])
    if Guess not in chosen_word:
        lives -= 1
        print(f"you guessed wrongly and you have {lives} lives left")
        print(stages[lives])
        if lives == 0:
            print(stages[lives])
            print("you lose")
            end_game = True
    if "_" not in display:
        print("you win")
        end_game = True







