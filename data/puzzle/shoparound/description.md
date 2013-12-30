### Introduction

ShopAround, a variant of Nicoli's Masyu game is played on a rectangular grid of
cells. One cell is designated as Home. The remaining grid has a set of Shops
(marked as S) and Gas Stations (marked as G). The purpose of this game is to
start from your home and return home after visiting all the shops and gas
stations in the grid. Following rules apply:

-   The trip must be in a single loop, starting and ending at home
-   Lines must pass through all cells containing shops and gas stations
-   A cell cannot be visited twice
-   Lines passing through a shop must go straight through the cell
-   A line reaching a gas station must make a right angle turn (left or right)
    at the station
-   Must go to a gas station at the start and at the end of the trip
-   Cannot go to two shops or two gas stations consecutively

Like Masyu, this puzzle can be rather difficult to solve.

### Main features of this program

This program helps you solve existing ShopAround puzzles as well as create new
ones. Main features of this program are:

-   Create new puzzles manually or automatically; automatic creation offers
    puzzles with different grid sizes from 5x5 to 10x10
-   Solve existing puzzles manually or let program solve it
-   Create new puzzles interactively or in bulk
-   Save puzzles as ascii or bitmap files
-   Print puzzles and solutions
-   20,000 puzzles with solutions are provided

Sample Layout

A sample screenshot is shown below:

![](../img/shoparound_help1.gif)

### Setting up a Puzzle

There are two ways for defining a new puzzle.

**1. Enter the puzzle details in a text file using a text editor:**

The puzzle definition format is as below:

    #1
    Auto 05-18-2007 06:29:38
    7, 7, 12
    .S....G
    GSG...S
    G.S.GSG
    .S.GS..
    ...HGSG
    SGSG..S
    GS....G

-   First line indicates the puzzle number. This line must have # as first
    letter.
-   The second line is the puzzle header.
-   The third line indicates the number of rows, the number of columns and the
    number stops (shops and gas stations). Third parameter is saved by the
    program for reference only.
-   Puzzle definition then follows.
    -   Letter G indicates a gas station,
    -   S a shop and
    -   H (only one cell) the home.

**2. A puzzle can also be defined interactively using the following steps:**

-   Click Create/Grid
-   Place mouse over a position and click H, G or S or X
-   H will place home, G as gas station, S a shop and X will clear a cell
-   Click Save/ShopAround file to save puzzle
-   Click AutoSolve first if you wish to save solution with the puzzle as well
-   You can edit an existing puzzle by the same procedure above; click
    Edit/SetEditMode for this purpose.

**Note that this program can automatically create new puzzles for you. No two
puzzles will be alike.**

### Editing a Puzzle

An existing puzzle can be edited, solved manually or by computer and saved.

-   Load an existing puzzle
-   Click Edit/SetEditMode
-   Place mouse over a position and click H, G, S or X
-   H will place home, G as gas station, S a shop and X will clear a cell
-   C will clear any lines in cell
-   One a grid puzzle is set, click AutoSolve to solve
-   You can also solve manually by drawing lines
-   Click Save/ShopAround file to save puzzle

### Solving a Puzzle - Manually

-   Click Solve/SetEditMode
-   Left click on a cell, drag mouse over to the cell to connect to, and release
    left click. If this is a valid connection, a red line will be drawn
-   Use right click if you wish to clear a line
-   Click Edit/CheckSolution to verify whether the puzzle has been solved or
    not.

### Solving a Puzzle - by Computer

Click Solve/AutoSolve button to let computer solve a puzzle. Click Cancel at the
top right of the display to stop this function.

Note that this program employs a set of rules to successively reduce the number
of valid choices. If reduction does not result in a solution, a trial and error
approach is used. Computer will eventually find a solution to any valid puzzle.
TOP

### View Solution

Puzzle solutions, by computer or manual, can be stored in the puzzle file along
with the puzzle. Click Solve/Viewsolution menu in order to view a stored
solution.

### Compiling New Puzzles

Puzzles can be compiled one at a time or in bulk.

**Single Puzzle Create:**

-   Click Create/Grid to set the grid size
-   Click Create/GridSizePuzzle to create a new puzzle of the displayed grid
    size
-   Click Create/RandomSizePuzzle to create a random size new puzzle
-   New puzzle will also be saved in a temporary file: TemporaryPuzzleFile.sar
-   A solution is also created as part of the new puzzle

**Multiple Puzzle Create:**

-   Click Create/Multi
-   Define the grid size and whether fixed or random; random size will be chosen
    from 6x6 to the size specified
-   Set how many puzzles you want to create
-   Select the file where new puzzles will be saved
-   Click Create, new puzzles will be stored in the file specified

### Saving Puzzles

A puzzle and its solution can be saved into a file or appended to the currently
loaded file. Solutions are saved with the puzzle. A solution saved along with
the puzzle can be viewed without obtaining a solution; use Solve/ViewSolution
menu command for this purpose.

### Loading Saved Puzzles

Use ShopAround/PuzzleFile/Load menu to load puzzles saved in a file.

### Sorting a Puzzle file

You can sort any puzzle file by the number of rows or by the puzzle title. This
option can also resequence puzzle numbers. Use ShopAround/PuzzleFile/Sort for
this purpose.

### Printing

The current puzzle and its solution will be printed on an A4 sheet that can be
folded in two halves to separate puzzle from its solution. Note that the puzzle
solution must be in view (use AutoSolve or ViewSolution) else a blank solution
will be printed.

You can also print multiple puzzles from an existing puzzle file in 1 or 2
puzzles per page. Puzzle solutions will be taken from the file.

### About ShopAround Program

This program was written in VB6, based on information available on web sites,
too numerous to acknowledge. This program is free to use and distribute but
cannot be used for commercial purposes.