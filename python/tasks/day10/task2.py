import re
import sys
import itertools
import math
import collections

def run(input_rows: list[str]):
  total_step_count = 1
  inner_tiles_count = 0
  input_lists = []
  pipe_map = dict()

  for i, row in enumerate(input_rows):
    input_lists.append(list(row.replace("7", "A")))

  # rename from_direction and to_direction to from_offset and to_offset?
  path_symbols = {
    "|": { 
      "x0_y1": { "x": 0, "y": 1 },  # From Up to Down
      "x0_y-1": { "x": 0, "y": -1 } # From Down to Up
    },
    "-": { 
      "x1_y0": { "x": 1, "y": 0 }, # From Left to Right
      "x-1_y0": { "x": -1, "y": 0 } # From Right to Left
    },
    "L": { 
      "x-1_y0": { "x": 0, "y": -1 }, # From Right to Up
      "x0_y1": { "x": 1, "y": 0 } # From Up to Right
    },
    "J": { 
      "x1_y0": { "x": 0, "y": -1 }, # From Left to Up
      "x0_y1": { "x": -1, "y": 0 } # From Up to Left
    },
    "A": { 
      "x1_y0": { "x": 0, "y": 1 }, # From Left to Down
      "x0_y-1": { "x": -1, "y": 0 } # From Down to Left
    },
    "F": { 
      "x-1_y0": { "x": 0, "y": 1 }, # From Right to Down
      "x0_y-1": { "x": 1, "y": 0 } # From Down to Right
    },
  }

  start_x, start_y = find_start_x_y(input_rows)
  current_directions, start_symbol = find_start_adjacent(start_x, start_y, path_symbols, input_lists)

  walking = True

  while walking:
    for (i, direction_info) in enumerate(current_directions):
      x, y = direction_info["current_position"].values()

      # Change the value of the previous symbol to the total step count
      current_directions[i] = find_adjacent(direction_info, path_symbols, input_lists)
      # input_lists[y][x] = total_step_count
      pipe_map[(x, y)] = total_step_count

      if current_directions[i] is None:
        print(f"Total step count: {int(total_step_count / 2)}")

        walking = False
        break
    
    total_step_count += 1

  for y, row in enumerate(input_lists):
    is_inside = False
    last_char = None

    for x, char in enumerate(row):
      if char == "-" and (x, y) in pipe_map:
        continue

      if char == 'S':
        char = start_symbol

      if (x, y) in pipe_map and (char == "|" or (last_char != 'F' and char == 'J') or (last_char != 'L' and char == "A") or char in ["L", "F"]):
        is_inside = not is_inside

      if char in ["L", "J", "A", "F"]:
        last_char = char

      if (x, y) not in pipe_map and is_inside:
        input_lists[y][x] = "I"
        inner_tiles_count += 1
      elif char == '.': 
        input_lists[y][x] = "0"
  
    
  print(f"Total enclosed pipes: {inner_tiles_count}")


def find_start_adjacent(x: int, y: int, path_symbols, input_lists):
  new_directions = []

  for (x_offset, y_offset) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
    try:
      new_x, new_y = x + x_offset, y + y_offset
      current_symbol = input_lists[new_y][new_x]

      if current_symbol in path_symbols:
        symbol_directions = path_symbols[current_symbol].keys()

        if f"x{x_offset}_y{y_offset}" in symbol_directions:
          direction = {
            "current_position": { "x": new_x, "y": new_y },
            "from_direction": { "x": x_offset, "y": y_offset }
          }

          new_directions.append(direction)
    except IndexError:
      continue
    except KeyError:
      continue
  
  symbol = None

  connections = []

  for direction in new_directions:
    x, y = direction["from_direction"].values()
    
    if x == 0 and y == -1:
      connections.append("N")
    elif x == 0 and y == 1:
      connections.append("S")
    elif x == -1 and y == 0:
      connections.append("W")
    elif x == 1 and y == 0:
      connections.append("E")

  if all(connection in connections for connection in ["N", "S"]):
    symbol = "|"
  elif all(connection in connections for connection in ["W", "E"]):
    symbol = "-"
  elif all(connection in connections for connection in ["N", "E"]):
    symbol = "L"
  elif all(connection in connections for connection in ["N", "W"]):
    symbol = "J"
  elif all(connection in connections for connection in ["S", "W"]):
    symbol = "A"
  elif all(connection in connections for connection in ["S", "E"]):
    symbol = "F"

  return new_directions, symbol


def find_start_x_y(input_rows: list[str]):
  row_length = len(input_rows[0])
  s_iter = next(re.finditer(r"S", ''.join(input_rows)))

  x = s_iter.start() % row_length
  y = s_iter.start() // row_length

  return (x, y)


def find_adjacent(direction_info, path_symbols, input_lists):
  try:
    current_position, from_direction = direction_info.values()

    x, y = current_position.values()
    origin_x_offset, origin_y_offset = from_direction.values()

    current_symbol = input_lists[y][x]

    origin_offset_key = f"x{origin_x_offset}_y{origin_y_offset}"
    to_x, to_y = path_symbols[current_symbol][origin_offset_key].values()

    next_direction = {
      "current_position": { "x": x + to_x, "y": y + to_y },
      "from_direction": { "x": to_x, "y": to_y }
    }

    return next_direction
  except KeyError:
    print("KeyError")
  except IndexError:
    print("IndexError")


