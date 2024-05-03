import tkinter as tk
current_player = "A"
buttons=[]

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
def get_winner():
    map=[]
    for row in range(3):
        add_row = []
        for column in range(3):
            add_row.append(buttons[row][column].cget("text"))
        map.append(add_row)
    if winner_conditions(map) != None:
        print(f"Player {winner_conditions(map)} wins")
            

def checked(r,c):
    global current_player
  
    if current_player == "A":
        buttons[r][c].config(text="X", bg="light blue", state=tk.DISABLED)
        current_player = "B"
    else:
        current_player = "A"
        buttons[r][c].config(text="O", bg="red", state=tk.DISABLED)

    get_winner()

    
def create_buttons():
    global buttons
    for row in range(3):
        button_row=[]
        for col in range(3):
            b = tk.Button(height=5, width=10, command=lambda r=row, c=col: checked(r, c))            
            b.grid(row=row, column=col)
            button_row.append(b)
        buttons.append(button_row)
    
window = tk.Tk()
window.title=("Tic Tac Toe")
window.minsize(width="300",height="300")

create_buttons()

window.mainloop()
