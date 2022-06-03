import random



choices = ["R","P","S"]

computer = random.choice(choices)
player = input("Select 'R'(rock), 'P'(paper) or 'S'(scissors):\n").upper()
while player not in choices:
   print("Error! Invalid entry!")
   player = input("Select 'R'(rock), 'P'(paper) or 'S'(scissors):\n").upper()
else:
   while player == computer:
      computer = random.choice(choices)
      player = input("Select 'R'(rock), 'P'(paper) or 'S'(scissors):\n").upper()
   else:
      print("Player(",player,") : CPU(",computer,")")
    
if player == "R":
  if computer== "P":
     print("Computer wins! It picked: ",computer)
  elif computer == "S":
     print("You win! Computer picked: ",computer) 
elif player == "P":
  if computer== "S":
     print("Computer wins! It picked: ",computer)
  elif computer== "R":
     print("You win! Computer picked: ",computer)
elif player == "S":
  if computer== "R":
     print("Computer wins! It picked: ",computer) 
  elif computer == "P":
     print("You win! Computer picked",computer) 