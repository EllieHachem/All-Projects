import random
letters = ["a", "D", "c", "G"]
numbers = ["1", "2", "3", "4"]
symbols = ["@", "#", "$"]
print("welcome to password generator")
letters_in = int(input("how many letters bro"))
numbers_in = int(input("how many numbers bro"))
symbols_in = int(input("how many symbols bro"))

# easy way
password_list = []
for chara in str(range(1, letters_in + 1)):
  password_list.append(random.choice(letters))
for chara2 in str(range(1, numbers_in + 1)):
    random_chara = str(random.choice(numbers))
    password_list += random_chara
for chara3 in range(1, numbers_in + 1):
    random_chara = (random.choice(symbols))
    password_list += random_chara
print(f"{password_list}")
random.shuffle(password_list)
print(f"{password_list}")

password = ""

for charo in password_list:
    password += chara

print(f"you final password is {password}")
