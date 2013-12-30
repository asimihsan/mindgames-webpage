### Introduction

MirrorMaze, derived from Japanese puzzle Masyu, is played on a grid of squares,
some of which contain 'mirrors'. The goal is to draw a single continuous non-
intersecting line from one circle to the other. Rules of the puzzle are:

-   Grid is a rectangular grid with two circles located at the boundaries of the
    grid
-   Grid size is minimum 6 rows or columns to maximum 20 rows or columns;
    product of number of rows and number of columns is less than 256
-   Some cells in the grid contain 'mirrors' of the following type:
    -   Blocked - a line cannot pass through such a cell
    -   Tunnel - a lines must pass in the direction of the tunnel, vertical or
        horizontal
    -   Reflection - a line must reflect at right angle
-   In an open cell without any mirror, line can go vertical, horizontal or at
    right angles
-   Only one line can go through a cell
-   A single line must join the two circles
-   Line must pass through all open cells

Like many other combinatory and logic puzzles, MirrorMaze can be very difficult
to solve.

### Main features

This program helps you solve existing MirrorMaze puzzles as well as create new
ones. Main features of this program are:

-   Create new puzzles manually or automatically; automatic creation offers
    puzzles with different grid sizes
-   Grid size limitations are:
    -   Minimum 6 rows or columns
    -   Maximum 20 rows or columns
    -   Product of number of rows and number of columns must be less than 256
    -   For example smallest grid will be 6x6, and largest 20x12 or 12x20 or
        16x16
-   Solve existing puzzles manually or let program solve it
-   Create new puzzles interactively or in bulk
-   Print puzzles and solutions
-   20,000 puzzles with solutions are provided

### Sample Layout

A sample screenshot is shown below:

![](../img/mirrormaze_help1.gif)

### Setting up a Puzzle

A puzzle can also be defined interactively using the following steps:

-   Click Create/NewGrid and set a grid of desired size
-   Double click on a cell, a dropdown menu will appear
-   Select the desired mirror to place in the cell
-   You can also specify locations of the two circles:
    -   Double click on a cell at the boundary to clear or set a circle
    -   Must clear a circle first before adding one at another location
    -   Must have two circles for a valid puzzle
-   Once a puzzle has been setup, click Solve/Autosolve to verify if the puzzle
    is logical and can be solved
-   Click Puzzle/Save; solution will be saved also
-   You can edit an existing puzzle by the same procedure above

**Note that this program can automatically create new puzzles for you. No two
puzzles will be alike.**

### Solving a Puzzle - Manually

-   Left click on a cell. With left button down, drag mouse over to the
    destination cell. - Release left click. If this is a valid connection a line
    will be drawn
-   Continue mouse move, with out left click to continue drawing the line to
    other cells
-   Use right click instead of left click if you wish to clear a line
-   Understanding the placement of the mirrors and how they interact with each
    other is the key to solving a MirrorMaze puzzle. Generally speaking, it is
    easiest to start along the outside border of the grid and work inwards.
-   Line directions at reflective and tunnel mirrors are fixed. You can use
    Solve/SolveMirrorMaze option to draw these lines automatically before you
    start solving a puzzle.
-   As in other loop-construction puzzles, "short circuits" also need to be
    avoided: as the solution must consist of a single line. Any segment that
    would close a loop is not allowed.

### Solving a Puzzle - by Computer

Click Solve/AutoSolve button to let computer solve a puzzle. Click Cancel at the
top right of the display to stop this function.

Note that this program employs a set of rules to successively reduce the number
of valid choices. If reduction does not result in a solution, a trial and error
approach is used. Computer will eventually find a solution to any valid puzzle.
TOP

### View Solution

Puzzle solutions, by computer or manual, can be stored in the puzzle file along
with the puzzle. Click Solve/ShowSolution menu in order to view a stored
solution.

### Compiling New Puzzles

Puzzles can be compiled one at a time or in bulk.

**Single Puzzle Create:**

-   Click Create/NewGrid to set the grid size
-   Specify locations of the two circles (optional):
    -   Double click on a cell at the boundary to clear or set a circle
    -   Must clear a circle first before adding one at another location
    -   Must have two circles for a valid puzzle
    -   Program will place circles randomly if none are specified
-   Click Create/OnePuzzle to create a new puzzle
-   New puzzle will also be saved in a temporary file: TemporaryPuzzleFile.mir
-   A solution is also created as part of the new puzzle

**Multiple Puzzle Create:**

-   Click Create/MultiplePuzzles
-   Define the grid size and whether fixed or random; random size will be chosen
    from 6 to 20
-   You can fix the placement of circles when creating multiple puzzles
-   Set how many puzzles you want to create
-   Select the file where new puzzles will be saved
-   Click Create, new puzzles will be stored in the file specified

### Saving Puzzles

A puzzle and its solution can be saved into a file or appended to the currently
loaded file. Solutions are saved with the puzzle. A solution saved along with
the puzzle can be viewed without obtaining a solution; use Solve/ShowSolution
menu command for this purpose.

### Loading Saved Puzzles

Use MirrorMaze/File/Load menu to load puzzles saved in a file.

### Sorting a Puzzle file

You can sort any puzzle file by the number of rows or by the puzzle title. This
option can also resequence puzzle numbers. Use MirrorMaze/File/Sort for this
purpose.

### Printing

The current puzzle or its solution will be printed on an A4 sheet. You can also
print multiple puzzles from an existing puzzle file. Puzzle solutions will be
taken from the file.

### About MirrorMaze Program

This program was written in VB6, based on information available on web sites,
too numerous to acknowledge. This program is free to use and distribute but
cannot be used for commercial purposes.