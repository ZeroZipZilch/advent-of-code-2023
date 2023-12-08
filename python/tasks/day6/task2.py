import re
import math

def run(input_rows: list[str]):
  time: int = int(''.join(re.compile('([\d]+)').findall(input_rows[0])))
  record_distance: int = int(''.join(re.compile('([\d]+)').findall(input_rows[1])))

  ways_to_win_race = 0

  for acceleration in range(time):
    total_distance = acceleration * (time - acceleration)
    
    if total_distance > record_distance:
      ways_to_win_race += 1

  print(ways_to_win_race)