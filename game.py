#Imports
import random

#Varibales
rock = "rock"
paper = "paper"
scissor = "scissor"
morechoices = ["r" , "p" , "s" , paper, rock , scissor]
choices = [ paper, rock , scissor]
yesnolist = ["y" , "n" , "yes" , "no"]
win = "You win"
lose = "you lose"
your_score = 0
comupter_score = 0

print("Welcome to my game")

while True :
    playagain = None
    player = None
    computer = random.choice(choices)
    computer_choice = "computer: " + computer
    while player  not in morechoices:
         player = input('rock(r) , paper(p) or scissor(s)? ').lower()
         
    if player == "r":
        player = rock
    elif player == "p":
        player = paper
    elif player == "s":
        player = scissor
    else:
        player= player

    if player == computer:
        print(computer_choice)
        print('it is a tie')
    elif player == scissor:
        if computer == rock: 
            print(computer_choice)      
            print(lose)
            comupter_score += 1
        elif computer == paper:
            print(computer_choice)     
            print(win)
            your_score += 1
    elif player == rock:
        if computer == paper:
            comupter_score += 1
            print(computer_choice)
            print(lose)
        else:
            print(computer_choice)    
            print(win)
            your_score += 1
    elif player == paper:
        if computer == rock:
            your_score += 1  
            print(computer_choice)    
            print(win)
        else:
            comupter_score += 1  
            print(computer_choice)
            print(lose)

    showscore = "Your score: " + str(your_score) + '  -  ' + "Computer score: "+ str(comupter_score)
    print(showscore)
    while playagain  not in yesnolist:
          playagain = input("play_again : Yes or No or y/n: ").lower()
    if playagain == "n":
       playagain = "no"
 
    if playagain == "no":
        print(showscore)
        break
    else:
        print("Lets gooo")

print("bye bye, Thank you so much for playing our game \nCredit : Ahmed Fouad & Eslam Fouad")