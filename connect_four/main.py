import argparse
from connect_four.game import ConnectFour
from connect_four.gui import ConnectFourGUI
from connect_four.player import setup_players

def launch_cli():
    """Launch the CLI version of Connect Four."""
    players = setup_players()
    game = ConnectFour(players)
    game.Play()

def launch_gui():
    """Launch the GUI version of Connect Four."""
    players = setup_players()
    ConnectFourGUI(players)

def main():
    """Decides mode based on arguments."""
    parser = argparse.ArgumentParser(description="Play Connect Four in CLI or GUI mode.")
    parser.add_argument("--gui", action="store_true", help="Run the game in GUI mode")
    args = parser.parse_args()

    if args.gui:
        launch_gui()
    else:
        launch_cli()

if __name__ == "__main__":
    main()
