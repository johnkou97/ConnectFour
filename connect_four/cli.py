from connect_four.board import Board

class ConnectFourCLI:
    def __init__(self, players):
        self.board = Board()
        self.players = players

    def play(self) -> None:
        '''
        Play the game.
        '''
        print("Welcome to Connect Four (CLI Mode)!")
        self.board.display()

        turn = 0
        while True:
            current_player = self.players[turn % 2]
            print(f"{current_player.name}'s turn ({current_player.disc})")

            move = current_player.get_move(self.board)
            self.board.drop_disc(move, current_player.disc)
            self.board.display()

            if self.board.check_winner(current_player.disc):
                print(f"Congratulations! {current_player.name} wins!")
                break

            if self.board.is_full():
                print("The game is a draw!")
                break

            turn += 1
