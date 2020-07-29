# Write your code here
import random

print("H A N G M A N")
action = str(input('Type "play" to play the game, "exit" to quit: '))
if action == "exit":
    exit()
elif action == "play":
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

        if len(guess_letter) != 1:
            print("You should input a single letter")
        elif not guess_letter.isalpha() or guess_letter.isupper():
            print("It is not an ASCII lowercase letter")
        elif guess_letter in guess_set:
            print("You already typed this letter")
        elif guess_letter in word_set:
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
            guess_set.add(guess_letter)
            lives -= 1
            print("No such letter in the word")



    if lives == 0:
        print("You are hanged!")

    print("Thanks for playing!")
