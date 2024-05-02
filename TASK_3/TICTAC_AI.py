#created an AI TIC-TAC-TOE using Minimax Algorithm
import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
        self.current_player = 'X'
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.create_buttons()
    
    def create_buttons(self):
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.root, text='', font=('Arial', 40), width=3, height=1,
                                                command=lambda i=i, j=j: self.make_move(i, j))
                self.buttons[i][j].grid(row=i, column=j)
    
    def make_move(self, i, j):
        if self.board[i][j] == '' and self.current_player != 'O':
            self.board[i][j] = self.current_player
            self.buttons[i][j].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("Winner", f"{self.current_player} wins!")
                self.reset_board()
            elif self.check_tie():
                messagebox.showinfo("Tie", "It's a tie!")
                self.reset_board()
            else:
                self.current_player = 'O'
                self.computer_move()

    def computer_move(self):
        best_score = -float('inf')
        best_move = None
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == '':
                    self.board[i][j] = 'O'
                    score = self.minimax(self.board, False)
                    self.board[i][j] = ''
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)
        if best_move:
            i, j = best_move
            self.board[i][j] = 'O'
            self.buttons[i][j].config(text='O')
            if self.check_winner():
                messagebox.showinfo("Winner", "Computer wins!")
                self.reset_board()
            elif self.check_tie():
                messagebox.showinfo("Tie", "It's a tie!")
                self.reset_board()
            else:
                self.current_player = 'X'

    def minimax(self, board, is_maximizing):
        if self.check_winner():
            return -1 if is_maximizing else 1
        elif self.check_tie():
            return 0
        if is_maximizing:
            best_score = -float('inf')
            for i in range(3):
                for j in range(3):
                    if board[i][j] == '':
                        board[i][j] = 'O'
                        score = self.minimax(board, False)
                        board[i][j] = ''
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(3):
                for j in range(3):
                    if board[i][j] == '':
                        board[i][j] = 'X'
                        score = self.minimax(board, True)
                        board[i][j] = ''
                        best_score = min(score, best_score)
            return best_score
    
    def check_winner(self):
        # Check rows
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != '':
                return True
        # Check columns
        for j in range(3):
            if self.board[0][j] == self.board[1][j] == self.board[2][j] != '':
                return True
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != '':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != '':
            return True
        return False
    
    def check_tie(self):
        for row in self.board:
            for cell in row:
                if cell == '':
                    return False
        return True
    
    def reset_board(self):
        for i in range(3):
            for j in range(3):
                self.board[i][j] = ''
                self.buttons[i][j].config(text='')
        self.current_player = 'X'

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()
