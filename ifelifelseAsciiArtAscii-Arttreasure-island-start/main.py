print('''
*******************************************************************************
                         `.  `-.
                         .-'    `.
                       .'      _..:._
                      `.  .--.'      `.
                      _.'  \.      .--.\
                    .'      |     |    |
                   `--.     |  .--|    D
                       `;  /'\/   ,`---'@
                     .'  .'   '._ `-.__.'
                   .'  .'      _.`---'
                 .'--''   .   `-..__.--.
          jgs ~-=  =-~_-   `-..___(  ===;
              ~-=  - -    .'       `---'

*******************************************************************************
''')
print("Welcome to Treasure sonic.exe Game bro.")
print("Your mission is to stay alive bro.") 

Direction = input(f"which direction you want to go bro:\n ")
Direction2 = input(f"nice now the second qusetion jump or swim?\n" )
Direction3 = input(f"Which of the following doors?\n" )
Direction_edit = Direction.lower()
Direction2_edit = Direction2.lower()
Direction3_edit = Direction3.lower()

if Direction_edit == str(f"right" or "Right" or "RIGHT" or "rIght"):
  print(Direction2_edit)
else:
  print("game over sonic have died")

if Direction2_edit == str("jump") or str("JUMP") or str("JUMP"):
   print(Direction3_edit)
else:
  print("sonic died lol gameoveer")

if Direction3_edit == str("yellow") or str("Yellow") or str("YELLOW"):
  print("nice you won and survived")
else:
  print("you died omg lol poor sonic")
