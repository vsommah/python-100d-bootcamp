alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().

def caesar(typed_text, typed_shift, typed_direction):
    desired_text = ""
    if typed_direction == "decode":
        typed_shift *= -1
    for letter in typed_text:
        position = alphabet.index(letter)
        new_position = position + typed_shift
        desired_text += alphabet[new_position]
    print(f"The {typed_direction}d text is {desired_text}")


# TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.

caesar(typed_text=text, typed_shift=shift, typed_direction=direction)
