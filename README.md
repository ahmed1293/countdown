### Numbers

Given six numbers and one target number, try to generate the target by using standard operations (+, -, *, /) on the six numbers. No number can be used more than once.
Normal rules will restrict the number of 'large' (> 25) and 'small' numbers. Here, any input is accepted.

#### Usage 

`python Numbers.py`, then follow instructions. 

_Tip:_ use [pypy](https://pypy.org) for 25x quicker execution time! 

#### Implementation

Prerequisite knowledge: [Reverse Polish Notation](https://en.wikipedia.org/wiki/Reverse_Polish_notation) (RPN). I discovered this thanks
to [this](http://www.datagenetics.com/blog/august32014/index.html) blog.

1. Compute all combinations of operators (5 operators with repeats results is 56 permutations).
2. Loop through operator combinations. For each combination:
    - Find all permutations of operators mixed with the numbers (39916800 permutations if 6 numbers).
    - Compute the value of each permutation using the RpnCalculator.
    - Exit if match is found.

### Letters

Given some random letters, try to generate the longest word possible.

#### Usage
`python letters.py`, then follow instructions. 

Note that the Unix "words" file, found in `/usr/share/dict/words`, is used as a dictionary so this script probably wont work on Windows.

