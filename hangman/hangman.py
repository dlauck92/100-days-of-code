import random
from animals_list import animals

stages = [
    """
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
          |
          |
          |
          |
    =========
    """
]

random_word = random.choice(animals)
placeholder = ""
word_length = len(random_word)
lives = 6

for letter in random_word:
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []

while not game_over:
    print(f"***Remaining lives: {lives}***")
    guess = input("Guess a letter: ").lower()
    display = ""

    if guess in correct_letters:
        print(f"You've already guessed {guess}. Try again.")

    for letter in random_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    if guess not in random_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("********************You lose...************************!")
            print(f"The word was {random_word}")

    if "_" not in display:
        game_over = True
        print("********************You win!************************")

    print(stages[lives])