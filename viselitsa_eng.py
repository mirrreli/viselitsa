import random

categories = ["nature", "food", "around us", "programming", "games"]
word_list_nature = [
    "tree",
    "forest",
    "insects",
    "horizon",
    "beetles",
    "raindrop",
    "sunrise",
    "waterfall",
    "ocean"
]

word_list_food = [
    "avocado",
    "shrimp",
    "spaghetti",
    "pickles",
    "cookie",
    "liver",
    "jelly",
    "beans"
]
word_list_around_us = [
    "computer",
    "table",
    "bulb",
    "bucket",
    "wardrobe",
    "mirror",
    "furniture",
    "dust",
]
word_list_programming = [
    "bugs",
    "jimmy",
    "hindenbug",
    "tuple",
    "duck",
    "banana",
    "backend",
    "oracle",
    "javascript"
]
word_list_games = [
    "dota",
    "witcher",
    "darksouls",
    "genshin",
    "minecraft",
    "cyberpunk",
    "stalker",
    "doom",
    "overwatch",
    "portal"
]


def get_category():
    category = random.choice(categories)
    return category.upper()


def get_word(category):
    if category == "NATURE":
        word = random.choice(word_list_nature)
    elif category == "FOOD":
        word = random.choice(word_list_food)
    elif category == "AROUND US":
        word = random.choice(word_list_around_us)
    elif category == "PROGRAMMING":
        word = random.choice(word_list_programming)
    else:
        word = random.choice(word_list_games)
    return word.upper()


def play(word, category):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Yo dude are u ready?")
    print("Your category: ", category)
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Come on, try to guess at least one letter: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("lol, man, you already guessed that letter", guess)
            elif guess not in word:
                print("ha, this mistake cost you a whole body part.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("wow,", guess, "you guessed right")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(
                    word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("calm down dude you already guessed this word wrong please leave me alone i beg you please im tired im just stupid code why are you doing this to me? never say " + guess + " again")
            elif guess != word:
                print(guess, "your mom.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("whats your problem, dude?.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Okay, good, you actually did it")
    else:
        print("Sorry bro, the word was " + word +
              " you did not guess it. i wanna say better luck next time, but you are dead")


def display_hangman(tries):
    stages = ["""
                    --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
              """
                    --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
              """
                    --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
              """
                    --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -

                """,
              """
                    --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                """,
              """
                    --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                """,
              """
                    --------
                   |      |
                   |
                   |
                   |
                   |
                   -
                """
              ]
    return stages[tries]


def main():
    category = get_category()
    word = get_word(category)
    play(word, category)
    while input("Wanna try again? (Y/N) ").upper() == "Y":
        category = get_category()
        word = get_word(category)
        play(word, category)


if __name__ == "__main__":
    main()