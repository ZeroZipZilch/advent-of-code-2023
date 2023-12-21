# Day 16 - Brainstorm


## Basic Instructions

- Start at the first column of the first row (0, 0) or "top left"
- Different symbols change direction in different ways, depending on the current direction and the symbol.


## Symbols


### Mirrors

Symbol | Current Direction | New direction

/      | Right             | Up
/      | Down              | Left
/      | Left              | Down
/      | Up                | Right

\      | Right             | Down
\      | Down              | Right
\      | Left              | Up
\      | Up                | Left


### Special symbols

Symbol | Meaning

|      | Pipe, split beam into both vertical directions
-      | Dash, split beam into both horizontal directions
.      | Dot, empty space


## Beam

A beam has a number of properties:
- position, Tuple with two values, hosting the x and y value for the position, in the shape of (x, y).
- last_direction, Tuple with two values, hosting the last registered move for the beam.

Start position would be (0, 0) and last_direction would be (1, 0) (right).


## Beams

Beams is a list of beams.

When a split happens, we remove the current beam from its index in the list of beams, and then we
create two new beams and add them to the linked list.


### Directional lookup

direction_lookup = {
  (1, 0): {
    '.': (1, 0),
    '/': (0, -1),
    '\\': (0, 1)
  },
  (0, 1): {
    '.': (0, 1),
    '/': (-1, 0),
    '\\': (1, 0)
  },
  (-1, 0): {
    '.': (-1, 0),
    '/': (0, 1),
    '\\': (0, -1)
  },
  (0, -1): {
    '.': (0, -1),
    '/': (1, 0),
    '\\': (-1, 0)
  },
}


### Splits
When a split happens, remove the current beam and create two new beams.

Each beam should have their positions influenced by the directions
in the values of the split symbol, originating from the split position,
and also their respective last_direction as the last_direction for each beam.

splits = {
  '|': [(0, -1), (0, 1)], # appended to `beams`
  '-': [(-1, 0), (1, 0)], # appended to `beams`
}

