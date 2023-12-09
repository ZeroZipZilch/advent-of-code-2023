import numpy as np

def run(input_rows: list[str]):
  # Make a simple list from 2 to 9 and then T, J, Q, K, A
  cards = ['J'] + list(map(str, range(2, 10))) + ['T', 'Q', 'K', 'A']
  
  hands = [[] for _ in range(7)]

  possible_hands = [ 'high_card', 'one_pair', 'two_pairs', 'three_of_a_kind', 'full_house', 'four_of_a_kind', 'five_of_a_kind' ]

  possible_hands_values = {
    11111: 'high_card',
    21110: 'one_pair',
    22100: 'two_pairs',
    31100: 'three_of_a_kind',
    32000: 'full_house',
    41000: 'four_of_a_kind',
    50000: 'five_of_a_kind'
  }

  # Loop through all hands of cards
  # Insert them into the hands list as a list of cards

  # To figure out the hand type:
  # Loop through each card in the hand, and add the card to a dict of string, int (?)
  # For each duplicate card, increment the int by 1

  # Sort the integers into a list from higehst to lowest
  # If the first integer is 5, it's a five of a kind
  # If the first integer is 4, it's a four of a kind
  # If the first integer is 3, check if the second integer is 2, if so, it's a full house, otherwise it's a three of a kind
  # If the first integer is 2, check if the second integer is 2, if so, it's two pairs, otherwise it's a pair
  # If the first integer is 1, it's a high card
  
  for hand in input_rows:
    hand, bid = hand.split(' ')
    hand_score = list(hand)
    jays = 0
    
    type_dict = dict()

    for char in hand:
      char_value = 1

      if char == 'J':
        jays += 1 
        char_value = 0

      type_dict[char] = type_dict[char] + char_value if char in type_dict else char_value

    type_list = list(type_dict.values())
    type_list.sort(reverse=True)

    if jays == 5:
      type_list = [5]
    elif 'J' in type_dict:
      # Fill first index in type_list up to +1 for each J, up to a max of 5
      # Then continue on to the next index if there are more Js
      type_list[-1] = jays - 1
      from_index = 0
      to_index = len(type_list) - 1

      for i in range(jays):
        type_list[from_index] += 1

        if type_list[to_index] != 0:
          type_list[to_index] -= 1
        else:
          del type_list[to_index]
          to_index -= 1

        if type_list[from_index] == 5:
          from_index += 1

        if to_index <= from_index:
          break
      
    type_score = int(''.join(map(str, type_list)).ljust(5, '0'))

    hand_type = possible_hands_values[type_score]
      

    # Loop through each card in the hand, and multiply by 10^n where n is the index of the card in the cards list
    for i, card in enumerate(hand_score):
      hand_score[i] = (cards.index(card) + 2) * 10 ** ((len(hand_score) - i - 1) * 2) # Multiply exponent by 2 for edge-cases where numbers overcome "stronger" numbers
    
    hand_value = sum(hand_score)
    
    # Divide the hands_array into a list of lists representing each type
    # Then sort the list of lists from lowest to higehst
    # Then loop through each type, starting from the lowest,
    # And assigns an integer to each hand, from lowest to highest

    hands[possible_hands.index(hand_type)].append((hand_value, bid, hand))

  # Sort the hands in each type from lowest to highest and concatenate them into a single list
  hands = [hand for hand_type in hands for hand in sorted(hand_type)]
  
  total_winnings = sum([int(hand[1]) * (i + 1) for i, hand in enumerate(hands)])

  print(total_winnings)