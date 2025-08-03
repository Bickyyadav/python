#Randomly choose a word from a word list ans assign it to a variable called choose world.Then print it. 
import random
words = ["apple", "banana", "car", "dog", "elephant", "fish", "grape", "hat", "ice", "jungle"]
choosen_world = random.choice(words)
for letter in choosen_world:
    print("_",end=" ")
#Ask the user to guess the letter in lower case 
guess = input("\nGuess the word:").lower()
print(guess)
display=""
#if the user that the letter guess and one of the first letter is present in the world or not 
for letter in choosen_world:
    if letter == guess:
        display += letter
    else:
        display += "_"

print(display) 