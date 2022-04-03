def play_hangman():
    print();
    print("***************************");
    print("Welcome to the hangman game");
    print("***************************");
    print();

    secret_word = "chocolate";
    found_letters = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]

    hanged = False;
    won = False;
    attempts = 0;

    print(found_letters);
    print();

    while (not hanged and not won):
        # print('hanged', hanged)
        guess = input("Type a letter: ");
        guessFormatted = guess.strip().lower();

        if (guessFormatted in secret_word):
            index = 0;

            for letter in secret_word:
                if (guessFormatted == letter):
                    found_letters[index] = letter
                index = index + 1;
        else:
            attempts = attempts + 1;
            # print('attempts', attempts)

        hanged = attempts == 6;
        print(found_letters);

        print("jogando...");

    print("Fim do jogo");

if (__name__ == "__main__"):
    play_hangman();