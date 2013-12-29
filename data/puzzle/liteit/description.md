### Introduction

This programs helps you solve existing LiteIt puzzles as well as create new
ones. LiteIt is another Japanese number puzzle (yes another one) consisting of a
grid comprising empty cells, black cells, and cells with numbers 0 to 4.
Challenge is to:

-   Illuminate all the empty cells by placing -light bulbs- at empty locations.
-   A bulb placed at a cell will light up all the cells in its row and column.
-   However, no two bulbs must face each other.
-   Also, a numbered cell must have exact number of bulbs around the cell, eg a
    cell with number 1 must have one and only bulb around it etc. Cell with
    number 0 cannot have any bulb around it.

Sounds simple but hard to figure out.

This program has a puzzle size limitation of maximum 20 rows and 24 columns.

### Sample Layout

A grid layout for a typical puzzle is given below:

![](../img/liteit_help1.gif)

### Setting up a Puzzle

There are two ways for defining a new puzzle.

**Enter the puzzle details in a text file using a text editor**:

The puzzle definition format for the puzzle shown above is as follows: (`--` is
a comment, not part of the definition):

    #1:-- Puzzle Number
    Easy :-- Puzzle Title
    10, 10 :-- Number of rows, Number of columns in the Puzzle
    1--------1
    ---B------
    -B---2--B-
    -------1--
    ---4------
    ------2---
    --2-------
    -B--2---B-
    ------0---
    1--------1

In the definition above in a row: B indicates a black cell; a single number
indicates a black cell with a number (bulbs required) and - is a blank cell. A
puzzle can also be defined interactively with keyboard or mouse clicks using the
following steps:

-   Create a new grid of the required size by using the Create Menu
-   Right click on cell to enter cell definition through a dropdown number pad.
-   Alternatively use arrow keys to navigate through the cells. Enter X to make
    a black cell, C to clear a cell, or, enter two numbers 0 to 4.

Solution for this puzzle is given below:

![](../img/liteit_help2.gif)

### Solving a Puzzle - Manually

-   Click on Manual Solve button to commence a manual solution
-   Right click on a cell to place or clear a bulb placement
-   You can also use arrow keys to navigate through the cells and set/clear a
    bulb placement by pressing B.

### Solving a Puzzle - by Computer

Click AutoSolve button to let computer solve a puzzle. Click cancel to stop this
function. The computer solution is basically a trial and error approach and is
not driven by any precise mathematical algorithm. Although brute-force guessing
is of course employable but will take a long time to exhaust all non-legal
combinations and end up with a solution. This program does employ a set of rules
to successively reduce the number of valid choices for placing a bulb.

**Caution: Some of the puzzles provided with this program may have multiple
solutions.**

### Compiling New Puzzles

A new puzzle can be compiled by using an existing grid and creating another
puzzle. For this purpose click Create/Compile menu option. Alternatively you can
create a new layout by using the Create/Edit menu. While in Edit mode you can
change the characteristics of any cell. In order to start with a clean grid use
Create/Grid option menu option. Once a new grid has been created, click
Create/Compile to test whether the grid is valid or not.

### Auto Generating Puzzles

Multiple puzzles can be generated and saved to a file automatically. Use
Create/Auto menu for this purpose. Grid size can be fixed or have a random size
between 8x8 and 16x16 cells; this option is useful in creating puzzles in bulk
with various sizes.

### Saving Puzzles

A puzzle and its solution can be saved into a file or appended to the currently
loaded file. Use File/Save or File/SaveAs menus for this purpose. Solutions are
saved with the puzzle, each row followed by | and solution. A solution saved
along with the puzzle can be viewed without obtaining a solution; use View
Solution command for this purpose.

### Loading Saved Puzzles

Use File/Load menu to load puzzles saved in a file.

### Sorting a Puzzle file

You can sort the currently loaded puzzle file by the number of rows or by the
puzzle title. This option can also resequence puzzle numbers.

### Printing

The current puzzle and its solution will be printed on an A4 sheet that can be
folded in two halves to separate puzzle from its solution. Note that the puzzle
solution must be obtained first else a blank solution will be printed. You can
also print multiple puzzles from an existing puzzle file.

### About LiteIt Program

This program was written in VB6, based on information available on web sites,
too numerous to acknowledge. This program is free to use and distribute but
cannot be used for commercial purposes.