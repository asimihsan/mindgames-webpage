### Introduction

Masyu is played on a rectangular grid of squares, some of which contain circles;
each circle is either white or black. The goal is to draw a single continuous
non-intersecting loop that properly passes through all circled cells. Rules of
the puzzle are:

-   Make a single loop. Lines must pass through the centers of cells
    horizontally or vertically and never cross, branch off, or go through the
    same cells twice.
-   Lines must pass through all cells containing black and white circles.
-   Lines passing through a white circle cell must go straight through the cell,
    then make a right-angled turn in the very next cell (on at least one side of
    the white circle cell).
-   Lines passing through a black circle cell must make a right angled turn
    immediately, in the black circle cell, then go straight for the next two
    cells.

Like many other combinatory and logic puzzles, Masyu can be very difficult to
solve.

### Main features of this program

This program helps you solve existing Masyu puzzles as well as create new ones.
Main features of this program are:

-   Create new puzzles manually or automatically; automatic creation offers
    puzzles with different grid sizes from 7x7 to 20x20, with maximum Rows x
    Columns limit of 225.
-   Solve existing puzzles manually or let program solve it
-   Create new puzzles interactively or in bulk
-   Save puzzles as Ascii or bitmap files
-   Print puzzles and solutions
-   20,000 puzzles with solutions are provided

### Sample Layout

A sample screenshot is shown below:

![](../img/masyu_help1.gif)

### Setting up a Puzzle

There are two ways for defining a new puzzle.

**1. Enter the puzzle details in a text file using a text editor:**

The puzzle definition format is as below:

    #1
    Easy : 05-01-2007 18:09:45
    7, 7, 21
    BWWB...
    W..W...
    ...BW..
    .WBWB..
    ..W.W.W
    W.W....
    BWB.W..

-   First line indicates the puzzle number. This line must have # as first
    letter.
-   The second line is the puzzle header. The third line indicates the number of
    rows, the number of columns and the number of circles.
-   Third parameter is saved by the program for reference only.
-   Puzzle definition then follows. Letter W indicates a white circle and B
    indicates a black circle.

**2. A puzzle can also be defined interactively using the following steps:**

-   Click Create/Grid
-   Place mouse over a position and click W, B or X
-   W will place a white circle, B a black circle and X will clear a circle
-   Click Save/Masyu file to save puzzle
-   Click AutoSolve first if you wish to save solution with the puzzle as well
-   You can edit an existing puzzle by the same procedure above; click
    Edit/SetEditMode for this purpose.

**Note that this program can automatically create new puzzles for you. No two
puzzles will be alike.**

### Editing a Puzzle

An existing puzzle can be edited, solved manually or by computer and saved.

-   Load an existing puzzle
-   Click Edit/SetEditMode
-   Place mouse over a position and click W, B or X
-   W will place a white circle, B a black circle and X will clear a circle
-   Click AutoSolve to solve
-   Solve manually by drawing lines
-   Click Save/Masyu file to save puzzle

### Solving a Puzzle - Manually

-   Click Solve/SetEditMode
-   Left click on a cell, drag mouse over to the cell to connect to, and release
    left click. If this is a valid connection bridge, a red line will be drawn
-   Use right click if you wish to clear a bridge
-   Click Edit/CheckSolution to verify whether the puzzle has been solved or
    not.

### How to Solve a Puzzle

Understanding the placement of the circles and how they interact with each other
is the key to solving a Masyu puzzle. Generally speaking, it is easiest to start
along the outside border of the grid and work inwards. Here are some basic
scenarios where portions of the loop can be determined:

-   Any segment travelling from a black circle must travel two cells in that
    direction without intersecting another part of the loop or the outer border;
    each black cell must have two such segments at a right angle. The logical
    combination of those two statements is that if a segment from a black cell
    cannot be drawn in some orthogonal direction, a segment in the opposite
    direction must be drawn. For example, if one cannot legally travel up two
    cells from a black circle, then the loop must travel down from that black
    circle for two cells. This has two common results:
    -   Any black circle along the outer border or one cell from the outer
        border must have a segment leading away from the border (and those
        sufficiently near a corner must lead from both walls, defining the
        loop's path through the circle);
    -   Orthogonally adjacent black circles must have segments travelling away
        from each other.
-   White circles along the outer border obviously need the loop to travel
    through them parallel to the border; if two white circles along a border are
    adjacent or are one cell apart, then the loop will need to turn away from
    the border just beyond the circles.
-   If three or more white circles are orthogonally contiguous and collinear,
    then the loop will need to pass through each of those circles perpendicular
    to the line of circles. As in other loop-construction puzzles, "short
    circuits" also need to be avoided: as the solution must consist of a single
    loop, any segment that would close a loop is forbidden unless it immediately
    yields the solution to the entire puzzle. TOP

### Solving a Puzzle - by Computer

Click Solve/AutoSolve button to let computer solve a puzzle. Click Cancel at the
top right of the display to stop this function.

Note that this program employs a set of rules to successively reduce the number
of valid choices. If reduction does not result in a solution, a trial and error
approach is used. Computer will eventually find a solution to any valid puzzle.

### View Solution

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
-   New puzzle will also be saved in a temporary file: TemporaryPuzzleFile.syu
-   A solution is also created as part of the newpuzzle

**Multiple Puzzle Create:**

-   Click Create/Multi
-   Define the grid size and whether fixed or random; random size will be chosen
    from 7x7 to the size specified
-   Set how many puzzles you want to create
-   Select the file where new puzzles will be saved
-   Click Create, new puzzles will be stored in the file specified

### Saving Puzzles

A puzzle and its solution can be saved into a file or appended to the currently
loaded file. Solutions are saved with the puzzle. A solution saved along with
the puzzle can be viewed without obtaining a solution; use Solve/ViewSolution
menu command for this purpose.

### Loading Saved Puzzles

Use Masyu/PuzzleFile/Load menu to load puzzles saved in a file.

### Sorting a Puzzle file

You can sort any puzzle file by the number of rows or by the puzzle title. This
option can also resequence puzzle numbers. Use Masyu/PuzzleFile/Sort for this
purpose.

### Printing

The current puzzle and its solution will be printed on an A4 sheet that can be
folded in two halves to separate puzzle from its solution. Note that the puzzle
solution must be in view (use AutoSolve or ViewSolution) else a blank solution
will be printed.

You can also print multiple puzzles from an existing puzzle file in 1 or 2
puzzles per page. Puzzle solutions will be taken from the file.

### About Masyu Program

This program was written in VB6, based on information available on web sites,
too numerous to acknowledge. This program is free to use and distribute but
cannot be used for commercial purposes.