Minesweeper Game

A simple Minesweeper game built with Python's Tkinter library.


Overview:

This is a basic implementation of the classic Minesweeper game using Python's Tkinter library. The game features a grid where players can click to reveal cells. If a player clicks on a mine, they lose the game. The goal is to reveal all non-mine cells.


Features:

    Configurable grid size (64, 100, 144 cells).
    Random mine generation with a 20% chance for each cell to contain a mine.
    User-friendly interface with a start screen and in-game UI.
    Game over and win conditions with appropriate messages.

Installation:



Install dependencies:
Ensure you have Python installed. This game uses the built-in tkinter library, which comes with Python by default.

If you need to install tkinter, you can do so using:



To start the game, simply run the following command:


python mineSweeper.py


Game Instructions:

    Start the Game:
        Choose the desired grid size: 64, 100, or 144 cells.
        Click on the "Start Game" button from the main menu.

    Playing the Game:
        Click on a cell to reveal it.
        If the cell contains a mine, the game is over.
        If the cell is empty, a number will appear indicating the number of surrounding mines.
        Reveal all non-mine cells to win the game.