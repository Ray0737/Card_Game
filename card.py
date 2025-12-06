import random
import os

deck_of_cards = ['2c', '3c', '4c', '5c', '6c', '7c', '8c', '9c', 'Tc', 'Jc', 'Qc', 'Kc', 'Ac', 
                 '2d', '3d', '4d', '5d', '6d', '7d', '8d', '9d', 'Td', 'Jd', 'Qd', 'Kd', 'Ad', 
                 '2h', '3h', '4h', '5h', '6h', '7h', '8h', '9h', 'Th', 'Jh', 'Qh', 'Kh', 'Ah', 
                 '2s', '3s', '4s', '5s', '6s', '7s', '8s', '9s', 'Ts', 'Js', 'Qs', 'Ks', 'As']


all_players = []
placed_deck = []

def sort_deck(deck):
    suit_order = {'c': 0, 'd': 1, 'h': 2, 's': 3}
    rank_order = {'2': 0, '3': 1, '4': 2, '5': 3, '6': 4, '7': 5, '8': 6, '9': 7, 'T': 8, 'J': 9, 'Q': 10, 'K': 11, 'A': 12}

    def get_sort_key(card):
        rank = card[:-1]
        suit = card[-1]
        if rank in rank_order and suit in suit_order:
            return (rank_order[rank], suit_order[suit])
        return (0, 0) # Fallback

    deck.sort(key=get_sort_key)
    return deck

def clear_console():
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')



try:
    player_count = int(input("How many players (Max 6): "))
    if not 1 <= player_count <= 6:
        print("Invalid player count. Setting to 4.")
        player_count = 4
except ValueError:
    print("Invalid input. Setting to 4 players.")
    player_count = 4

random.shuffle(deck_of_cards)
index_size = 52 / player_count

for i in range(player_count):
    hand = deck_of_cards[int(index_size * i):int(index_size * (i + 1))]
    sorted_hand = sort_deck(hand) 
    all_players.append(sorted_hand) 
    
    clear_console() 
    print(f"Player {i+1}'s hand:")
    print(sorted_hand)

    input_val = input("Press ENTER to pass to the next player: ")
    if input_val.lower() == "q": 
        break
    clear_console()


print("\n--- Game Starts ---\n")

while True:
    for i in range(player_count):
        current_player_hand = all_players[i]
        player_num = i + 1  
        clear_console() 
        print(f"**It is Player {player_num}'s turn.**")
        print(f"Card order: {placed_deck}")
        print(f"Your hand: {current_player_hand}")
        chosen_input = input("Choose card(s) (e.g., 2c or 2c-2h): ").strip().lower()

        if chosen_input == "q": continue
        chosen_cards = chosen_input.split("-")
        
        valid_play = True
        for card in chosen_cards:
            if card not in current_player_hand:
                print(f"Error: Card '{card}' is not in your hand. Please try again.")
                valid_play = False
                break
            if not current_player_hand:
                print(f"\n*** Player {player_num} wins! ***")
                exit() 
            else:
                placed_deck.append(card)
                current_player_hand.remove(card)
            
        print(f"Player {player_num} played: {chosen_cards}")
            

        input("Press ENTER to clear and pass to the next player...")
        clear_console()
print("Game Over")
