from random import randrange


while True: # INFINITE LOOP
    userInput = input("Gozine khod ra vared konid (sang, kaqaz, qeichi): ")   # GET INPUT FROM USER
    options = ["sang" , "kaqaz" , "qeichi"] # OPTIONS USED IN GAME
    if userInput != options: # CHECK IF USERINPUT IS IN OPTIONS
        print("Lotfan yeki az gozine haie (sang, kaqaz, qeichi) ra entekhab konid!!!")
        userInput = input("Gozine khod ra vared konid (sang, kaqaz, qeichi): ")
    random_index = randrange(len(options)) # CHOOSE RANDOM LEN OF OPTIONS LIST
    computerChoose = options[random_index] # CHOOSE A RANDOM OPTION
    computerChooseTxt = "Entekhab Computer: %s" % computerChoose

    if computerChoose == userInput: # GAME RULES
        print("Barbar Shodid!" , computerChooseTxt)
    elif computerChoose == "sang" and userInput == "qeichi":
        print("Shoma Bakhtid!", computerChooseTxt)
    elif computerChoose == "sang" and userInput == "kaqaz":
        print("Shoma Bordid!" , computerChooseTxt)
    elif computerChoose == "kaqaz" and userInput == "qeichi":
        print("Shoma Bordid!" , computerChooseTxt)
    elif computerChoose == "kaqaz" and userInput == "sang":
        print("Shoma Bakhtid!" , computerChooseTxt)
    elif computerChoose == "qeichi" and userInput == "kaqaz":
        print("Shoma Bakhtid!" , computerChooseTxt)
    elif computerChoose == "qeichi" and userInput == "sang":
        print("Shoma Bordid!", computerChooseTxt) 
