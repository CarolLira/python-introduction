import random;

def play_hangman():

    opening_message();

    secret_word = load_secret_word();

    found_letters = initialize_correct_words(secret_word);

    hanged = False;
    won = False;
    attempts = 0;

    print(found_letters);
    print();

    while (not hanged and not won):
        guessFormatted = ask_for_a_letter();

        if (guessFormatted in secret_word):
            save_correct_letters(secret_word, guessFormatted, found_letters);
        else:
            attempts += 1;
            draw_hangman(attempts);

        hanged = attempts == 7;
        won = "_" not in found_letters;
        print(found_letters);

    if (won):
        won_message();
    else:
        lose_message(secret_word);

    print("Fim do jogo");

def opening_message():
    print();
    print("***************************");
    print("Welcome to the hangman game");
    print("***************************");
    print();

def load_secret_word():
    file = open("words.txt", "r");
    words_list = [];

    for line in file:
        line = line.strip();
        words_list.append(line);

    file.close();

    word_index = random.randrange(0, len(words_list));
    secret_word = words_list[word_index].upper();

    return secret_word;

def initialize_correct_words(secret_word):
    return ["_" for letter in secret_word];

def ask_for_a_letter():
    guess = input("Type a letter: ");
    return guess.strip().upper();

def save_correct_letters(secret_word, guessFormatted, found_letters):
    index = 0;

    for letter in secret_word:
        if (guessFormatted == letter):
            found_letters[index] = letter;
        index += 1;

def won_message():
    print("Você acertou!");

def lose_message(secret_word):
    print("Você perdeu :(");
    print();
    print("A palavra secreta era: {}".format(secret_word));

def draw_hangman(attempts):
    print("  _______     ")
    print(" |/      |    ")

    if(attempts == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(attempts == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(attempts == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(attempts == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(attempts == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(attempts == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (attempts == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if (__name__ == "__main__"):
    play_hangman();