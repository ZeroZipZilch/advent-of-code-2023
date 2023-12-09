import re
import math

def run(input_rows: list[str]):
  pattern_list = list(input_rows[0])
  pattern_length = len(pattern_list)
  pattern_iterator = 0

  steps = 0
  map_directions, current_paths = map_paths(input_rows)

  path_lengths = dict()

  path: str
  for (i, path) in enumerate(current_paths):
    while path[-1] != 'Z':
      direction = pattern_list[pattern_iterator]

      path = map_directions[path][direction]
      current_paths[i] = path
      
      pattern_iterator += 1
      steps += 1

      if pattern_iterator == pattern_length:
        pattern_iterator = 0
    
    path_lengths[path] = steps - sum(path_lengths.values())
    
    lcm = math.lcm(*path_lengths.values())

  print(lcm)


def map_paths(input_rows: list[str]):
  map_directions = dict()
  current_paths = []

  for row in input_rows[2:]:
    path, left_destination, right_destination = re.match(r"([A-Z0-9]{3}) = \(([A-Z0-9]{3}), ([A-Z0-9]{3})\)", row).groups()

    if path[-1] == 'A':
      current_paths.append(path)

    map_directions[path] = { 'L': left_destination, 'R': right_destination }

  return map_directions, current_paths