#grab imports
import random
#input
#process
#output
#building a darts counter

#need to get bot to have their turn after each score entered by user has been confirmed


#user inputs their score : lowest is 0 and highest is 180
#need to check if the input is an integer
#user can choose what the starting score should be : 501 or 301
#need to do score: 501/301 - score
#need to have the bot randomly generate a score from 0 - 180 using a for loop implementing random.randint()
#game ends when user or bot reaches 0
#creating a player 2 to play against player 1


#creating function for user to choose if they want to play
def start_game():
    play = input("Would you like to play darts? (Y/N): ")
    if play == "Y" or play == "y":
        sel_score()
    else:
        print("Okay. Goodbye")
        quit()

Player1 = ""
Player2 = ""
#creating UserInput as a global variable
def num_range_check():
    while True :
        global score, score1
      
        Player1 = input("Player 1, enter your score: ")
        try:
             if Player1.strip("-").isdigit():

            #new variable to pass input as an integer
                score = int(Player1)
            #checking input to see if it's in range
        
                if  0 <= score <= 180:
                    print(score)
                    break
                elif score and score1 < 0:
                    print("number not in range of 0 - 180")
                elif score and score1 > 180:
                    print("number not in range of 0 - 180")
        #check if score is all digits and is positive
        except ValueError:
            print("You can only enter whole numbers")  
   

def Player2():
      global score1
      while True :
        
        Player2 = input("Player 2, enter your score: ")
        try:
        #check if score is all digits and is positive
                if Player2.strip("-").isdigit():

            #new variable to pass input as an integer
                    score1 = int(Player2)
            #checking input to see if it's in range
                    if score1 >= 0 and score1 <= 180:
                        print(score1)
                        break
                    elif score1 < 0:
                        print("number not in range of 0 - 180")
                    elif score1 > 180:
                        print("number not in range of 0 - 180")
        except ValueError:
            print("You can only enter whole numbers")

        

    


#score that user will start on
def sel_score():
    while True:
        global select1
        global select2
       
        select = input("Would you like to start on 501 or 301? ")
        if select.isdigit():
            select1 = int(select)
            select2 = select1
            
            if select1 == 501 or select1 == 301:
                game_on()
                break
            else:
                print("You can only choose 501 or 301")
        else:
            print("Invalid input, choose between 501 and 301")

def game_on():
    global select1, score, score1, select2
   
    while True:
        num_range_check()

        select1 -= score
        print("Player 1 is on: ", select1)
        if select1 == 0:
            print("Player 1 has won the game!")
            break
        bot_num
        select2 -= score1
        print("Player 2 is on: ", select2)
        if select2 == 0:
            print("Player 2 has won the game!")
            break
        if select1 < 0:
            print("Player 1 has gone bust. Player 2 wins!")
            break
        if select2 < 0:
            print("Player 2 has gone bust. Player 1 has won!")
        
            

  
            


#creating bot score
def bot_num():
    global select2, bot_score
    bot_score = random.randint(0,180)

    print(f"the bot scored: {bot_score}")
     




start_game()
