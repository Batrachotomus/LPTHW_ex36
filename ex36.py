import os
from sys import exit
import roomdesc

clear = lambda: os.system('cls' if os.name=='nt' else 'clear')

player_inv = []

def starter():
    clear()
    print(roomdesc.startroom)
    print("\n[check] what's happening. Do [nothing]\n")
    choice = input("> ")
    
    if "check" in choice:
        print("You look at the floor but see void instead, it draws you in!")
        input()
        first_room()
    elif "nothing" in choice:
        print("You've decided to do nothing, but it feels that whole bed is falling down!!")
        input()
        first_room()
    else:
        starter()

def first_room():
    clear()
    print("Your inventory:", player_inv)
    print(roomdesc.firstroom)
    print("\nGo to [left] door. Go to [center] door. \nGo to [right] door. [Examine] the room.\n")
    choice = input("> ")
    
    if "left" in choice:
        mario_room()
    elif "center" in choice:
        bear_room()
    elif "right" in choice:
        spaceinv_room()
    elif "examine" in choice:
        first_room_examine()
    else:
        print("It seems your choice was incorrect")
        input()
        moebius()

def first_room_examine():
    clear()
    print("Your inventory:", player_inv)
    print(roomdesc.firstroomexamine)
    choice = input("> ")

    if "pick" in choice:
        player_inv.append('mushroom')
        print("You put a mushroom in your pocket!")
        roomdesc.firstroomexamine = roomdesc.examined
        input()
        first_room()
    elif "ignore" in choice:
        print("You've decided to leave it for now..")
        input()
        first_room()
    else:
        print("It seems your choice was incorrect")
        input()
        moebius()

invader_fed = False

def spaceinv_room():
    global invader_fed
    clear()
    print("Your inventory:", player_inv)
    print(roomdesc.spaceinvroom)
    print("\nOpen the center [door]. Go [back]\n[Interact] with monster or [Examine] the room.\n")
    choice = input("> ")
    
    if "door" in choice and invader_fed is True:
        print("You've chosen to open the door..")
        input()
        portal_room()
    elif "door" in choice and invader_fed is False:
        print("You can't pass here. Maybe you don't have nesseccary item in inventory..")
        input()
        spaceinv_room()
    elif "interact" in choice and "coin" in player_inv:
        print("Space invader thankfully gets a coin and sticks to the ceiling.")
        input()
        player_inv.remove('coin')
        invader_fed = True
        spaceinv_room()
    elif "interact" in choice and "coin" not in player_inv:
        print("You tried to sing 'Invaders must die by Prodigy' as lullaby, but he refused to move avay and sleep.")
        input()
        spaceinv_room()
    elif "back" in choice:
        print("You've decided to go back")
        input()
        first_room()
    elif "examine" in choice:
        print("You start looking for anything useful")
        input()
        spaceinv_room_examine()
    else:
        print("It seems your choice was incorrect")
        input()
        moebius()

def spaceinv_room_examine():
    global invader_fed
    clear()
    print("Your inventory:", player_inv)
    print(roomdesc.spaceinvroomexamine)
    input()
    spaceinv_room()

def portal_room():
    clear()
    print("Your inventory:", player_inv)
    print(roomdesc.portalroom)
    print("\nEnter the [portal]. Go [back] or [Examine] the room.\n")
    choice = input("> ")
    
    if "back" in choice:
        print("You've decided to go back to space invader room..")
        input()
        spaceinv_room()
    elif "portal" in choice:
        print("You've decided to jump into a portal. Let's see where it drops you..")
        input()
        spacecube_room()
    elif "examine" in choice:
        print("You've chosen to check the room for suspicious items..")
        input()
        portal_room_examine()
    else:
        print("It seems your choice was incorrect")
        input()
        moebius()

def portal_room_examine():
    clear()
    print("Your inventory:", player_inv)
    print(roomdesc.portalroomexamine)
    choice = input("> ")
    
    if "back" in choice:
        print("You've decided to go back to space invader room..")
        input()
        spaceinv_room()
    elif "pick" in choice:
        player_inv.append('cake')
        roomdesc.portalroomexamine = roomdesc.examined
        print("You put a cake in your inventory!")
        input()
        portal_room()
    else:
        print("It seems your choice was incorrect")
        input()
        moebius()

def spacecube_room():
    clear()
    print("Your inventory:", player_inv)
    print(roomdesc.spacecuberoom)
    print("\nGo back into the [portal]. Or maybe [examine] the room.\n")
    choice = input("> ")
    
    if "portal" in choice:
        print("You've decided to jump into a portal again.\nCrossed fingers give you a feeling that you will return..")
        input()
        portal_room()
    elif "examine" in choice:
        print("You've decided to look around")
        input()
        spacecube_room_examine()
    else:
        print("It seems your choice was incorrect")
        input()
        moebius()

def spacecube_room_examine():
    clear()
    print("Your inventory:", player_inv)
    print(roomdesc.spacecuberoomexamine)
    choice = input("> ")
    
    if "pick" in choice:
        player_inv.append('key')
        print("You put a key in your pocket!")
        input()
        roomdesc.spacecuberoomexamine = roomdesc.examined
        spacecube_room()
    elif "ignore" in choice:
        print("You decided to leave it alone")
        input()
        spacecube_room()
    else:
        print("It seems your choice was incorrect")
        input()
        moebius()

