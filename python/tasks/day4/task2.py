import re

def run(scratchcards: list[str]):
  card_total = parse_cards(scratchcards)

  print(card_total)

def parse_cards(scratchcards: list[str]) -> int:
  occurences = {}
  total = [1] * len(scratchcards)

  for i, scratchcard in enumerate(scratchcards):
    card_number, card = re.match('Card[ ]+([\d]+): (.+)', scratchcard).groups()
    card_number = int(card_number)

    won_the_next_x_cards = calculate_winnings(card)
    occurences[i + 1] = occurences.get(i + 1, 0) + total[i]
    print("Occurences: ", occurences)

    if won_the_next_x_cards > 0:
      print("Entering loop for i value {index} and will loop until index {until}".format(index = i, until = i + won_the_next_x_cards))
      
    for j in range(won_the_next_x_cards):
      print("Increasing total for index {index} by a {increase}".format(index = i + j + 1, increase = total[i]))
      total[i + j + 1] = total[i + j + 1] + total[i]
      print("Total", total)

  return sum(total[:i + 1])


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