import tkinter as tk

# Global Variables
current_player = "A"
buttons = []

  
def winner_conditions(board):
    # Check rows and columns
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != "":
            return board[row][0]  # Return winner (X or O)

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != "":
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0]
    
    if board[0][2] == board[1][1] == board[2][0] != "":
        return board[0][2]

    return None

def get_winner(player_label):
    map = []
    for row in range(3):
        add_row = []
        for column in range(3):
            add_row.append(buttons[row][column].cget("text"))
        map.append(add_row)

    winner = winner_conditions(map)
    if winner:
        player_label.config(text=f"Player {winner} wins", bg="yellow", font=('consolas', 20))
        restart_button=tk.Button(text="Play Again?", bg="light green", font=('consolas', 20),command=lambda: restart_game(player_label,restart_button))
        restart_button.grid(row=4, column=0, columnspan=3, pady=(10, 10)) 

def restart_game(player_label,restart_button):
    global current_player

    
    # Reset the current player
    current_player = "A"
    
    # Clear the button texts and enable them
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text="", bg="#d9d9d9", state=tk.NORMAL)
   
    # Reset the player label, destroy restart button
    player_label.config(text=f"Player {current_player}'s turn", bg="light blue",font=('consolas', 10))
    restart_button.destroy()
    
def checked(r, c, player):
    global current_player
    
    if current_player == "A":
        buttons[r][c].config(text="X", bg="light blue", state=tk.DISABLED)
        current_player = "B"
        player.config(text=f"Player {current_player}'s turn", bg="#FFCCCC")

    else:
        current_player = "A"
        buttons[r][c].config(text="O", bg="#FFCCCC", state=tk.DISABLED)
        player.config(text=f"Player {current_player}'s turn", bg="light blue")

    
    get_winner(player)

def create_buttons(player):
    global buttons
    for row in range(3):
        button_row = []
        for col in range(3):
            b = tk.Button(height=5, width=10, command=lambda r=row, c=col: checked(r, c, player))            
            b.grid(row=row+1, column=col)
            button_row.append(b)
        buttons.append(button_row)

def main():
    window = tk.Tk()
    window.title=("Tic Tac Toe")
    window.minsize(width="300", height="300")

    player = tk.Label(text=f"Player {current_player}'s turn",bg="light blue",font=('consolas', 10))
    player.grid(row=0,column=1)
    player.grid(row=0, column=0, columnspan=3, pady=(10, 10)) 

    create_buttons(player)

    window.mainloop()

if __name__ == "__main__":
    main()
