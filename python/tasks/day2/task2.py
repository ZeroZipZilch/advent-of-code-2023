import re

def run(input_rows):
  powers = []

  for row in input_rows:
    lowest_red_in_set = max([int(cube) for cube in re.findall(r'(\d+) red', row)] or [1])
    lowest_green_in_set = max([int(cube) for cube in re.findall(r'(\d+) green', row)] or [1])
    lowest_blue_in_set = max([int(cube) for cube in re.findall(r'(\d+) blue', row)] or [1])

    set_total = lowest_red_in_set * lowest_green_in_set * lowest_blue_in_set

    print("set_total:", set_total)
    powers.append(set_total)
      
  print("Sum: ", sum(powers))