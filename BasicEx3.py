# Building a guessing game

times = ["", "First", "Second", "Third", "Fourth", "Fifth", "Sixth", "Seventh", "Eighth", "Ninth", "Tenth",
         "Eleventh", "Twelfth", "Thirteenth", "Fourteenth", "Fifteenth", "Sixteenth", "Seventeenth",
         "Eighteenth", "Nineteenth", "Twentieth"]
times_guessed = 0
max_times_to_guess = 20  # Up tp 20
the_word = "Knight"


def guess(guess_word):
    global times_guessed
    times_guessed += 1
    if guess_word == the_word:
        print("Correct! Good job!")
        return True
    else:
        print("It is not correct...")
    if times_guessed == max_times_to_guess:
        print("You ran out of energy!")
        return False


def run():
    print("Guess the word!")
    for i in range(1, max_times_to_guess+1):
        guess_word = input(f"{times[i]} challenge: ")
        flag = guess(guess_word)
        if flag:
            print(f"You guessed correctly in {i+1} times!")
            break


run()
