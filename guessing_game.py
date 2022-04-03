import random;

def play_guessing():
    print();
    print("****************************");
    print("Welcome to the guessing game");
    print("****************************");
    print();

    secret_number = random.randrange(1, 101);
    attempts = 1;
    maxAttempts = 0;
    points = 1000;

    print("Choose a difficulty level:");
    print("(1) Easy (2) Medium (3) Hard");
    level = int(input("Level: "));

    if (level == 1):
        maxAttempts = 20;
    elif (level == 2):
        maxAttempts = 10;
    else:
        maxAttempts = 5;
        

    for attempts in range(1, maxAttempts + 1):
        print("Attempt: {} from {}".format(attempts, maxAttempts));
        print("********************************************");
        print();

        answer = int(input("Type a number between 1 and 100: "));

        print("You typed: ", answer);

        if (answer < 1 or answer > 100):
            print("Type a number between 1 and 100");
            continue

        isItRight = answer == secret_number;
        higher = answer > secret_number;
        lower = answer < secret_number;

        if (secret_number == answer):
            print("You're right and did {} points".format(points));
            break;
        else:
            if (answer > 12):
                print("You're wrong! You're guess was higher than the secret number");
            elif (answer < 12):
                print("You're wrong! You're guess was lower than the secret number");
            lost_points = abs(secret_number - answer);
            points = points - lost_points;

    print("Fim do jogo");

if (__name__ == "__main__"):
    play_guessing();
