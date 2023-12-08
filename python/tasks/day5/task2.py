import re
import sys

import numpy as np

seeds = list()

map_mapper = {
  'seed_to_soil': list(),
  'soil_to_fertilizer': list(),
  'fertilizer_to_water': list(),
  'water_to_light': list(),
  'light_to_temperature': list(),
  'temperature_to_humidity': list(),
  'humidity_to_location': list()
}

map_order = ["seed_to_soil", "soil_to_fertilizer", "fertilizer_to_water", "water_to_light", "light_to_temperature", "temperature_to_humidity", "humidity_to_location"]

def run(input_rows: list[str]):
  current_map = None
  closest_location = sys.maxsize

  for row in input_rows:
    if row == '':
      continue

    if row.startswith("seeds"):
      seeds = list(map(int, re.match('seeds: (.+)', row).groups()[0].split(' ')))
    
    elif row.endswith("map:"):
      current_map = row.replace(" map:", "").replace("-", "_")
    
    else:
      destination_range_start, source_range_start, range_length = map(int, re.match('([\d]+) ([\d]+) ([\d]+)', row).groups())

      map_mapper_value = dict(
        destination_range_start = destination_range_start,
        source_range_start = source_range_start,
        length = range_length,
        diff = source_range_start - destination_range_start
      )

      if map_mapper_value not in map_mapper[current_map]:
        map_mapper[current_map].append(map_mapper_value)
  
  print(get_lowest_location_value(seeds))
    


def get_lowest_location_value(seeds: list[int]) -> int:
  seeds = np.reshape(seeds, (-1, 2))
  location_value = 0
  
  for value in range(0, 10000000000):
    location_value = value

    for current_map_index in range(len(map_order) - 1, -1, -1):
      current_map = map_mapper[map_order[current_map_index]]
      
      for map_range in current_map:
        is_value_in_destination_range = value >= map_range["destination_range_start"] and value <= map_range["destination_range_start"] + map_range["length"]

        if is_value_in_destination_range:
          value = value + map_range["diff"]
          
          if current_map_index == 0 and is_value_in_seed_range(value, seeds):
            return location_value
          else:
            break
              

def is_value_in_seed_range(value: int, seeds: list[int]) -> bool:
  for seed in seeds:
    if value >= seed[0] and value <= seed[0] + seed[1]:
      return True
  
  return False