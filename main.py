import random
import json
import requests

url = "https://random-word-api.herokuapp.com/all"
response = requests.get(url)

data = response.json()

word = random.choice(data)

print("Guess the characters of the word!")

guesses = ''

turns = len(word) + 5

while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char)
        else:
            print("_")
            failed += 1
    for char in word:
        if char in guesses:
            print(char)
        else:
            print("_")
            failed += 1
            

    if failed == 0:
        print("You Win, Congratulations!!!")
        print("The word is: ", word)
        break

    guess = input("guess a character:")
    guesses += guess

    if guess not in word:
        turns -= 1
        print("Wrong")
        print("You have", + turns, 'more guesses')
        if turns == 0:
            print("You Loose, better luck next time!")