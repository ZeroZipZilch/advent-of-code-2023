import re

def run(input_rows: list[str]):
  pattern_list = list(input_rows[0])
  pattern_length = len(pattern_list)
  pattern_iterator = 0

  current_path = "AAA"
  steps = 0

  map_list = dict()

  for row in input_rows[2:]:
    path, left_destination, right_destination = re.match(r"([A-Z]{3}) = \(([A-Z]{3}), ([A-Z]{3})\)", row).groups()

    map_list[path] = { 'L': left_destination, 'R': right_destination }

  while current_path != 'ZZZ':
    current_path = map_list[current_path][pattern_list[pattern_iterator]]
    pattern_iterator += 1
    steps += 1

    if pattern_iterator == pattern_length:
      pattern_iterator = 0

  print(steps)