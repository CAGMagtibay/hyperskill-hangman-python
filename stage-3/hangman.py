# Write your code here
import random

print("H A N G M A N")

word_choices = ("python", "java", "kotlin", "javascript")
word = random.choice(word_choices)
guess = input("Guess the word: ")

if guess == word:
    print("You survived!")
else:
    print("You are hanged!")
