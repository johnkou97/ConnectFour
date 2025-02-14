from connect_four.game import ConnectFour
from connect_four.player import Player


def SetPlayers():
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


def main():
    print("Welcome to Connect Four!")
    players = SetPlayers()
    game = ConnectFour(players)
    game.Play()


if __name__ == "__main__":
    main()
