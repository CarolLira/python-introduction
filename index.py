import guessing_game;
import hangman_game;

print("*************************");
print("******Choose a game******");
print("*************************");

print("(1) hangman (2) guessing");

game = int(input("Choose: "));

if (game == 1):
    print("Playing Hangman Game");
    hangman_game.play_hangman();
elif (game == 2):
    print("Playing Guessing Game");
    guessing_game.play_guessing();