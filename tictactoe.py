'''
Purpose: TicTacToeCZ.py will allow the user to play a Tic-Tac-Toe game

Author: Catherine Zhang

Creation Date:: 04/06/2021

Edited by: Catherine Zhang, 17/04/2023
'''
# Allows Pygame Zero to be run from Wing and other IDE's
import pgzrun

# Sets the screen size
WIDTH = 350
HEIGHT = 300

#Starting turn is x
turn = "X"

#Create 9 region
region1 = Rect((0, 0), (100, 100))
region2 = Rect((100, 0), (100, 100))
region3 = Rect((200, 0), (100, 100))
region4 = Rect((0, 100), (100, 100))
region5 = Rect((100,100 ), (100, 100))
region6 = Rect((200, 100), (100, 100))
region7 = Rect((0, 200), (100, 100))
region8 = Rect((100, 200), (100, 100))
region9 = Rect((200, 200), (100, 100))

#Determind either x or o occupied the spot
s1 = ""
s2 = ""
s3 = ""
s4 = ""
s5 = ""
s6 = ""
s7 = ""
s8 = ""
s9 = ""

#Check if the user made a valid move
move = "1"

#Winner statement after a user win
winner = ""

#Check if the winning result is met
xWin = 0
oWin = 0
    
     

# Function that is responsible for drawing everything on the screen
def draw ():
    #Black background
    screen.fill ((0,0,0))
    
    #Seperate the screen to 9 regions 
    screen.draw.line ((300,100 ), (0, 100), (255,255,255))
    screen.draw.line ((300,200), (0, 200), (255,255,255))
    screen.draw.line ((100,0 ), (100, 300), (255,255,255))
    screen.draw.line ((200,0 ), (200, 300), (255,255,255))
    screen.draw.line ((300,0 ), (300, 300), (255,255,255))
     
    #Show whose turn it is
    screen.draw.text( turn,  (315,140),    color="red",  fontsize=50)
    
    #Fill the squares with text
    screen.draw.text (s1,      (40,35),    color="blue",  fontsize=50 )
    screen.draw.text (s2,      (140,35),    color="blue",  fontsize=50 )
    screen.draw.text (s3,      (240,35),    color="blue",  fontsize=50 )
    screen.draw.text (s4,      (40,135),    color="blue",  fontsize=50 )
    screen.draw.text (s5,      (140,135),    color="blue",  fontsize=50 )
    screen.draw.text (s6,      (240,135),    color="blue",  fontsize=50 )
    screen.draw.text (s7,      (40,235),    color="blue",  fontsize=50 )
    screen.draw.text (s8,      (140,235),    color="blue",  fontsize=50 )
    screen.draw.text (s9,      (240,235),    color="blue",  fontsize=50 )
    
    #Show the winner statement on the screen
    screen.draw.text( winner, (100, 130), color="green", fontsize = 30)
    
    
# Function that is responsible for handling mouse release events
def on_mouse_up(pos, button):
    if xWin == 0 and oWin == 0:
        global turn, move, s1,s2,s3,s4,s5,s6,s7,s8,s9
       
        #check to see which region has been clicked 
        if turn == "X":
            if region1.collidepoint(pos) and s1 == "":
                        s1 = "X"
                        move = "1"
            if region2.collidepoint(pos) and s2 == "":
                        s2 = "X"
                        move = "1"
            if region3.collidepoint(pos) and s3 == "":
                        s3 = "X"
                        move = "1"
            if region4.collidepoint(pos) and s4 == "":            
                        s4 = "X"
                        move = "1"
            if region5.collidepoint(pos) and s5 == "":
                        s5 = "X"
                        move = "1"
            if region6.collidepoint(pos) and s6 == "":
                        s6 = "X"
                        move = "1"
            if region7.collidepoint(pos) and s7 == "":
                        s7 = "X"
                        move = "1"
            if region8.collidepoint(pos) and s8 == "":
                        s8 = "X"
                        move = "1"
            if region9.collidepoint(pos) and s9 == "":
                        s9 = "X"
                        move = "1"
                                  
        #check to see which region has been clicked    
        if turn == "O":
            if region1.collidepoint(pos) and s1 == "":
                        s1 = "O"
                        move = "0"
            if region2.collidepoint(pos) and s2 == "":
                        s2 = "O"
                        move = "0"
            if region3.collidepoint(pos) and s3 == "":
                        s3 = "O"
                        move = "0"
            if region4.collidepoint(pos) and s4 == "":
                        s4 = "O"
                        move = "0"
            if region5.collidepoint(pos) and s5 == "":
                        s5 = "O"
                        move = "0"
            if region6.collidepoint(pos) and s6 == "":
                        s6 = "O"
                        move = "0"
            if region7.collidepoint(pos) and s7 == "":
                        s7 = "O"
                        move = "0"
            if region8.collidepoint(pos) and s8 == "":
                        s8 = "O"
                        move = "0"
            if region9.collidepoint(pos) and s9 == "":
                        s9 = "O"
                        move = "0"
                                 
        #show whose turn it is
        if turn == "X"and move == "1":
            turn = "O"
        elif turn == "O" and move == "0": 
            turn = "X"
 

def update():
    global xWin, oWin, winner, s1,s2,s3,s4,s5,s6,s7,s8,s9
    #Determind if X has win
    if s1 == "X" and s2 == "X"and s3 == "X":
        xWin = 1
    elif s4 == "X"and s5 == "X"and s6 == "X":
        xWin = 1
    elif s7 == "X"and s8 == "X"and s9 == "X":
        xWin = 1 
    elif s1 == "X"and s4== "X" and s7 == "X":
        xWin = 1    
    elif s2 == "X"and s5 == "X"and s8 == "X":
        xWin = 1 
    elif s3 == "X"and s6 == "X"and s9 == "X":
        xWin = 1 
    elif s1 == "X"and s5 == "X"and s9 == "X":
        xWin = 1   
    elif s3 == "X"and s5 == "X"and s7 == "X":
        xWin = 1 
        
    #Determind if O has win
    if s1 == "O"and s2 == "O"and s3 == "O":
        oWin = 1
    elif s4 == "O"and s5 == "O"and s6 == "O":
        oWin = 1
    elif s7 == "O"and s8 == "O"and s9 == "O":
        oWin = 1 
    elif s1 == "O"and s4 == "O"and s7 == "O":
        oWin = 1    
    elif s2 == "O"and s5== "O" and s8 == "O":
        oWin = 1 
    elif s3 == "O"and s6 == "O"and s9 == "O":
        oWin = 1 
    elif s1 == "O"and s5 == "O"and s9 == "O":
        oWin = 1   
    elif s3 == "O"and s5 == "O"and s7 == "O":
        oWin = 1   
        
       
    #When the winning condition is meet, it winner statement will appear
    if xWin == 1:
        winner = "X is the winner"
    elif oWin == 1:
        winner = "O is the winner"
    elif (s1 != "" and s2 != "" and s3 != "" and s4 != "" and 
        s5 != "" and s6 != "" and s7 != "" and s8 != ""):
        winner = "No Winner, Tie!"   

# Runs the Pygame Zero file
pgzrun.go()   


