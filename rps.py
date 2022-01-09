"""
Basic user input rock paper scissors.
Date: Feb 24, 2020

"""
from os import system
import time

def evaluate_turn(move1, move2):
    """ 
    Compare each players move to see if someone won. 
        Params:
            player1: player 1's move
            player2: player 2's move
    """
    if move1 == "rock":
        if move2 == "scissors":
            return move1, "Player 1"
        elif move2 == "paper":
            return move2, "Player 2"
    
    if move1 == "scissors":
        if move2 == "rock":
            return move2, "Player 2"
        elif move2 == "paper":
            return move1, "Player 1"
    
    if move1 == "paper":
        if move2 == "rock":
            return move1, "Player 1"
        elif move2 == "scissors":
            return move2, "Player 2"

    if move1 == move2:
        return None, None

def verify_move(move):
    # Check if the user input is a valid move.
    # Make the user re-enter their move if its not valid.
    acceptable_moves = ["rock", "Rock", "paper", "Paper", "Scissors", "scissors"]
    acceptable_move = False

    while acceptable_move != True:
        if move in acceptable_moves:
            acceptable_move = True
            return True
        else:
            move = input("ERROR: Invalid move!\nPlease enter either rock, paper or scissors: \n")
        

def setup_game():
    system('cls')
    print("Please enter either: rock, paper or scissors: ")

    win = False
    while win != True:
        system('color D')
        player1 = input("Player 1: Enter your move: ")
        if verify_move(player1):

            system('cls')
            system('color B')
            player2 = input("Player 2: Enter your move: ")
            verify_move(player2)
            system('cls')

            if verify_move(player2):
                winning_move, winner = evaluate_turn(player1, player2)

                for i in range(3, 0, -1):
                    print(f"{i}!")
                    time.sleep(1)
                system('cls')
                
                print(f"Player 1: {player1} vs Player 2: {player2}")

                if winning_move is not None:
                    print(f"The winner was {winner}, since they guessed {winning_move}.")
                elif winning_move is None:
                    print("This round is a tie!")

        restart = input("Type quit to close, or any key to play again.\n")
        if restart == "quit":
            win = True
        else:
            win = False


def main():
    system('cls')
    setup_game()

main()






