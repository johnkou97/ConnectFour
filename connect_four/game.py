from connect_four.board import Board

class ConnectFour:
    def __init__(self, players):
        self.board = Board()
        self.players = players

    def Play(self):
        '''
        Play the game of Connect Four.
        '''
        print("Welcome to Connect Four!")
        self.board.Display()

        turn = 0
        while True:
            current_player = self.players[turn % 2]
            print(f"{current_player.name}'s turn ({current_player.disc})")

            move = current_player.GetMove(self.board)
            self.board.DropDisc(move, current_player.disc)
            self.board.Display()

            if self.board.CheckWinner(current_player.disc):
                print(f"Congratulations! {current_player.name} wins!")
                break

            if self.board.CheckFull():
                print("The game is a draw!")
                break

            turn += 1