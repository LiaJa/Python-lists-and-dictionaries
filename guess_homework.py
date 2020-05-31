import random
import json
import datetime

player = input("Hi, what's your name?")

current_time = datetime.datetime.now()
secret = random.randint(1, 30)
attempts = 0

with open("scorehow_list.txt", "r") as scorehow_file:
    scorehow_list = json.loads(scorehow_file.read())
    for scorehow_dict in scorehow_list:
        print(str(scorehow_dict["attempts"]) + "  attempts for " +  scorehow_dict.get("player_name") + " on date: " + scorehow_dict.get("datetime") + " with secret number: " + str(scorehow_dict.get("secret_number")) + " and "  + str(scorehow_dict.get("wrong_guesses")) + " wrong guessess ")

wrong_guesses=[]
while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))
    attempts += 1

    if guess == secret:
        scorehow_data = {"attempts": attempts, "datetime": str(current_time), "player_name": player, "secret_number": secret,"wrong_guesses": wrong_guesses}
        scorehow_list.append(scorehow_data)

        with open("scorehow_list.txt", "w") as scorehow_file:
            scorehow_file.write(json.dumps(scorehow_list))

        print("You've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))
        break
    elif guess > secret:
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        print("Your guess is not correct... try something bigger")

    wrong_guesses.append(guess)
