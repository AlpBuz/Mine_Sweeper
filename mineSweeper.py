import tkinter as tk
from tkinter import messagebox


#-----Global Variables-------------
rows = 4
columns = 4
grid = []
buttons = []
#---------------------------------








def buttonClick():
    None

def gameStart():
    None

def checkSurrondings(row, column):
    None

def gameOver():
    None

def generateMines():
    global grid, buttons
    





#---------------Grid/Setting functions-----------------------------------------------------------
def changeGrid(newRows, newColumns):
    global rows, columns, grid, buttons

    rows = newRows
    columns = newColumns

    grid.clear()
    buttons.clear()

    createGrid(rows, columns)
    menuLabel.config(text=f"Grid size is {rows} x {columns}")

    print(f"new Grid size is {rows} x {columns}")

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

    sixtyFourGrid = tk.Button(setting_frame, text="64 Size Grid", command=lambda: changeGrid(8, 8))
    sixtyFourGrid.pack(pady=10)

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


def displayGrid(rows, column):
    None
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
    start_button = tk.Button(menuFrame, text="Start Game", command=gameStart)
    start_button.pack(pady=10)

    settings_button = tk.Button(menuFrame, text="Settings", command=lambda: show_settings(root))
    settings_button.pack(pady=10)

    exit_button = tk.Button(menuFrame, text="Exit", command=lambda: endGame(root))
    exit_button.pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()