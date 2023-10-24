def encode(pw):
    encoded = ""
    for digit in pw:
        encoded += str(int(digit) + 3)
    return encoded


def decode(pw):
    decoded = encode(pw)
    original = ''
    for digit in decoded:
        original += str(int(digit) - 3)
    return original


def main():
    runmenu = True
    while runmenu:
        print("\nMenu\n-------------\n1. Encode\n2. Decode\n3. Quit")
        menuinput = int(input("\nPlease enter an option: "))
        if menuinput == 1:
            password = input("Please enter your password to encode: ")
            print("Your password has been encoded and stored!")
        elif menuinput == 2:
            print(f'The encoded password is {encode(password)}, and the original password is {password}.')
        elif menuinput == 3:
            print(decode(password))
            runmenu = False


if __name__ == "__main__":
    main()