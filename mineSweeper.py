import tkinter as tk
from tkinter import messagebox
import random

#-----Global Variables-------------
rows = 4
columns = 4
grid = [[" " for _ in range(6)] for _ in range(6)]
buttons = [[" " for _ in range(4)] for _ in range(4)]
#---------------------------------


def buttonClick(row, col):
    global grid, buttons

    if grid[row+1][col+1] == " ":
        bombs = checkSurrondingsBomb(row+1,col+1)
        buttons[row][col].config(text=str(bombs))
        #checkSurroundings(row, col)
    else:
        buttons[row][col].config(text="X")
        #gameOver()



def displayGame(root):
    menuFrame.pack_forget()  # Hide the main menu frame
    gameStart(root)  # Create and show the settings frame



def gameStart(root):
    global rows, columns, buttons
    gameScreen = tk.Frame(root, padx=100, pady=100)
    gameScreen.pack()

    generateMines()

    for row in grid:
        # Join elements of the row with a space and add dividers between them
        print(" | ".join(map(str, row)))
        # Print a horizontal line as a divider between rows
        print("-" * (len(row) * 4 - 1))  # Adjust the multiplier for longer numbers
    

    for row in range(rows):
        for col in range(columns):
            button = tk.Button(gameScreen, text= buttons[row][col], font='Helvetica 20 bold', height=1, width=3,
                           command=lambda row=row, col=col: buttonClick(row, col))
            button.grid(row=row, column=col)
            buttons[row][col] = button



#--------------Functions to check the surrondings---------------------------------
def checkSurrondingsBomb(row, column): #function checks the surronding for any bombs, returns the number of bombs found
    reVal = 0
    if grid[row-1][column-1] == "X":
        reVal += 1

    if grid[row-1][column] == "X":
        reVal += 1

    if grid[row-1][column+1] == "X":
        reVal += 1

    if grid[row][column-1] == "X":
        reVal += 1

    if grid[row][column+1] == "X":
        reVal += 1

    if grid[row+1][column-1] == "X":
        reVal += 1

    if grid[row+1][column] == "X":
        reVal += 1

    if grid[row+1][column+1] == "X":
        reVal += 1
    return reVal

#This function will be used to help create that chain reaction of when a user selects a section on the map, it also opens any other sections next
#to it when their is no bombs
def checkSurroundings(row, col): 
    global grid, buttons, columns, rows

    if (row < 0 or row >= rows) or (col < 0 or col >= columns):
        return
    

    if grid[row][col] == "X":
        return
    
    if grid[row][col] != " ":
        return

    # Count the number of bombs surrounding the cell
    bombs = checkSurrondingsBomb(row, col)
    buttons[row][col].config(text=str(bombs))

    
    # Check all eight possible surrounding cells
    checkSurroundings(row, col - 1)  # left
    checkSurroundings(row, col + 1)  # right
    checkSurroundings(row - 1, col)  # up
    checkSurroundings(row + 1, col)  # down
    checkSurroundings(row - 1, col - 1)  # top-left
    checkSurroundings(row - 1, col + 1)  # top-right
    checkSurroundings(row + 1, col - 1)  # bottom-left
    checkSurroundings(row + 1, col + 1)  # bottom-right

    

#------------------------------------------------------------




def gameOver():
    None


def checkWinner():
    global buttons
    for row in buttons:
        for col in buttons:
            if col == " ":
                return False
    
    return True

def generateMines():
    global grid, buttons, rows, columns

    for row in range(rows):
        for col in range(columns):
            if random.random() < .50:
                grid[row+1][col+1] = "X"
    





#---------------Grid/Setting functions-----------------------------------------------------------
def changeGrid(newRows, newColumns):
    global rows, columns, grid, buttons

    rows = newRows
    columns = newColumns

    grid.clear()
    buttons.clear()

    createGrid(rows, columns)
    menuLabel.config(text=f"Grid size is {rows} x {columns}")

def show_settings(root):
    menuFrame.pack_forget()  # Hide the main menu frame
    gameSettings(root)  # Create and show the settings frame


def gameSettings(root):
    setting_frame = tk.Frame(root, padx=100, pady=100)
    setting_frame.pack()

    sixteenGrid = tk.Button(setting_frame, text="16 Size Grid", command=lambda: changeGrid(4, 4))
    sixteenGrid.pack(pady=10)

    thirtySixGrid = tk.Button(setting_frame, text="36 Size Grid", command=lambda: changeGrid(6, 6))
    thirtySixGrid.pack(pady=10)

    hundredFortyFourGrid = tk.Button(setting_frame, text="144 Size Grid", command=lambda: changeGrid(12, 12))
    hundredFortyFourGrid.pack(pady=10)

    back_button = tk.Button(setting_frame, text="Back", command=lambda: show_menu(setting_frame, root))
    back_button.pack(pady=10)

    return setting_frame


def createGrid(rows, columns):
    global grid, buttons
    
    #create the grid for the grid variable matrix
    for i in range(rows+2):
        row = []
        for j in range(columns+2):
            row.append(" ")
        grid.append(row)
    
    #creates the grid for the buttons variable matrix
    for i in range(rows):
        row = []
        for j in range(columns):
            row.append(" ")
        buttons.append(row)


#------------------------------------------------------------------------------------------------- 


def endGame(root):
    if messagebox.askokcancel("Exit", "Are you sure you want to quit?"):
        root.destroy()


def show_menu(current_frame, root):
    current_frame.pack_forget()  # Hide the current frame
    menuFrame.pack()


def main():
    global menuFrame, menuLabel
    global rows, columns, grid, buttons

    root = tk.Tk()
    root.title("Mine Sweeper")

    # Create a frame for the menu buttons
    menuFrame = tk.Frame(root, padx=100, pady=100)
    menuFrame.pack()

    menuLabel = tk.Label(menuFrame, text=f"Grid size is {rows} x {columns}", font=("Helvetica", 16), fg="blue")
    menuLabel.pack(pady=20)


    # Create buttons for different options
    start_button = tk.Button(menuFrame, text="Start Game", command=lambda: displayGame(root))
    start_button.pack(pady=10)

    settings_button = tk.Button(menuFrame, text="Settings", command=lambda: show_settings(root))
    settings_button.pack(pady=10)

    exit_button = tk.Button(menuFrame, text="Exit", command=lambda: endGame(root))
    exit_button.pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()