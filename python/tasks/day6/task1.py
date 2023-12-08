import re
import math

def run(input_rows: list[str]):
  times: list[int] = list(map(int, re.compile('([\d]+)').findall(input_rows[0])))
  distances: list[int] = list(map(int, re.compile('([\d]+)').findall(input_rows[1])))

  possible_accelerations = []

  for (race, time) in enumerate(times):
    minimum_distance = distances[race]
    ways_to_win_race = 0

    for acceleration in range(time):
      total_distance = acceleration * (time - acceleration)
      
      if total_distance > minimum_distance:
        ways_to_win_race += 1
  
    possible_accelerations.append(ways_to_win_race)

  print(math.prod(possible_accelerations))