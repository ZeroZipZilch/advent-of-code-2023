import re

def run(input_rows):
  max_red_cubes = 12
  max_green_cubes = 13
  max_blue_cubes = 14

  legal_games = []

  for row in input_rows:
    game_id = re.findall(r'Game (\d+)', row)[0]
    game_sets = row[7:].split(';')

    print(game_id)
    print(game_sets)

    is_game_illegal = False

    for game_set in game_sets:
      is_red_illegal = True in [int(cube) > max_red_cubes for cube in re.findall(r'(\d+) red', game_set)]
      is_green_illegal = True in [int(cube) > max_green_cubes for cube in re.findall(r'(\d+) green', game_set)]
      is_blue_illegal = True in [int(cube) > max_blue_cubes for cube in re.findall(r'(\d+) blue', game_set)]

      if is_red_illegal or is_green_illegal or is_blue_illegal:
        is_game_illegal = True

        break

    if not is_game_illegal:
      legal_games.append(int(game_id))
      
  print("Legal sum: ", sum(legal_games))