Steps taken:

. . . . . 0
. S - 7 . 1
. | . | . 2
. L - J . 3
. . . . . 4
0 1 2 3 4


F -> - -> 7 -> | -> J -> - -> L -> |

{
  "F": { from: (1, 2), current: (1, 1),  to: (2, 1) },
  "-": { from: (1, 1), current: (2, 1),  to: (3, 1) },
  "7": { from: (2, 1), current: (3, 1),  to: (3, 2) },
  "|": { from: (3, 1), current: (3, 2),  to: (3, 3) },
  "J": { from: (3, 2), current: (3, 3),  to: (2, 3) },
  "-": { from: (3, 3), current: (2, 3),  to: (1, 3) },
  "L": { from: (2, 3), current: (1, 3),  to: (1, 2) },
  "|": { from: (1, 3), current: (1, 2),  to: (1, 1) },
}

{
  "F": { from: (2, 1), current: (1, 1),  to: (1, 2) },
  "|": { from: (1, 1), current: (1, 2),  to: (1, 3) },
  "L": { from: (1, 2), current: (1, 3),  to: (2, 3) },
  "-": { from: (1, 3), current: (2, 3),  to: (3, 3) },
  "J": { from: (2, 3), current: (3, 3),  to: (3, 2) },
  "|": { from: (3, 3), current: (3, 2),  to: (3, 1) },
  "7": { from: (3, 2), current: (3, 1),  to: (2, 1) },
  "-": { from: (3, 1), current: (2, 1),  to: (1, 1) },
}

Offsets:

{
  "F": { back: (0, 1), forward: (1, 0) },
  "-": { back: (-1, 0), forward: (1, 0) },
  "7": { back: (-1, 0), forward: (0, 1) },
  "|": { back: (0, -1), forward: (0, 1) },
  "J": { back: (0, -1), forward: (-1, 0) },
  "-": { back: (1, 0), forward: (-1, 0) },
  "L": { back: (1, 0), forward: (0, -1) },
  "|": { back: (0, 1), forward: (0, -1) },
}

{
  "F": { back: (1, 0), forward: (0, 1) },
  "|": { back: (0, -1), forward: (0, 1) },
  "L": { back: (0, -1), forward: (1, 0) },
  "-": { back: (-1, 0), forward: (1, 0) },
  "J": { back: (-1, 0), forward: (0, -1) },
  "|": { back: (0, 1), forward: (0, -1) },
  "7": { back: (0, 1), forward: (-1, 0) },
  "-": { back: (1, 0), forward: (-1, 0) },
}

#### Note 1 ################################################
# A symbol is inversed when the offset is inverted in the  #
# from_direction of the symbol in path_symbols.            #
#                                                          #
# F, L, J and 7 are all inverted when changing directions. #
# On top of that, the values of L and 7 are also negated.  #
###### # # # # # # # # # # # # # # # # # # # # # # # # # # #

To determine if the direction is inverted, we can:

1. Subtract from_direction and current_position
2. If the result is inversed as per [Note 1](#note-1), then the from_direction is inverted.
3. If that is the case, then the to_direction needs to be inversed as well.

. . . . . 0
. F - 7 . 1
. | . | . 2
. L - J . 3
. . . . . 4
0 1 2 3 4


#### Note 2 ################################################
# Measures need to be taken to not account for symbols     #
# that are adjecent to the start position, but that are    #
# not actually valid as part of the path due to their      #
# directions instructions.                                 #
###### # # # # # # # # # # # # # # # # # # # # # # # # # # #

Test case for [Note 2](#note-2):

. J . . . 0
7 S - 7 . 1
. | . | . 2
. L - J . 3
. . . . . 4
0 1 2 3 4

Here, both the `7` and the `J` are adjecent to the start position, but they are not valid as part of the path. Thus, after the first iteration, current_paths should only contain the paths to
the `|` and the `-`.


#### Note 3 ################################################
# For part 2, I need to be able to find the "inside" of    #
# the pipe loop. Two test-cases that would be helpful, in  #
# order, one very easy and one more realistic, are:        #
###### # # # # # # # # # # # # # # # # # # # # # # # # # # #

Simple test case for [Note 3](#note-3):

. . . . . . . . . 0
. S - - - - - 7 . 1
. | . . . . . | . 2
. | . . . . . | . 3
. | . . . . . | . 4
. | . . . . . | . 5
. | . . . . . | . 6
. L - - - - - J . 7
. . . . . . . . . 8
0 1 2 3 4 5 6 7 8

More realistic test case for [Note 3](#note-3):

. . . . . . . . . . . 0
. S - - - - - - - 7 . 1
. | F - - - - - 7 | . 2
. | | . . . . . | | . 3
. | | . . . . . | | . 4
. | L - 7 . F - J | . 5
. | . . | . | . . | . 6
. L - - J . L - - J . 7
. . . . . . . . . . . 8
0 1 2 3 4 5 6 7 8 9 0

##### Note about [Note 3](#note-3) #########################
# "Inside the loop" is defined as the cells that are       #
# surrounded by the pipe loop, but not part of the pipe    #
# loop itself. The following example, where I means        #
# it counts and O means it doesn't, should make it clear:  #
##### ######################################################

. . . . . . . . . . 0
. S - - - - - - 7 . 1
. | F - - - - 7 | . 2
. | | O O O O | | . 3
. | | O O O O | | . 4
. | L - 7 F - J | . 5
. | I I | | I I | . 6
. L - - J L - - J . 7
. . . . . . . . . . 8
0 1 2 3 4 5 6 7 8 9 
