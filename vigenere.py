#  This is a simple program to encode or decode a message using a vigenere cipher
my_map = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11,
          "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22,
          "w": 23, "x": 24, "y": 25, "z": 26}
letters = "abcdefghijklmnopqrstuvwxyz"


def main():
    print("Would you like to encode or decode a message? e/d")
    method = input()
    encode = True
    correct_input = False
    while not correct_input:
        if method.lower() == 'e' or method.lower() == 'encode':
            correct_input = True
        elif method.lower() == 'd' or method.lower() == 'decode':
            encode = False
            correct_input = True
        else:
            print("Invalid input, please specify e or d")
            method = input()

    if encode:
        print("Please enter the message you would like to encode, only letters a-z")
        message = input().lower()
        print("Please enter the key to encode the message")
        key = input()
        while key.find(" ") != -1:
            print("Key cannot have a space in it, please enter a new key")
            key = input()
        key = key.lower()

        ciphertext = ""
        spacecount = 0
        for i, letter in enumerate(message):
            if letter == " ":
                ciphertext += " "
                spacecount += 1
                continue
            index = (my_map[letter] + my_map[key[(i - spacecount) % len(key)]] - 2) % 26
            ciphertext += letters[index]
        print("===============")
        print(ciphertext)
        print("===============")
    else:
        print("Please enter the message you would like to decode, only letters a-z")
        message = input().lower()
        print("Please enter the key to decode the message")
        key = input()
        while key.find(" ") != -1:
            print("Key cannot have a space in it, please enter a new key")
            key = input()
        key = key.lower()
        plaintext = ""
        spacecount = 0
        for i, letter in enumerate(message):
            if letter == " ":
                plaintext += " "
                spacecount += 1
                continue
            index = (my_map[letter] - my_map[key[(i - spacecount) % len(key)]]) % 26
            plaintext += letters[index]
        print("===============")
        print(plaintext)
        print("===============")


if __name__ == '__main__':
    main()
