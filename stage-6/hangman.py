 # Write your code here
import random

print("H A N G M A N")

word_choices = ("python", "java", "kotlin", "javascript")
word = random.choice(word_choices)
guess_list = list("-" * len(word))

word_set = set(word)
guess_set = set()

lives = 8

while lives > 0:
    print()
    print(''.join(guess_list))

    guess_letter = str(input("Input a letter: "))

    if guess_letter in word_set:
        if guess_letter in guess_set:
            lives -= 1
            print("No improvements")

        else:
            guess_set.add(guess_letter)

            for i in range(len(word)):
                if word[i] == guess_letter:
                    guess_list[i] = guess_letter

            if ''.join(guess_list) == word:
                print()
                print(word)
                print("You guessed the word!")
                print("You survived!")
                break
    else:
        lives -= 1
        print("No such letter in the word")



if lives == 0:
    print()
    print("You are hanged!")

print("Thanks for playing!")
