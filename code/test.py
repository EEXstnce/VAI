

import random

#A function to flip the coin
def coin_flip():
    toss = random.choice(['Heads', 'Tails'])
    return toss

#A function to determine the winner
def determine_winner(player1,player2):
    toss = coin_flip()
    print("The coin was tossed and it landed on " + toss)
    if toss == player1:
        print("Player 1 wins!")
    elif toss == player2:
        print("Player 2 wins!")

#Initialize score count
player1_score = 0
player2_score = 0

#Initialize game loop
game_over = False

while game_over == False:
    player1 = input("Player 1, call heads or tails: ")
    player2 = input("Player 2, call heads or tails: ")
    determine_winner(player1,player2)
    if player1 == toss:
        player1_score += 1
    elif player2 == toss:
        player2_score += 1
    
    print("Player 1 score: " + str(player1_score))
    print("Player 2 score: " + str(player2_score))
    if player1_score == 5:
        print("Player 1 wins the game!")
        game_over = True
    elif player2_score == 5:
        print("Player 2 wins the game!")
        game_over = True
