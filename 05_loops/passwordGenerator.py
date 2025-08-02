import random
capital_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                   'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                   'U', 'V', 'W', 'X', 'Y', 'Z']
small_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']
special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
                      '-', '_', '=', '+', '[', ']', '{', '}', ';', ':',
                      "'", '"', ',', '.', '<', '>', '/', '?', '\\', '|', '`', '~']
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

print("Welcome to the password Generator")
nr_letter = int(input("How many letter you want to like in the password \n"))
nr_symbol = int(input("how many symbol you want to \n"))
nr_numbers = int(input("How many number would you like?\n")) 
nr_character = int(input("How many character would you like?\n")) 

#easy level 
password =""

for i in range(1,nr_letter +1):
    random_character=random.choice(capital_letters)
    password+=random_character

for i in range(1,nr_symbol+1):
    random_character = random.choice(small_letters)
    password+=random_character
   

for i in range(1,nr_numbers+1):
    random_character=random.choice(numbers)
    password+=random_character


for i in range(1,nr_character+1):
    random_character+=random.choice(special_characters)
    password+=random_character
 
print("Password",password)
