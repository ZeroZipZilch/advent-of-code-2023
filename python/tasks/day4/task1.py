import re

def run(scratchcards: list[str]):
  total = 0

  for card in scratchcards:
    card = re.split('Card [ 0-9]+: ', card)[1]
    card_total = parse_card(card)
    
    total += card_total

  print(total)

def parse_card(card: str) -> int:
  card_score = 0

  winning_numbers = []

  after_bar = False

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
      card_score = card_score * 2 if card_score >= 1 else 1

  return card_score