### Introduction

GuessNum is a MastermindTM* like game where you are required to find a target
hidden number given a set of progressive clues. Target number varies from 3 to 9
digits long with each digit being 1 to 9. A digit can be repeated in target
numbers size of 6 or below. Maximum number of tries is 12. You must guess a
number with each digit in it correct and in correct position. Two clues are
given for each guess. A Black (B) clue indicates how many digits are correct and
in correct positions while a White (W) clue indicates how many digits are
correct but in wrong positions.

### Sample Layout

![](../img/guessnum_help1.gif)

### How clues are determined

Two clues are given for each guess. Black clue (B's) indicates how many digits
are correct and in correct position while White clue (W's) indicates how many
digits are correct but in wrong position. If there are duplicate digits in the
guess, they cannot all be awarded a B unless they correspond to the same
position in the target number. For example, if the target number is 1122 and the
player guesses 1112, program will give two Bs for the two correct 1s, nothing
for the third 1 as there is not a third 1 in the target number, and a B for the
last digit 2. No indication is given of the fact that the target number also
includes a second 2. Consider following clues:

    Target number: 7547
    Guess  B W
    4561   1 1
    3427   1 1
    2778   0 2
    6842   1 0

    Target number: 46515
    Guess  B W
    64277  0 2
    43177  1 1
    25454  0 3
    26725  2 0
    41626  1 2

### Program features

Main features of this program are:

-   Create new puzzles, number size 3 to 9 with numbers from 1 to 9 in each
    puzzle
-   Create puzzle with a given target answer
-   Disable duplicate digits in target numbers (except in target number size 7,
    8 or 9)
-   Import and solve existing puzzles
-   Solve a puzzle where you provide BW clues
-   Verify and check for unique solution of an imported puzzle
-   Create one or multiple puzzles
-   Create multiple puzzle with random target numbers or ones specified by you
-   Print one or multiple puzzles, 4 per page
-   Export puzzles in text format
-   Display pictures or letters instead of numbers
-   Help with guesses in a game
-   Copy a puzzle to Clipboard
-   Set display colour schemes
-   Use one of [60 GuessNum
    pictures](http://www.ihsan.biz/common/exe/guessnumpictures.zip) 398Kb
-   Use one of [20,000 ready made
    puzzles](http://www.ihsan.biz/common/exe/guessnum20k.zip) 241Kb

### Creating new puzzles

In order to create a single new puzzle:

-   Set target number size 3 to 9. Puzzles with 9 digits are not that
    challenging as the digits are already known, only positions need to be
    determined.
-   Set whether the target number can have repeated digits
-   Target numbers of size 7 to 9 will not have repeated digits irrespective of
    no-repeat-option set
-   Leftclick create command button; a new puzzle will be created
-   Rightclick create command button if you want to specify a target number
-   You can use pictures or letters instead of number. See 'using pictures and
    letters' option.
-   After you create or load a puzzle you can do the following with it:
    -   Export it to a text file if you are compiling a set of puzzles: use
        Puzzle/Export menu
    -   Save it as a puzzle file for reloading later by GuessNum: use
        Puzzle/Save menu
    -   Print the puzzle to solve on paper: use Print/CurrentPuzzle menu
    -   Solve on screen: use ManualSolve command button

In order to create multiple puzzles:

-   Click create multiple puzzle menu and set options. Computer will select
    target numbers.
-   You can also preset target numbers. For this purpose first create a text
    file containing a list of target numbers, one on each line. Then use create
    multiple file menu. If you set target numbers as letters like: ABLAZE or
    HAPPY, ILOVEU, WELL, BYE etc computer will generate appropriate guesses and
    BW values using letters only. Note that there should be no duplicate digits
    or letters in target numbers of size 7, 8 and 9.
-   Creating multiple puzzles may take some time; use a fast computer overnight.

### Solving a puzzle

When you create or load a saved puzzle its clues will be displayed. Normally one
would print these clues and solve on paper. However, you can also solve on
screen:

-   Create a new puzzle or load from a file
-   Click manual solve button (bottom right of the display); clues will be
    erased since the grid must be empty for you to try your guesses. This is
    same as if you were playing on a board game.
-   Enter your starting guess in row 1 in the grid. In order to enter a number:
    -   Left click on a position or position cursor using arrow keys
    -   Enter a number 1 to 9
    -   You can also drag-drop a number from the top row to a position. Drag-
        drop can also be used to set numbers within a row.
    -   After your guess is set, click OK - computer will calculate and display
        BW counts
    -   Examine the result of your guess and prepare your next move
    -   Continue your guesses until you get the answer using BW clues

### Computer solution

Computer can provide two types of solutions:

-   You provide a list of clues with numbers and corresponding BW values for
    each number and let computer find the solution. Computer will examine each
    BW clue and find the hidden target number. Clues can be entered via a text
    file that you can prepare using a text editor. The file format should be
    Number,B,W like below. This is generally how GuessNum type puzzles appear in
    media.

        4561,1,1
        3427,1,1
        2778,0,2
        6842,1,0

    Leftclick AutoSolve button and follow instructions.

    In some cases the puzzle you want computer to solve may have an upper limit
    on the digit value. It is common to see puzzles published on Internet with a
    limit of 6 colours, thus using digits 1 to 6 only, unlike default 1 to 9 in
    the GuessNum program. In such cases specify the uplift in the Digit Limit
    box.

-   You select a target number and let computer find it. For this purpose write
    down your number on a piece of paper and rightclick AutoSolve button.
    Computer will display its guesses and you provide the BW answers. Computer
    will generally find the answer in 6 or less tries.

### Getting help

Computer can provide help with your guesses. This will apply in two scenarios:

1.  When you are playing against an opponent, like on a board game:
    -   You will start with a guess and the opponent will give you the BW
        numbers
    -   In GuessNum create a grid of same size as the game on the board, like 3,
        4 or 5 digits etc
    -   Enter your guess and the BW values in row 1 of the puzzle
    -   Click start cell of the next row and press F1
    -   Computer will recommend and enter a guess in the row
    -   If you like, play this guess on the board and get opponent response for
        BW numbers
    -   Enter BW numbers in the GuessNum game; then go to step e above for the
        next guess
    -   You can override computer guess with your own
2.  When you are playing against the computer in GuessNum game:
    -   Computer would have created a puzzle for you
    -   Start your solution by entering a guess for row 1 and click OK
    -   Computer will calculate and display BW numbers
    -   Cursor will move to the start of the next row
    -   Click F1 for guess; computer will recommend and enter a guess in the row
    -   If you wish to try computer guess click; next step will be c above

Note: Computer recommended guess may not be the best guess. This is simply
because of time limitations as the program will not evaluate every single
option. See Solution Technique.

### Displaying numbers as pictures and letters

GuessNum puzzles are based on numbers 1 to 9. However you can use pictures or
letters instead of numbers. The basic logic and calculations remain the same but
pictures or letters are displayed, one corresponding to each number. You can
select quite a large variety of 9-picture-sets for this purpose. Use Options
menu to set numbers/pictures/letters/circles option and select which pictures to
use for pictures option.

1.  Using numbers
    -   This is straight forward, most common and default option for GuessNum
    -   Numbers 1 to 9 are used in all target numbers and clues
    -   Cannot have duplicate numbers in target number size above 6
    -   Use Options menu to set display to numbers
2.  Using pictures
    -   Numbers are replaced by pictures of your choice
    -   Download [http://www.ihsan.biz/common/exe/guessnumpictures.zip](60
        GuessNum pictures) and unzip to the directory where GuessNum is
        installed
    -   Once downloaded you can select around 60 styles of pictures
    -   Pictures are not printed when you print a puzzles; only corresponding
        numbers will be printed
    -   Picture are good option to teach younger users
3.  Using letters
    -   Numbers are replaced by letters; default assignment is letters A to I
        for numbers 1 to 9
    -   If you create a puzzle with a given target in letters, GuessNum will
        automatically assign letters to numbers. For example for a puzzle size
        of 5 you can set the target to HELLO. Program will generate clues
        accordingly with final answer being HELLO.
    -   In order to specify a letter target rightclick on 'create puzzle'
        button. In the input box enter the target letters like LOVELY for 6
        digit puzzle size. A puzzle will be created with the specified target
    -   Cannot have duplicate letters in puzzle size 7 and above
    -   Letters are good option to create interesting sounding targets
4.  Using circles
    -   Numbers 1 to 9 are replaced by 9 circles
    -   Use 'circles' to get GuessNum puzzle display and print like a standard
        Mastermind puzzle
    -   Circles will be printed when you print a puzzle

### Printing puzzles

Puzzles can be printed in a numbers of ways:

-   Print the current puzzle - one page puzzle will be printed
-   Copy to clipboard - you can then paste the puzzle to other applications
-   Print multiple puzzles from a file - four puzzles per page will be
    printed

Note that pictures will be printed only when you select number display as
'circle'. This is similar to Mastermind peg colours display. Any other picture
types will not be printed. TOP

### Solution technique

Computer uses following steps to solve or create a puzzle:

-   Start with a set of all possible numbers. Like 729 possibilities for a 3
    digit number: 111 to 999, with duplicates allowed.
-   Given a value of BW numbers, remove all possibilities from the set that
    would not give the same BW count
-   For each possible guess calculate how many possibilities from the set would
    be eliminated for each possible BW count. Rank the guess as the least of
    these values. The next guess should be where we have maximum eliminations.
-   Step 3 could take a long time when we have a large digit number, like for a
    6 digit number with duplicates allowed would have 531,441 choices at the
    outset. Computer will take a subset of option numbers to reduce calculation
    time. Solutions or puzzle clues therefore may not be optimum. However,
    generally the computer will be able to solve a puzzle in around 6 tries.
-   Go back to step 2 until we have the answer

### About GuessNum Program

This program is free to use and distribute but cannot be used for commercial
purposes. Thanks to Noah Bennett.