from functools import cache
from random import choice


@cache
def get_words():
    with open("words.txt") as file:
        return [word.strip() for word in file.readlines()]


def game():
    score = 0
    game_on = True

    while game_on:
        print(f"Score: {score}")
        word = choice(get_words())
        unique_letters = len(set(word))
        guessed_letters = []

        mistakes = 0
        max_mistakes = 3

        while len(guessed_letters) != unique_letters:
            hidden_word = "".join([letter if letter in guessed_letters else "_" for letter in word if letter])
            letter = input(f"Word: {hidden_word}\nAttempt: {max_mistakes - mistakes}\nGuess letter: ").strip()
            if letter in word:
                guessed_letters.append(letter)
            else:
                mistakes += 1
                if mistakes > max_mistakes:
                    print("You lose")
                    break
        else:
            score += 1
            print("You win!")

        game_on = input("Do you want play one more time? (y/n)") != "n"


if __name__ == "__main__":
    game()
