import argparse
from connect_four.cli import ConnectFourCLI
from connect_four.gui import ConnectFourGUI
from connect_four.player import setup_players

def launch_cli() -> None:
    '''
    Launch the CLI version of Connect Four.
    '''
    players = setup_players()
    game = ConnectFourCLI(players)
    game.play()

def launch_gui() -> None:
    '''
    Launch the GUI version of Connect Four.
    '''
    players = setup_players()
    ConnectFourGUI(players)

def main() -> None:
    '''
    Decides mode based on arguments.
    '''
    parser = argparse.ArgumentParser(description="Play Connect Four in CLI or GUI mode.")
    parser.add_argument("--gui", action="store_true", help="Run the game in GUI mode")
    args = parser.parse_args()

    if args.gui:
        launch_gui()
    else:
        launch_cli()

if __name__ == "__main__":
    main()
