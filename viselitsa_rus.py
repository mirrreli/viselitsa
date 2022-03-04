import random
categories = ["природа", "еда", "вокруг нас", "программирование", "игры"]
word_list_nature = [
    "комар",
    "дерево",
    "насекомое",
    "горизонт",
    "закат",
    "палка",
    "восход",
    "водопад"
]

word_list_food = [
    "авокадо",
    "креветка",
    "роллы",
    "макароны",
    "корнишоны",
    "майонез",
    "желе",
    "котлета",
    "пюрешка",
    "борщ"
]
word_list_around_us = [
    "пылесос",
    "кровать",
    "компьютер",
    "лампочка",
    "тлен",
    "хрущевка",
    "батарея",
    "кружка",
    "пакет"
]
word_list_programming = [
    "жаба",
    "плюсы",
    "питон",
    "фича",
    "репка",
    "бэкенд",
    "коммит",
    "ботать",
    "ридми"
]
word_list_games = [
    "дота",
    "ксго",
    "ведьмак",
    "дарксоулс",
    "геншин",
    "майнкрафт",
    "киберпанк",
    "сталкер",
    "овервотч",
    "дум"
]

def get_category():
    category = random.choice(categories)
    return category.upper()

def get_word(category):
    if category == "ПРИРОДА":
        word = random.choice(word_list_nature)
    elif category == "ЕДА":
        word = random.choice(word_list_food)
    elif category == "ВОКРУГ НАС":
        word = random.choice(word_list_around_us)
    elif category == "ПРОГРАММИРОВАНИЕ":
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
    print("Ну че погнали, вешать тебя будем")
    print("Твоя категория: ", category)
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Давай, попробуй угадать хотя бы букву: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("Лол,дебик,ты уже угадал эту букву", guess)
            elif guess not in word:
                print("Ха, лох, эта ошибка стоила тебе конечности.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Ого,", guess, "ряльно в слове есть")
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
                print("Да угадал ты уже это слово, успокойся", guess)
            elif guess != word:
                print(guess, "твоя мамаша, а не нужное слово.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Ты нормально давай, без выебонов.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Ну ладно, красава,угадал")
    else:
        print("Сорян, братан, но слово " + word +
              " ты не угадал. Я бы сказал повезет в другой раз, но ты сдох ха-ха")


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
    while input("Заново хочешь? (Y/N) ").upper() == "Y":
        category = get_category()
        word = get_word(category)
        play(word, category)


if __name__ == "__main__":
    main()
