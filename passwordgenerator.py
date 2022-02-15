# Modified password generator project from day 5
import random


class Password:

    def __init__(self):
        self.LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                        't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                        'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    def generate(self):

        nr_letters = random.randint(8, 10)
        nr_symbols = random.randint(2, 4)
        nr_numbers = random.randint(2, 4)

        password_list = []

        for char in range(nr_letters):
            password_list.append(random.choice(self.LETTERS))

        for char in range(nr_symbols):
            password_list += random.choice(self.SYMBOLS)

        for char in range(nr_numbers):
            password_list += random.choice(self.NUMBERS)

        random.shuffle(password_list)

        password = ""
        for char in password_list:
            password += char

        return password
