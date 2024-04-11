import random

user_ammo = 1
computer_ammo = 1

gameon = True

print('''Welcome to the game 007! You must beat our AI by choosing three choices! Shoot, Shield or Reload! If you shoot
    while the AI does not shield themselves, You Win! However, they can do the same thing to you.
    Watch your ammo count as you may need to reload!''')


def DBL07(computer_ammo, user_ammo):

    gameon = True

    choices = ['shoot', 'shield', 'reload']
    computer_choice = random.choices(choices, weights = [5,6,3])[0]
    user_choice = input("Enter your choice of Shoot, Shield, or Reload: ").lower()

    print("Your opponent chose:", computer_choice)
    print(user_choice)
    if user_choice not in choices:
        print(user_choice)
        print("Invalid choice. Please choose again from Shoot, Shield, or Reload.")
        

    elif user_choice == 'shoot':
        if computer_choice == 'shoot':
            if computer_ammo > 0 and user_ammo > 0:
                print("Tie!")
                gameon = False
            elif computer_ammo <= 0 and user_ammo > 0:
                print("You Win!")
                gameon = False
            elif computer_ammo > 0 and user_ammo < 0:
                print("You Lose")
                gameon = False
            elif computer_ammo < 0 and user_ammo < 0:
                print("No ammo, Try again")



        if computer_choice == 'reload':
            if user_ammo > 0:
                print("You win!")
                gameon = False
            elif user_ammo <= 0:
                print("You ran out of ammo! RELOAD!")
        elif computer_choice == 'shield':
            if user_ammo > 0:
                user_ammo -= 1
                print("Deflected!") 
            else:
                print("You ran out of ammo! RELOAD!")
        
               
    elif user_choice == 'shield':
        if computer_choice == 'shoot':
            if computer_ammo <= 0: 
                print("Computer out of ammo!")
            else:
                computer_ammo -= 1
                print("Deflected!")
            
        elif computer_choice == 'reload':
            computer_ammo += 1
        
    elif user_choice == 'reload':
        user_ammo += 1
        if computer_choice == 'reload':
            computer_ammo += 1
        elif computer_choice == 'shoot':
            if computer_ammo <= 0: 
                print("Computer out of ammo!")
            else:
                print("You lose")
                gameon = False
    
    
    return gameon, computer_ammo, user_ammo

while gameon:
    gameon, computer_ammo, user_ammo = DBL07(computer_ammo, user_ammo)