import re

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
        source_range_start = source_range_start,
        total = range_length,
        diff = destination_range_start - source_range_start 
      )

      if map_mapper_value not in map_mapper[current_map]:
        map_mapper[current_map].append(map_mapper_value)
  
  
  seeds = get_seeds_over_map(seeds)
    
  print(min(seeds))


def get_seeds_over_map(seeds: [int]) -> int:
  for current_map_index in range(len(map_order)):
    current_map = map_order[current_map_index]
    
    for (i, seed_number) in enumerate(seeds):
      for j in range(len(map_mapper[current_map])):
        is_seed_in_start_range = seed_number >= map_mapper[current_map][j]["source_range_start"] and seed_number < map_mapper[current_map][j]["source_range_start"] + map_mapper[current_map][j]["total"]

        if is_seed_in_start_range:
          seeds[i] = seed_number + map_mapper[current_map][j]["diff"]
    
  return seeds