**Developed by:**
*2nd year students, IM-21 group:*

<span padding-right:5em></span> **Rudyi Nazarii** [Email: rudiy.nazaryi@lll.kpi.ua,  [Telegram](https://t.me/iNazqq)]

<span padding-right:5em></span> **Fesun Anna** [Email: fesun.anna@lll.kpi.ua,  [Telegram](https://t.me/anyafesun)]


# 15 Puzzle Game

## Project Description
Software has been developed that allows playing the 15 puzzle game and solving it using search algorithms. The program has the following functional requirements:

- Ability to set initial conditions for the 15 puzzle game, including the ability to set an empty field
- Ability to generate a correctly solved 15 puzzle game
- Ability to manually solve the 15 puzzle game
- Ability to automatically solve the 15 puzzle game with solution steps displayed
- Ensuring acceptable time characteristics for automatic solving of the 15 puzzle (no more than 2 minutes). Before developing the program, a <a name="jdk" href="https://docs.google.com/document/d/1rVkbBMYSszTD1hn5XBeSRE2qt0xa3ZuiKDP1cdVK4bU/edit?usp=sharing">Design Document</a> was created.

## Instructions on How to Build and Run the Project

1. If Python is not yet installed on your computer, download and install it from the official website <a name="jdk" href="https://www.python.org/downloads">python</a>

2. Download the repository to your local computer
   
3. Launch terminal in the root folder of the repository
   
4. Enter the command "python main.py" in the terminal to run the application
You can also download the .exe file located in the program folder and simply run the program.

## Project Solution Justification
The project solution for creating the "15 Puzzle" game was made based on several key aspects that consider convenience, functionality, and game efficiency.

1. Simplicity and Logic
The implementation of the "15 Puzzle" game is designed to be simple and easily understandable for players. Logical placement of interface elements, as well as simple and clear game rules allow users to quickly master the game. The main goal is to provide an enjoyable gaming process without unnecessary complications.
2. Functionality
The game has a complete set of functions necessary for comfortable gameplay. The tile movement system, ability to shuffle numbers on the field to start a new game, and display of the current game state make the game interesting and challenging.

## Illustrations

<div align="center">
  <img src="https://github.com/Ancellie/15-puzlle/blob/main/images/picture1.png" alt="Початкове вікно програми">
  <p>Figure 1.1 — Initial program window</p>
</div>

By clicking the "New Game" button, the tile board will be moved 1000 times in random directions (Figure 1.2)
 
<div align="center">
  <img src="https://github.com/Ancellie/15-puzlle/blob/main/images/picture2.png" alt="Вікно програми після натискання кнопки “New Game”">
  <p>Figure 1.2 — Program window after clicking "New Game" button</p>
</div>

If you press the "Solve" button, the path-finding algorithm will start to solve the game (Figure 1.3)

<div align="center">
  <img src="https://github.com/Ancellie/15-puzlle/blob/main/images/picture3.png" alt="Алгоритм запущений">
  <p>Figure 1.3 — Algorithm running</p>
</div>

After the algorithm finds the path, the game begins to automatically solve itself, with tile movement animation, until it completes all necessary moves and the game is in a solved configuration (Figure 1.4)

<div align="center">
  <img src="https://github.com/Ancellie/15-puzlle/blob/main/images/picture4.png" alt="Гра була розв'язана">
  <p>Figure 1.4 — Game was solved</p>
</div>

If you press the up arrow, the empty tile will move up, same with other arrows: if you press down, it will move down, if left, then left. If you press the "Quit" button, the game will close.
