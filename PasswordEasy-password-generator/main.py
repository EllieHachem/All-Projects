import random
letters = ["a", "D", "c", "G"]
numbers = ["1", "2", "3", "4"]
symbols = ["@", "#", "$"]
print("welcome to password generator")
letters_in = int(input("how many letters bro"))
numbers_in = int(input("how many numbers bro"))
symbols_in = int(input("how many symbols bro"))

# easy way
password = ""
for chara in range(1, letters_in + 1):
    random_chara = random.choice(letters)
    password += random_chara

for chara2 in range(1, numbers_in + 1):
    random_chara = random.choice(numbers)
    password += random_chara
for chara3 in range(1, numbers_in + 1):
    random_chara = random.choice(symbols)
    password += random_chara
print(password)
