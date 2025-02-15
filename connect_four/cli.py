from connect_four.board import Board

class ConnectFourCLI:
    def __init__(self, players):
        self.board = Board()
        self.players = players

    def play(self):
        print("Welcome to Connect Four (CLI Mode)!")
        self.board.Display()

        turn = 0
        while True:
            current_player = self.players[turn % 2]
            print(f"{current_player.name}'s turn ({current_player.disc})")

            move = current_player.get_move(self.board)
            self.board.DropDisc(move, current_player.disc)
            self.board.Display()

            if self.board.CheckWinner(current_player.disc):
                print(f"Congratulations! {current_player.name} wins!")
                break

            if self.board.CheckFull():
                print("The game is a draw!")
                break

            turn += 1
