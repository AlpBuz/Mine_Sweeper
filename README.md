# Minesweeper Game

A simple Minesweeper game built with Python's Tkinter library.

## Overview
This is a basic implementation of the classic Minesweeper game using Python's Tkinter library. The game features a grid where players can click to reveal cells. If a player clicks on a mine, they lose the game. The goal is to reveal all non-mine cells.


## Features
- **Configurable grid size:** 64, 100, or 144 cells.
- **Random mine generation** with a 20% chance for each cell to contain a mine.
- **User-friendly interface** with a start screen and in-game UI.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/AlpBuz/Mine_Sweeper.git
   cd minesweeper

2. **Install dependencies:**
    Ensure you have Python installed. This game uses the built-in tkinter library, which comes with Python by default.

3. **Run the file**
    run the file using the command: python mineSweeper.py


## Game Instruction

1. **Start the Game:**

    Choose the desired grid size: 64, 100, or 144 cells.
    Click on the "Start Game" button from the main menu.

2. **Playing the Game:**

    Click on a cell to reveal it.
    If the cell contains a mine, the game is over.
    If the cell is empty, a number will appear indicating the number of surrounding mines.
    Reveal all non-mine cells to win the game.

3. **End of Game:**

    If you hit a mine, the game will show a "Game Over" message.
    If you successfully reveal all non-mine cells, you will see a "You Win" message.