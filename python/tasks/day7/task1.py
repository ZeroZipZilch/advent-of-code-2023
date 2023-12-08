import re
import math

def run(input_rows: list[str]):
  # Make a simple list from 2 to 9 and then T, J, Q, K, A
  cards = list(map(str, range(2, 10))) + ['T', 'J', 'Q', 'K', 'A']
  
  hands = []

  # Loop through all hands of cards
  # Insert them into the hands list as a list of cards
  
  for hand in input_rows:
    hand, bid = hand.split(' ')
    hands.append(list(hand))

  hands.sort(key=lambda hand: cards.index(hand[0][0]))
  
  pass