import random

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
           "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
           'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the gPassword generator!")

input_letters = int(input("How many letters do you want in your password?:\n"))
input_numbers = int(input("How many numbers do you want in your password?:\n"))
input_symbols = int(input("How many symbols do you want in your password?:\n"))

password = []

for i in range(1, input_letters + 1):
    password += random.choice(letters)
for j in range(1, input_numbers + 1):
    password += random.choice(numbers)
for k in range(1, input_symbols + 1):
    password += random.choice(symbols)

random.shuffle(password)

password_new = ""

for elements in password:
    password_new+=elements
print(password_new)
