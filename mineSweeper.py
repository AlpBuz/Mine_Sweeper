import tkinter as tk
from tkinter import messagebox
import random

#-----Global Variables-------------
rows = 8
columns = 8
grid = [[" " for _ in range(rows+2)] for _ in range(columns+2)]
buttons = [[" " for _ in range(rows)] for _ in range(columns)]
firstClick = True
overlaw = None
menuFrame, menuLabel = None, None
gameScreen = None
#---------------------------------

def buttonClick(row, col, root):
    global grid, buttons, firstClick
    
    if firstClick:
        firstClickGridChange(row + 1, col + 1)
        firstClickChange(row, col)
    else:
        if grid[row + 1][col + 1] == " ":
            bombs = checkSurrondingsBomb(row + 1, col + 1)
            buttons[row][col].config(text=str(bombs))
            if bombs == 0:
                revealConnectedCells(row, col)
            win = checkWinner()
            if win:
                revalAll()
                showWinner(root)
        else:
            buttons[row][col].config(text="X", fg="red")
            showGameOver(root)


def checkSurrondingsBomb(row, column):
    reVal = 0
    if grid[row - 1][column - 1] == "X":
        reVal += 1
    if grid[row - 1][column] == "X":
        reVal += 1
    if grid[row - 1][column + 1] == "X":
        reVal += 1
    if grid[row][column - 1] == "X":
        reVal += 1
    if grid[row][column + 1] == "X":
        reVal += 1
    if grid[row + 1][column - 1] == "X":
        reVal += 1
    if grid[row + 1][column] == "X":
        reVal += 1
    if grid[row + 1][column + 1] == "X":
        reVal += 1
    return reVal



def revealConnectedCells(row, col):
    global grid, buttons, rows, columns

    # Directions including diagonals
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    
    # Stack for Depth-First Search (DFS)
    stack = [(row, col)]
    
    # Set for tracking visited cells
    visited = set()

    while stack:
        current_row, current_col = stack.pop()

        if (current_row, current_col) in visited:
            continue
        visited.add((current_row, current_col))

        # Skip if out of bounds
        if current_row < 0 or current_row >= rows or current_col < 0 or current_col >= columns:
            continue

        # Skip if cell contains a bomb
        if grid[current_row + 1][current_col + 1] == "X":
            continue

        

        bombs = checkSurrondingsBomb(current_row + 1, current_col + 1)
        buttons[current_row][current_col].config(text=str(bombs))

        # If there are no bombs around the current cell, reveal adjacent cells
        if bombs == 0:
            for deltaRow, deltaCol in directions:
                newRow, newCol = current_row + deltaRow, current_col + deltaCol
                if (newRow < 0 or newRow >= rows) or (newCol < 0 or newCol >= columns):
                    if (newRow, newCol) not in visited:
                        stack.append((newRow, newCol))
                else:
                    #if section is already visited or the spot has been revealed already skip it
                    if (newRow, newCol) not in visited or buttons[newRow][newCol]["text"] != " ":
                        stack.append((newRow, newCol))



def revalAll():
    global grid, buttons, rows, columns

    for row in range(rows):
        for col in range(columns):
            if buttons[row][col]["text"] == " ":
                buttons[row][col].config(text=str(grid[row + 1][col + 1]), fg="red")


def firstClickChange(row, col):
    global firstClick, grid, buttons, rows, columns

    firstClick = False

    buttons[row][col].config(text=str(checkSurrondingsBomb(row + 1, col + 1)))

    # Define the directions to check the surrounding cells
    directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]

    for drow, dcol in directions:
        new_row = row + drow
        new_col = col + dcol

        # Check if the new position is within the grid boundaries
        if 0 <= new_row < rows and 0 <= new_col < columns:
            bombs = checkSurrondingsBomb(new_row + 1, new_col + 1)
            buttons[new_row][new_col].config(text=str(bombs))
            

def firstClickGridChange(row, col):
    grid[row][col] = " "

    grid[row - 1][col] = " "
        
    grid[row][col - 1] = " "
        
    grid[row][col + 1] = " "

    grid[row + 1][col] = " "



        


def showGameOver(root):
    global gameScreen

    # Clear existing widgets from gameScreen
    for widget in gameScreen.winfo_children():
        widget.destroy()

    # Add "Game Over" widgets to gameScreen
    tk.Label(gameScreen, text="Game Over", font=("Helvetica", 24, "bold"), bg="#f4f4f4", fg="#f44336").pack(pady=10)
    tk.Label(gameScreen, text="You Hit a Mine", font=("Helvetica", 24, "bold"), bg="#f4f4f4", fg="#f44336").pack(pady=10)
    
    tk.Button(gameScreen, text="Main Menu", font=("Helvetica", 14), bg="#4CAF50", fg="white", height=2, width=20,
              command=lambda: showMenu(root)).pack(pady=10)
    
    tk.Button(gameScreen, text="Exit", font=("Helvetica", 14), bg="#f44336", fg="white", height=2, width=20,
              command= lambda: [endGame(root)]).pack(pady=10)







