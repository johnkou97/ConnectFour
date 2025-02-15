import random
import tkinter as tk
from tkinter import messagebox
from connect_four.board import Board

class ConnectFourGUI:
    def __init__(self, players):
        self.board = Board()
        self.players = players
        self.current_player_index = 0
        self.game_running = True

        self.root = tk.Tk()
        self.root.title("Connect Four")
        self.buttons = []
        self.labels = []

        self.create_widgets()
        self.root.after(100, self.check_computer_turn)  # Start checking for AI moves
        self.root.mainloop()

    def create_widgets(self) -> None:
        '''
        Create the GUI elements for the game.
        '''
        frame = tk.Frame(self.root)
        frame.pack()

        for col in range(self.board.columns):
            button = tk.Button(frame, text=f"Col {col + 1}", command=lambda c=col: self.handle_move(c))
            button.grid(row=0, column=col)
            self.buttons.append(button)

        for row in range(self.board.rows):
            label_row = []
            for col in range(self.board.columns):
                label = tk.Label(frame, text=".", width=4, height=2, relief="ridge", bg="white", font=("Arial", 16))
                label.grid(row=row + 1, column=col, padx=2, pady=2)
                label_row.append(label)
            self.labels.append(label_row)

    def handle_move(self, column: int) -> None:
        '''
        Handle a move by a human player.
        '''
        if not self.game_running:
            return

        current_player = self.players[self.current_player_index]
        if not current_player.is_human:
            return

        result = self.board.drop_disc(column, current_player.disc)
        if result:
            self.update_board(result, current_player.disc)
            if self.check_game_over(current_player):
                return
            self.switch_player()

    def update_board(self, position: tuple, disc: str) -> None:
        '''
        Update the game board with the new disc.
        '''
        row, col = position
        self.labels[row][col].config(text=disc, bg="yellow" if disc == "O" else "red")

    def switch_player(self) -> None:
        '''
        Switch to the next player.
        '''
        self.current_player_index = 1 - self.current_player_index

    def check_computer_turn(self) -> None:
        '''
        Check if it is the computer's turn to move.
        '''
        if not self.game_running:
            return

        current_player = self.players[self.current_player_index]
        if not current_player.is_human:
            valid_columns = [col for col in range(self.board.columns) if self.board.grid[0][col] == "."]
            if valid_columns:
                column = random.choice(valid_columns)
                result = self.board.drop_disc(column, current_player.disc)
                if result:
                    self.update_board(result, current_player.disc)
                    if self.check_game_over(current_player):
                        return
                    self.switch_player()

        self.root.after(500, self.check_computer_turn)

    def check_game_over(self, player) -> bool:
        '''
        Check if the game is over.
        '''
        if self.board.check_winner(player.disc):
            self.game_running = False
            self.show_end_dialog(f"{player.name} ({player.disc}) wins!")
            return True
        elif self.board.is_full():
            self.game_running = False
            self.show_end_dialog("It's a draw!")
            return True
        return False

    def show_end_dialog(self, message: str) -> None:
        '''
        Show the end game dialog.
        '''
        response = messagebox.askyesno("Game Over", f"{message}\nDo you want to play again?")
        if response:
            self.reset_game()
        else:
            self.root.destroy()

    def reset_game(self) -> None:
        '''
        Reset the game.
        '''
        self.board = Board()
        self.current_player_index = 0
        self.game_running = True
        for row in self.labels:
            for label in row:
                label.config(text=".", bg="white")

        self.root.after(100, self.check_computer_turn)
