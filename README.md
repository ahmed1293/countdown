## Intro

I used to watch a lot of "8 out of 10 Cats does Countdown", and I generally sucked on both rounds. So, I decided to automate them.

### Numbers

Given six numbers and one target number, try to generate the target by using standard operations (+, -, *, /) on the six numbers. No number can be used more than once.
Normal rules will restrict the number of 'large' (> 25) and 'small' numbers. Here, any input is accepted.

#### Usage 

`python Numbers.py`, then follow instructions.

#### Implementation

Prerequisite knowledge: [Reverse Polish Notation](https://en.wikipedia.org/wiki/Reverse_Polish_notation) (RPN). I discovered this thanks
to [this](http://www.datagenetics.com/blog/august32014/index.html) blog.

1. Compute all combinations of operators (5 operators with repeats results in 56 permutations).
2. Loop through operator combinations. For each combination:
    3. Find all permutations of operators mixed with the numbers (39916800 permutations if 6 numbers).
    4. Filter out invalid combinations.
    5. Filter based on calculated value matching target.
    6. Exit if match is found.


### Letters

Given some random letters, try to generate the longest word possible.

#### Usage
`python LettersToWords.py`, then follow instructions. 

Note that the Unix "words" file, found in `/usr/share/dict/words`, is used as a dictionary so this script probably wont work on Windows.

