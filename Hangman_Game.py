import random
from hangman_art import stages, logo #locally module created
from hangman_words import word_list  #locally module created

print("welcome to the HangMan Game")
print(logo)

# to create random choice
chosen_word = random.choice(word_list)

# to create display
word_range = len(chosen_word)
display = []
for _ in range(word_range):
    display += "_"

print(display)  # to be deleted

# to create loop to end game
lives = 6
end_game = False

while not end_game:
    # user input
    guess = input("Guess any word: ").lower()
    # to notify the user they have already guessed word
    if guess in display:
        print(f"you have already guessed the {guess}")

    for position in range(word_range):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You've guessed {guess} which is a wrong word, and you've lost one life")

        lives -= 1
        if lives == 0:
            end_game = True
            print("you loose")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_game = True
        print("you win")

    print(stages[lives])
