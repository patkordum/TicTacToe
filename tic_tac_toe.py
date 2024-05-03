import tkinter as tk
from tkinter import simpledialog

# Global Variables
current_player = ""
player_a_name = ""
player_b_name = ""
buttons = []

def winner_conditions(board):
    """Check if there's a winner."""
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
    """Check for the winner and update UI."""
    map = [[buttons[i][j].cget("text") for j in range(3)] for i in range(3)]

    winner = winner_conditions(map)
    if winner:
        if winner == "X":
            winner_name = player_a_name
            color = "light blue"
        else:
            winner_name = player_b_name
            color = "#FFCCCC"

        player_label.config(text=f"{winner_name} wins", bg=color, font=('consolas', 20))
        restart_button = tk.Button(text="Play Again?", bg="light green", font=('consolas', 20), command=lambda: restart_game(player_label, restart_button))
        restart_button.grid(row=4, column=0, columnspan=3, pady=(10, 10))
    elif all(map[row][col] for row in range(3) for col in range(3)):
        player_label.config(text="It's a TIE!", bg="yellow", font=('consolas', 20))
        restart_button = tk.Button(text="Play Again?", bg="light green", font=('consolas', 20), command=lambda: restart_game(player_label, restart_button))
        restart_button.grid(row=4, column=0, columnspan=3, pady=(10, 10))

def restart_game(player_label, restart_button):
    """Reset the game."""
    global current_player

    # Reset the current player
    current_player = player_a_name

    # Clear the button texts and enable them
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text="", bg="#d9d9d9", state=tk.NORMAL)

    # Reset the player label, destroy restart button
    player_label.config(text=f"{current_player}'s turn", bg="light blue", font=('consolas', 10))
    restart_button.destroy()

def checked(r, c, player_label):
    """Mark the button clicked and check for the winner."""
    global current_player
    if current_player == player_a_name:
        symbol = "X"
        color = "light blue"
        player_label.config(text=f"{player_b_name}'s turn", bg="#FFCCCC")
        current_player = player_b_name
        
    else:
        symbol = "O"
        color = "#FFCCCC"
        player_label.config(text=f"{player_a_name }'s turn", bg="light blue")
        current_player = player_a_name     
   
    buttons[r][c].config(text=symbol, bg=color, state=tk.DISABLED)
    get_winner(player_label)

def create_buttons(player_label):
    """Create buttons for the game grid."""
    global buttons
    for row in range(3):
        button_row = []
        for col in range(3):
            b = tk.Button(height=5, width=10, command=lambda r=row, c=col: checked(r, c, player_label))
            b.grid(row=row+1, column=col)
            button_row.append(b)
        buttons.append(button_row)

def get_names():
    """Prompt users to enter player names."""
    global player_a_name, player_b_name, current_player
    player_a_name = simpledialog.askstring("Player A's Name", "Enter Player A's Name:")
    player_b_name = simpledialog.askstring("Player B's Name", "Enter Player B's Name:")
    current_player = player_a_name

def main():
    """Main function to run the Tic Tac Toe game."""
    # Get names of players
    get_names()

    # Initialize the Tkinter window
    window = tk.Tk()
    window.title("Tic Tac Toe")
    window.minsize(width="300", height="300")

    # Create player label
    player = tk.Label(text=f"{current_player}'s turn", bg="light blue", font=('consolas', 10))
    player.grid(row=0, column=1)
    player.grid(row=0, column=0, columnspan=3, pady=(10, 10))

    # Create game grid buttons
    create_buttons(player)

    # Start the Tkinter event loop
    window.mainloop()

if __name__ == "__main__":
    main()
