import random

money = 100

#Write your game of chance functions here
def coin():
 coin = random.randint(1,2)
 if coin == 1:
  return "Heads"
 else:
  return "Tails"

def coin_flips(guess,bet):
  toss = coin()
  if guess != "Heads" and "Tails" :
   print("Your input is wrong")
  else :
   print(toss)
  if toss ==  guess :
   return  + bet 
  else :
   return  - bet
  

#print(coin_flips(Heads,10)



def guess_cho_han():
 dice_one = random.randint(1,6)
 dice_two = random.randint(1,6)
 result_dice = dice_one + dice_two
 if result_dice%2 == 0:
  return "even"
 else:
   return "odd"

def cho_han(guess,bet):
  result = guess_cho_han() 
  if guess != "odd" and "even":
   print("Your input is wrong")
  else :
    print(result)
  if result == guess :
   return  + bet
  else :
   return  - bet 

#print(cho_han("odd",50))


def card():
  player1 = random.randint(1,10)
  player2 = random.randint(1,10)
  if player1 > player2:
   return "player1"
  elif player2 > player1:
   return "player2"
  else :
   return ("player1","player2")

def player_wins(guess,bet):
  pick_player = card()
  if guess != "player1" and "player2":
   print("Your input is wrong")
  else :
    print(pick_player)
  if pick_player == guess:
   return  + bet
  elif pick_player != guess:
   return  - bet 
  elif pick_player == "player1" and "player2":
   return money 
  
   

#Call your game of chance functions here
money += coin_flips("Heads", 60)
money += cho_han("odd", 70)
money += player_wins("player1",80)
if money < 0 :
 print("You have 0 balance now!")
else : 
 print("You have "+ str(money) +" balance now!")