bear_fed = False

def bear_room():
    global bear_fed 
    clear()
    print("Your inventory:", player_inv)
    print(roomdesc.bearroom)
    print("\nMaybe try to [open] the door behind the bear. Go [back],\n[examine] the room, or [interact] with him (or her).")
    choice = input("> ")

    if "open" in choice and bear_fed is True:
        print("You've decided to open that door, let's see what's behind..")
        input()
        porch()
    elif "open" in choice and bear_fed is False:
        print("Angry bear doesn't give you a chance to pass by..")
        input()
        bear_room()
    elif "interact" in choice and "cake" in player_inv:
        print("You give cake to a bear. Yummy... happy..")
        player_inv.remove('cake')
        bear_fed = True
        input()
        bear_room()
    elif "interact" in choice and "cake" not in player_inv:
        print("Bear sniffs your nikes but refuses to move..")
        input()
        bear_room()
    elif "back" in choice:
        print("You've decided to go back..")
        input()
        first_room()
    elif "examine" in choice:
        print("You've decided to look around..")
        input()        
        bear_room_examine()
    else:
        print("It seems your choice was incorrect")
        input()
        moebius()

def bear_room_examine():
    clear()
    print("Your inventory:", player_inv)
    print(roomdesc.bearroomexamine)
    choice = input("> ")
    bear_room()

def porch():
    clear()
    print("Your inventory:", player_inv)
    print(roomdesc.porch)
    print("\nOpen the door and go [back]. Take a look [around].")
    choice = input("> ")

    if "back" in choice:
        print("Surprisingly you've decided to check bear again.")
        input()
        bear_room()
    elif "around" in choice:
        print("You've decided to check the surroundings..")
        input()
        porch_examine()
    else:
        print("It seems your choice was incorrect")
        input()
        moebius()

def porch_examine():
    clear()
    print("Your inventory:", player_inv)
    print(roomdesc.porchexamine)
    print("\nGo on, just [start] the car.")
    choice = input("> ")
    
    if "start" in choice and "key" in player_inv:
        print("You use key to start the car. Thanks god your journey is over.")
        input()
        endgame()
    elif "start" in choice and "key" not in player_inv:
        print("You try to short out the wires, but no luck. Try to find the car keys.")
        input()
        porch()
    else:
        print("It seems your choice was incorrect")
        input()
        moebius()        

mario_fed = False

def mario_room():
    clear()
    print("Your inventory:", player_inv)
    print(roomdesc.marioroom)
    print("\nOpen the [door] near him. Go [back],\n[Interact] with him or [Examine] the room.\n")
    global mario_fed
    
    choice = input("> ")
            
    if "door" in choice and mario_fed is True:
        print("You've decided to go forward.")
        input()
        coin_room()
    elif "door" in choice and mario_fed is False:
        print("That nasty red-cap blocks the way. Maybe you don't have nesseccary item in inventory.")
        input()
        mario_room()
    elif "interact" in choice and "mushroom" in player_inv:
        print("Mario gently takes the mushroom and starts eating it.")
        input()
        player_inv.remove('mushroom')
        mario_fed = True
        mario_room()
    elif "interact" in choice and "mushroom" not in player_inv:
        print("What are you going to give him? A big fat nothing?")
        input()
        mario_room()
    elif "back" in choice:
        print("You've decided to go back.")
        input()
        first_room()
    elif "examine" in choice:
        mario_room_examine()
    else:
        print("It seems your choice was incorrect")
        input()
        moebius()
  
def mario_room_examine():
    clear()
    print("Your inventory:", player_inv)
    print(roomdesc.marioroomexamine)
    input()
    mario_room()

def coin_room():
    clear()
    print("Your inventory:", player_inv)
    print(roomdesc.coinroom)
    print("\nGo [back] or [Examine] the room.\n")
    choice = input("> ")

    if "back" in choice:
        print("Somehow you've chosen to return to Mario")
        input()
        mario_room()
    elif "examine" in choice:
        print("Strange feeling tells you to check the room")
        input()
        coin_room_examine()
    else:
        print("It seems your choice was incorrect")
        input()
        moebius()

def coin_room_examine():
    clear()
    print("Your inventory:", player_inv)
    print(roomdesc.coinroomexamine)
    choice = input("> ")
    
    if "pick" in choice:
        player_inv.append('coin')
        print("You put a coin in your pocket!")
        roomdesc.coinroomexamine = roomdesc.examined
        input()
        coin_room()
    elif "ignore" in choice:
        print("You decided to leave it alone")
        input()
        coin_room()
    else:
        print("It seems your choice was incorrect")
        input()
        moebius()
        
def moebius():
    clear()
    print("\nStrange force draws you back and you find yourself in the beginning of your journey. \nThankfully that your inventory was not lost..")
    input()
    first_room()

def endgame():
    clear()
    print(roomdesc.ending)
    print("\nFantastic!")
    input()
    exit(0)

starter()