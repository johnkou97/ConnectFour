import random

class Player:
    '''
    Player class to represent a player in the game.
    '''
    def __init__(self, name, disc, is_human=True):
        self.name = name
        self.disc = disc
        self.is_human = is_human

    def get_move(self, board) -> int:
        '''
        Get the player's move.
        If the player is human, prompt for input.
        If the player is a computer, choose a random valid move.
        '''
        if self.is_human:
            while True:
                try:
                    column = int(input(f"{self.name}, choose a column (1-7): ")) - 1
                    if 0 <= column < board.columns and board.grid[0][column] == ".":
                        return column
                    else:
                        print("Invalid move. Try again.")
                except ValueError:
                    print("Please enter a valid number.")
        else:
            valid_columns = [col for col in range(board.columns) if board.grid[0][col] == "."]
            return random.choice(valid_columns)

def setup_players() -> list:
    '''
    Set the players for the game.
    Ask for input to determine if each player is human or computer.
    '''
    players = []
    for i, disc in enumerate(["O", "X"], start=1):
        while True:
            player_type = input(f"Is Player {i} (Disc: {disc}) a Human or Computer? (h/c): ").strip().lower()
            if player_type in ("h", "c"):
                name = f"Player {i}" if player_type == "h" else f"Computer {i}"
                is_human = player_type == "h"
                players.append(Player(name, disc, is_human))
                break
            else:
                print("Invalid input. Please enter 'h' for Human or 'c' for Computer.")
    return players