#---------------If player won functions-----------------------------------------------------
def showWinner(root):
    global gameScreen

    # Clear existing widgets from gameScreen
    for widget in gameScreen.winfo_children():
        widget.destroy()

    # Add "Game Over" widgets to gameScreen
    tk.Label(gameScreen, text="You Win", font=("Helvetica", 24, "bold"), bg="#f4f4f4", fg="green").pack(pady=10)
    
    tk.Button(gameScreen, text="Main Menu", font=("Helvetica", 14), bg="#4CAF50", fg="white", height=2, width=20,
              command=lambda: showMenu(root)).pack(pady=10)
    
    tk.Button(gameScreen, text="Exit", font=("Helvetica", 14), bg="#f44336", fg="white", height=2, width=20,
              command= lambda: [endGame(root), gameScreen.destroy()]).pack(pady=10)
    

def checkWinner():
    global grid, buttons, rows, columns
    for row in range(rows):
        for col in range(columns):
            if grid[row + 1][col + 1] != "X" and buttons[row][col]["text"] == " ":
                return False
            
    print("You won")
    return True
#---------------------------------------------------------------------------------------------

#--------------------Grid functions-----------------------------------------------------------
def generateMines():
    global grid, buttons, rows, columns

    for row in range(rows):
        for col in range(columns):
            if random.random() < 0.2:
                grid[row + 1][col + 1] = "X"



def changeGrid(newRows, newColumns):
    global rows, columns, grid, buttons

    rows = newRows
    columns = newColumns

    grid.clear()
    buttons.clear()

    grid = [[" " for _ in range(columns + 2)] for _ in range(rows + 2)]
    buttons = [[" " for _ in range(columns)] for _ in range(rows)]

    menuLabel.config(text=f"Grid size: {rows} x {columns}")
#-----------------------------------------------------------------------------------------------------

#---------------------Starting and ending game functions----------------------------------------------
def displayGame(root):
    menuFrame.pack_forget()
    gameStart(root)

def gameStart(root):
    global rows, columns, buttons, firstClick, gameScreen
    firstClick = True
    gameScreen = tk.Frame(root, padx=20, pady=20, bg="#f4f4f4")
    gameScreen.pack()

    generateMines()

    for row in grid:
        print(" | ".join(map(str, row)))
        print("-" * (len(row) * 4 - 1))

    for row in range(rows):
        for col in range(columns):
            button = tk.Button(gameScreen, text=buttons[row][col], font='Helvetica 12 bold', height=1, width=3,
                               command=lambda row=row, col=col: buttonClick(row, col, gameScreen))
            button.grid(row=row, column=col)
            buttons[row][col] = button



def endGame(root):
    if messagebox.askokcancel("Exit", "Are you sure you want to quit?"):
        if gameScreen != None:
            gameScreen.destroy()
        if menuFrame != None:    
            menuFrame.destroy()
        root.destroy()

#------------------------------------------------------------------------------------------

#---------Main Screen and Loop--------------------------------------------------------------
def showMenu(root):
    global menuFrame, menuLabel, rows, columns, gameScreen

    if gameScreen != None:
        for widget in gameScreen.winfo_children():
            widget.destroy()
        gameScreen = None


    menuFrame = tk.Frame(root, bg="#f4f4f4", padx=20, pady=20)
    menuFrame.pack(fill='both', expand=True)

    header = tk.Label(menuFrame, text="Mine Sweeper", font=("Helvetica", 24, "bold"), bg="#f4f4f4", fg="#333")
    header.pack(pady=10)

    menuLabel = tk.Label(menuFrame, text=f"Grid size: {rows} x {columns}", font=("Helvetica", 16), bg="#f4f4f4", fg="#555")
    menuLabel.pack(pady=10)

    start_button = tk.Button(menuFrame, text="Start Game", font=("Helvetica", 14), bg="#4CAF50", fg="white", height=2, width=20,
                             command=lambda: [changeGrid(rows, columns), displayGame(root)])
    start_button.pack(pady=10)

    settings_frame = tk.Frame(menuFrame, bg="#f4f4f4")
    settings_frame.pack(pady=10)

    grid_label = tk.Label(settings_frame, text="Grid Size:", font=("Helvetica", 16), bg="#f4f4f4", fg="#555")
    grid_label.grid(row=0, column=0, padx=10, pady=5)

    grid_64 = tk.Button(settings_frame, text="64", font=("Helvetica", 14), bg="#2196F3", fg="white", width=5,
                        command=lambda: changeGrid(8, 8))
    grid_64.grid(row=1, column=0, padx=10, pady=5)

    grid_100 = tk.Button(settings_frame, text="100", font=("Helvetica", 14), bg="#2196F3", fg="white", width=5,
                         command=lambda: changeGrid(10, 10))
    grid_100.grid(row=1, column=1, padx=10, pady=5)

    grid_144 = tk.Button(settings_frame, text="144", font=("Helvetica", 14), bg="#2196F3", fg="white", width=5,
                         command=lambda: changeGrid(12, 12))
    grid_144.grid(row=1, column=2, padx=10, pady=5)

    exit_button = tk.Button(menuFrame, text="Exit", font=("Helvetica", 14), bg="#f44336", fg="white", height=2, width=20,
                            command=lambda: endGame(root))
    exit_button.pack(pady=20)

def main():
    root = tk.Tk()
    root.title("Mine Sweeper")
    root.geometry("400x500")
    root.configure(bg="#f4f4f4")
    showMenu(root)
    root.mainloop()


#------------------------------------------------------------------------


if __name__ == "__main__":
    main()
