# Write your code here
import random

print("H A N G M A N")

word_choices = ("python", "java", "kotlin", "javascript")
word = random.choice(word_choices)
word_snippet = word[:3] + '-' * (len(word) - 3)

guess = input("Guess the word " + word_snippet + ": ")

if guess == word:
    print("You survived!")
else:
    print("You are hanged!")
