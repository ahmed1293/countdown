# Numbers

Given six numbers and one target number, try to generate the target by using standard operations (+, -, *, /) on the six numbers. No number can be used more than once.
Normal rules will restrict the number of 'large' (> 25) and 'small' numbers. Here, any input is accepted.

### Prerequisites

[Reverse Polish Notation](https://en.wikipedia.org/wiki/Reverse_Polish_notation) (RPN). I discovered this thanks
to [this](http://www.datagenetics.com/blog/august32014/index.html) blog.

## async

`python numbers_async.py`, then follow instructions. 10 solutions are found by default, change the `NO_OF_SOLUTIONS` variable
in `numbers_async.py` to change this.

#### Implementation

1. Compute all combinations of operators (5 operators with repeats results is 56 permutations).
2. For each combination of operators, find all permutations of those operators with the numbers. There should now be
56 lists of permutations, each with a length of 39916800. An example permutation is: 
`(1, '+', 2, 3, '*', 4, 5, 6, '+', '+', '-')`
3. Loop through each all 56 lists, concurrently, and compute each value.
4. Once a solution is found, add it to a common set of solutions.
5. Stop when the number of solutions is equal to the required value.

## sync

`pypy3 numbers_sync.py`, then follow instructions (standard Python is about 25x as slow).

#### Implementation

1. Compute all combinations of operators (5 operators with repeats results is 56 permutations).
2. Loop through operator combinations. For each combination:
    - Find all permutations of operators mixed with the numbers (39916800 permutations if 6 numbers).
    - Compute the value of each permutation (making use of RPN notation).
    - Exit if match is found.

# Letters

Given some random letters, try to generate the longest word possible.

#### Usage
`python letters.py`, then follow instructions. 

Note that the Unix "words" file, found in `/usr/share/dict/words`, is used as a dictionary so this script probably wont work on Windows.

### _old/

My (not so nice) implementation when I was first learning Python. 