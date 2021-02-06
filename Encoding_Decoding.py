alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def ceaser(message, shift_no, cipher_direction):
    display = ""
    if direction == "encode":
        for i in text:
            position = alphabet.index(i)
            if position > len(alphabet):
                display += alphabet[(position + shift) - len(alphabet)]
            else:
                display += alphabet[position + shift]
        print(display)
    else:
        display_decode = ""
        for i in text:
            position = alphabet.index(i)
            if position > len(alphabet):
                display_decode += alphabet[(position - shift) - len(alphabet)]
            else:
                display_decode += alphabet[position - shift]
        print(display_decode)


end_game = True
while end_game:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    ceaser(message=text, shift_no=shift, cipher_direction=direction)
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        print("Goodbye")
        end_game = False





