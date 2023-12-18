?###???????? 3,2,1
.###.##.#...
.###.##..#..
.###.##...#.
.###.##....#
.###..##.#..
.###..##..#.
.###..##...#
.###...##.#.
.###...##..#
.###....##.#

Rules are simple:

The numbers indicate how many # exist in-between spaces (dots)

Basically, 3, 2, 1 means there are three groups of 3, 2, and 1 pounds (#) respectively.
Groups **have** to be separated by at least one dot (.) in both directions
Questionmarks (?) could be either a pound (#) or a dot (.), and each line
can have either one, or multiple possible arrangements.

For example, the example above has 10 possible arrangements.

However, in the example above, the first and second questionmarks (?) will **always**
be dots (.) in **every** possible arrangement, because the first group is 3, and
character indexes 1 - 3 are all pounds (#), completing the first group.

This leaves index 5 -11 to be filled by dots (.), and the group of 2 pounds and the group of 1 pound,
in several different ways. As seen by the example above, there are 10 possible arrangements.

The question is... Rather than brute-forcing the problem, is there a way to calculate the number of possible arrangements?

##### ############################################################

How many possible arrangements are there for the following?

?????????? 3,2,1
###.##.#..
###.##..#.
###.##...#
###..##.#.
###..##..#
.###.##.#.
.###.##..#
.###..##.#
..###.##.#

###.#.##..
###.#..##.
###.#...##
###..#.##.
###..#..##
.###.#.##.
.###.#..##
.###..#.##
..###.#.##

##.###.#..
##.###..#.
##.###...#
##..###.#.
##..###..#
.##.###.#.
.##.###..#
.##..###.#
..##.###.#

##.#.###..
##.#..###.
##.#...###
##..#.###.
##..#..###
.##.#.###.
.##.#..###
.##..#.###
..##.#.###

#.##.###..
#.##..###.
#.##...###
#..##.###.
#..##..###
#...##.###
.#.##.###.
.#.##..###
.#..##.###

#.###.##..
#.###..##.
#.###...##
#..###.##.
#..###..##
.#..###.##
.#.###.##.
.#.###..##
.#..###.##

Thus, if we have a group of 3, 2, and 1, and the total number of characters is 10, we end up with 54 possible arrangements.

I wonder if we can do something with binary, where dots (.) would be 0, and pounds (#) would be 1.
That just leaves out questionmarks (?), which could be either 0 or 1.

LET'S BUILD A QUANTUM COMPUTER!

Recrsive method?
Maybe.

If we have 3, 2 and 1, we can start by looping through each number