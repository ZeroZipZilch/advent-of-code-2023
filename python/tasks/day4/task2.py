import re

instance_counter = dict()

def run(scratchcards: list[str]):
  card_total = 0

  card_total = parse_cards(scratchcards[0], 0, scratchcards)



  print(card_total)

def parse_cards(card: str, index: int, scratchcards: list[str]) -> int:
  card = re.split('Card [ 0-9]+: ', card)[1]

  # 1 -> 2,3,4,5
  # 2 -> 3,4
  # 2 -> 3,4
  # 3 -> 4,5
  # 3 -> 4,5
  # 3 -> 4,5
  # 3 -> 4,5
  # 4 -> 5
  # 4 -> 5
  # 4 -> 5
  # 4 -> 5
  # 4 -> 5
  # 4 -> 5
  # 4 -> 5
  # 4 -> 5
  # 4 -> 5
  # 5 -> -
  # 5 -> -
  # 5 -> -
  # 5 -> -
  # 5 -> -
  # 5 -> -
  # 5 -> -
  # 5 -> -
  # 5 -> -
  # 5 -> -
  # 5 -> -
  # 5 -> -
  # 5 -> -
  # 5 -> -
  # 6 -> -
  
  won_the_next_x_cards = calculate_winnings(card)
  


def calculate_winnings(card):
  winning_numbers = []
  after_bar = False
  won_the_next_x_cards = 0

  for number in card.split(' '):
    if number == '':
      continue

    if number == '|':
      after_bar = True
      continue

    number = int(number)

    if not after_bar:
      winning_numbers.append(number)
      continue

    if number in winning_numbers:
      won_the_next_x_cards += 1
  
  return won_the_next_x_cards