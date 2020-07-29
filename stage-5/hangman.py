# Write your code here
import random

print("H A N G M A N")
print()

word_choices = ("python", "java", "kotlin", "javascript")
word = random.choice(word_choices)
guess_string = "-" * len(word)

word_set = set(word)

for i in range(8):
    print(guess_string)

    guess_letter = str(input("Input a letter: "))

    if guess_letter in word_set:
        for i in range(len(word)):
            if word[i] == guess_letter:
                guess_string[i] = guess_letter
    else:
        print("No such letter in the word")

    print()

print("Thanks for playing!")
print("We'll see how well you did in the next stage")
