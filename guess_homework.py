import random
import json
import datetime

player = input("Hi, what's your name?")

current_time = datetime.datetime.now()
secret = random.randint(1, 30)
attempts = 0

with open("scorehw_list.txt", "r") as scorehw_file:
    scorehw_list = json.loads(scorehw_file.read())
    for scorehw_dict in scorehw_list:
        print(str(scorehw_dict["attempts"]) + "  attempts for " +  scorehw_dict.get("player_name") + " on date: " + scorehw_dict.get("datetime") + " with secret number: " + str(scorehw_dict.get("secret_number")) + " and " + str(scorehw_dict.get("wrong_guesses")) + " wrong guesses ")

wrong_guesses = []
while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))
    attempts += 1

    if guess == secret:
        scorehw_data = {"attempts": attempts, "datetime": str(current_time), "player_name": player, "secret_number": secret, "wrong_guesses": wrong_guesses}
        scorehw_list.append(scorehw_data)

        with open("scorehw_list.txt", "w") as scorehw_file:
            scorehw_file.write(json.dumps(scorehw_list))

        print("You've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))
        break
    elif guess > secret:
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        print("Your guess is not correct... try something bigger")

