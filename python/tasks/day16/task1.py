import copy
import re
import sys
import itertools
import math
import collections
import numpy as np


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


def run(input: list[str]):
  beams = [ { "position": (0, 0), "direction": (1, 0) } ]
  energized = [(0, 0)]

  grid = [ [ x for x in line ] for line in input ]
  debug_grid = copy.deepcopy(grid)

  while len(beams) > 0:
    for (i, beam) in enumerate(beams):
      position = beam["position"]
      direction = beam["direction"]

      x_position = position[0]
      y_position = position[1]

      x_direction = direction[0]
      y_direction = direction[1]

      new_x_position = x_position + x_direction
      new_y_position = y_position + y_direction

      if new_x_position < 0 or new_x_position >= len(grid[0]) or new_y_position < 0 or new_y_position >= len(grid):
        beams.remove(beam)

        break

      new_position = (new_x_position, new_y_position)
      debug_grid[new_y_position][new_x_position] = 'X'

      symbol = grid[new_y_position][new_x_position]


      if symbol == '-' or symbol == '|':
        if new_position not in energized:
          energized.append(new_position)

        beams.remove(beam)

        for beam in split_beam(symbol, new_position):
          beams.append(beam)
        
        continue

      new_direction = direction_lookup[direction][symbol]

      if new_position in energized and tuple(np.array(new_position) + np.array(new_direction)) in energized:
        beams.remove(beam)

        break
      

      if new_position not in energized:
        energized.append(new_position)

      beams[i] = { "position": new_position, "direction": new_direction }
    
    for line1, line2 in zip(debug_grid, grid):
      print(''.join(line1), '  ', ''.join(line2))
    print('')
  
  print(len(energized))


def split_beam(symbol, origin):
  if symbol == '-':
    return {
      "position": origin,
      "direction": (-1, 0)
    }, {
      "position": origin,
      "direction": (1, 0)
    }
  elif symbol == '|':
    return {
      "position": origin,
      "direction": (0, -1)
    }, {
      "position": origin,
      "direction": (0, 1)
    }