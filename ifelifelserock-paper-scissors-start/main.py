import random 
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice = int(input("what u wanna know rock paper or scissors 0 rock 1 rock and siscors 2?\n"))
game_images = [rock, paper , scissors]
computer = random.randint(0, 2)
print("computer chosen")

if choice >= 3  and choice < 0:
  print ("invalid pro")
  print(game_images[computer])

elif computer == 0 and choice == 2:
  print("you win")
  print(game_images[computer])
  print(game_images[choice])
elif computer > choice:
  print("you lose")
  print(game_images[computer])
  print(game_images[choice])
elif computer == 0 and choice:
  print("draw brorororor")
  print(game_images[computer])
  print(game_images[choice])
elif computer == 0 and choice == 2:
  print("you lost ")
  print(game_images[computer])
  print(game_images[choice])
elif computer < choice:
  print(game_images[computer])
  print("you win")
  print(game_images[choice])
else:
  print("you typed an invaild number, you lose bruh")