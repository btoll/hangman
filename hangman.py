import getopt
import os
import random
import sys
import textwrap


import art


game = {
    "token": " _ "
}


def usage():
    """
    Prints the usage string

    """

    str = """
        USAGE:

            python3 hangman.py [--guesses=10]

        --guesses, -g  The number of guesses to allow.

        HINT:

            Press Ctl-D to start over at any time.
    """
    print(textwrap.dedent(str))


def guess(guesses):
    """
    Calls itself after every guess.

    :param guesses: Initially is 0 and is incremented every call.
    :type guesses: int
    """

    try:
        letter = input("Pick a letter: ")

        # Always clear the screen. The code below will determine what needs drawn.
        os.system("clear")

        game["guessed_letters"] += letter

        blanks = game.get("blanks")
        word = game.get("word")
        total_guesses = game.get("total_guesses")

        if letter in word:
            # Replace every blank with the guessed letter.
            for index, item in enumerate(word):
                if item == letter:
                    blanks[index] = letter

            # Draw the hanging man (since the guesses counter hasn't increased it will be the same as last time).
            # Note only draw him if the guesses counter has been incremented due to a bad guess.
            if guesses == 0:
                pass
            if guesses < 6:
                art.draw(guesses - 1)
            else:
                # Draw the whole hanging man.
                art.draw_all()

            print("\nGood job!")
            print("Previous guesses = " + game.get("guessed_letters"))
            print("\nGuess the word: " + " ".join(blanks) + "\n")
            if game.get("token") in blanks:
                guess(guesses)
            else:
                print("Congratulations, you win! You are awesome!")
                play_again()
        else:
            guesses += 1

            if guesses < 6:
                # Always draw the hanging man, regardless of the total number of guesses.
                art.draw(guesses - 1)
                print("\nThe word does not contain the letter " + letter + ".")
                print("Previous guesses = " + game.get("guessed_letters"))
                print("\nGuess the word: " + " ".join(blanks) + "\n")
                guess(guesses)
            elif guesses < total_guesses:
                # Draw the whole hanging man.
                art.draw_all()
                print("\nThe word does not contain the letter " + letter + ".")
                print("Previous guesses = " + game.get("guessed_letters"))
                print("\nGuess the word: " + " ".join(blanks) + "\n")
                guess(guesses)
            elif guesses == total_guesses:
                # Draw the whole hanging man.
                art.draw_all()
                print("\nSorry, you lose!")
                print("The word was " + word + ".")
                play_again()
    except EOFError:
        # Control-D to start over.
        init_game()


def init_game():
    """
    Starts a new game.  Mixes in session data to the global `game` dict.

    """

    os.system("clear")

    word = random.choice(game.get("words"))
    blanks = [game.get("token")] * len(word)

    game.update({
        "blanks": blanks,
        "word": word,
        # Reset this value if having played a game already.
        "guessed_letters": ""
    })

    # Draw the scaffold!
    art.start()

    print("\nGuess the word: " + " ".join(blanks) + "\n")
    guess(0)


def play_again():
    """
    Re-initiates another game.

    """

    resp = input("\nPlay again? [Y|n]: ")
    if resp not in ("N", "n"):
        init_game()
    else:
        print("Goodbye.")


def main(argv):
    """
    Entrypoint.

    :param argv: Argument vector.
    :type argv: list
    """

    try:
        opts, args = getopt.getopt(argv, "hg:", ["help", "guesses="])
    except getopt.GetoptError:
        print("Error: Unrecognized flag.")
        usage()
        sys.exit(2)

    # 6 == the number of hanging man body parts.
    total_guesses = 6

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit(0)
        elif opt in ("-g", "--guesses"):
            total_guesses = int(arg)

    try:
        game.update({
            "total_guesses": total_guesses,
            "words": open("/usr/share/dict/words").read().splitlines(),
        })

        init_game()
    except KeyboardInterrupt:
        # Control-C or Control-D sent a SIGINT to the process, handle it.
        print("\nGame aborted!")
        sys.exit(1)


if __name__ == "__main__":
    main(sys.argv[1:])
