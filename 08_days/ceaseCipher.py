small_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']

word = input("Type Message\n ").lower()
shift=int(input("Type to how much shift:\n"))
direction = input("Type decoded to encoded and type encoded to decoded")

finalWord=""

def encrypt(original_text,shift_amount):
    for letter in original_text:
        letter.index(small_letters) + shift_amount
encrypt(word, shift,direction)