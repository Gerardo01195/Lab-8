playerHp = 100
monsterHp = 100
punchDmg = 8
swordDmg = 15
fireBall = 30
import random
print "A wild monster has appeared! Time to fight!"
print "--------------------------------------------"
print "you have 100 health"
print "the monster has 100 health"
print "--------------------------------------------"
print "what attack do you wish to use?"
print "1 - Punch 2 - Sword. 3 - Fireball."
print "--------------------------------------------"

while (playerHp > 0) and (monsterHp > 0):
    userInput = int(raw_input())

    if userInput == (1):
        monsterHp = monsterHp - 8
    
    if userInput == (2):
        monsterHp = monsterHp - 15
        
    if userInput == (3):
        monsterHp = monsterHp - 30
       
    
    # monster attack
    damageBymonster = random.randint (1,35)
    playerHp =  playerHp - damageBymonster 
   
    print "you have " + str(playerHp) + " health"
    print "the monster has " + str(monsterHp) + " health"
    print "--------------------------------------------"
    print "what attack do you wish to use next?"
    print "1 - Punch 2 - Sword. 3 - Fireball."
    print "--------------------------------------------"


    
