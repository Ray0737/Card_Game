import random
import os

deck_of_cards = ['2c', '3c', '4c', '5c', '6c', '7c', '8c', '9c', 'Tc', 'Jc', 'Qc', 'Kc', 'Ac', 
                 '2d', '3d', '4d', '5d', '6d', '7d', '8d', '9d', 'Td', 'Jd', 'Qd', 'Kd', 'Ad', 
                 '2h', '3h', '4h', '5h', '6h', '7h', '8h', '9h', 'Th', 'Jh', 'Qh', 'Kh', 'Ah', 
                 '2s', '3s', '4s', '5s', '6s', '7s', '8s', '9s', 'Ts', 'Js', 'Qs', 'Ks', 'As']

player1 = []
player2 = []
player3 = []
player4 = []
player5 = []
player6 = []
placed_deck = []


def sort_deck(deck):
    suit_order = {'c': 0, 'd': 1, 'h': 2, 's': 3}
    rank_order = {'2': 0, '3': 1, '4': 2, '5': 3, '6': 4, '7': 5, '8': 6, '9': 7, 'T': 8, 'J': 9, 'Q': 10, 'K': 11, 'A': 12}

    def get_sort_key(card):
        rank = card[:-1]  # 'A'
        suit = card[-1]
        return (rank_order[rank],suit_order[suit])

    deck.sort(key=get_sort_key)
    return deck

def clear_console():
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')

player = int(input("How many players (Max 6): "))
random.shuffle(deck_of_cards)
index = 52/player

for i in range (player):
    clear_console() 
    sorted_deck = sort_deck(deck_of_cards[int(index*i):int(index*(i+1))])
    print(sorted_deck)
    if i == 0:
        player1.append(sorted_deck)
    elif i == 1:
        player2.append(sorted_deck)
    elif i == 2:
        player3.append(sorted_deck)
    elif i == 3:
        player4.append(sorted_deck)
    elif i == 4:
        player5.append(sorted_deck)
    elif i == 5:
        player6.append(sorted_deck)

    if input("pass (p): ") == "p": clear_console()    

while True:
    for i in range (player):
        clear_console()  
        print(f"Card order: {placed_deck} | (press q to skip)")
        if i == 0:
            print(player1)
            chosen = input("Choose card:")
            if chosen == "p": continue
            placed_deck.append(chosen)
            deck_of_cards.remove(chosen)
            player1.remove(chosen)
            clear_console()  
        if i == 1:
            print(player2)
            chosen = input("Choose card:")
            if chosen== "p": continue
            placed_deck.append(chosen)
            deck_of_cards.remove(chosen)
            player2.remove(chosen)
            clear_console()  
        if i == 2:
            print(player3)
            chosen = input("Choose card:")
            if chosen == "p": continue
            placed_deck.append(chosen)
            deck_of_cards.remove(chosen)
            player3.remove(chosen)
            clear_console()  
        if i == 3:
            print(player4)
            chosen = input("Choose card:")
            if chosen== "p": continue
            placed_deck.append(chosen)
            deck_of_cards.remove(chosen)
            player4.remove(chosen)
            clear_console()  
        if i == 4:
            print(player5)
            chosen = input("Choose card:")
            if chosen == "p": continue
            placed_deck.append(chosen)
            deck_of_cards.remove(chosen)
            player5.remove(chosen)
            clear_console()  
        if i == 5:
            print(player6)
            chosen = input("Choose card:")
            if chosen == "p": continue
            placed_deck.append(chosen)
            deck_of_cards.remove(chosen)
            player6.remove(chosen)
            clear_console()

import random
import os

deck_of_cards = ['2c', '3c', '4c', '5c', '6c', '7c', '8c', '9c', 'Tc', 'Jc', 'Qc', 'Kc', 'Ac', 
                 '2d', '3d', '4d', '5d', '6d', '7d', '8d', '9d', 'Td', 'Jd', 'Qd', 'Kd', 'Ad', 
                 '2h', '3h', '4h', '5h', '6h', '7h', '8h', '9h', 'Th', 'Jh', 'Qh', 'Kh', 'Ah', 
                 '2s', '3s', '4s', '5s', '6s', '7s', '8s', '9s', 'Ts', 'Js', 'Qs', 'Ks', 'As']

player1 = []
player2 = []
player3 = []
player4 = []
player5 = []
player6 = []
placed_deck = []


def sort_deck(deck):
    suit_order = {'c': 0, 'd': 1, 'h': 2, 's': 3}
    rank_order = {'2': 0, '3': 1, '4': 2, '5': 3, '6': 4, '7': 5, '8': 6, '9': 7, 'T': 8, 'J': 9, 'Q': 10, 'K': 11, 'A': 12}

    def get_sort_key(card):
        rank = card[:-1]  # 'A'
        suit = card[-1]
        return (rank_order[rank],suit_order[suit])

    deck.sort(key=get_sort_key)
    return deck

def clear_console():
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')

player = int(input("How many players (Max 6): "))
random.shuffle(deck_of_cards)
index = 52/player

for i in range (player):
    clear_console() 
    sorted_deck = sort_deck(deck_of_cards[int(index*i):int(index*(i+1))])
    print(sorted_deck)
    if i == 0:
        player1.append(sorted_deck)
    elif i == 1:
        player2.append(sorted_deck)
    elif i == 2:
        player3.append(sorted_deck)
    elif i == 3:
        player4.append(sorted_deck)
    elif i == 4:
        player5.append(sorted_deck)
    elif i == 5:
        player6.append(sorted_deck)

    if input("pass (p): ") == "p": clear_console()    

while True:
    for i in range (player):
        clear_console()  
        print(f"Card order: {placed_deck} | (press q to skip)")
        if i == 0:
            print(player1)
            chosen = input("Choose card:")
            if chosen == "p": continue
            placed_deck.append(chosen)
            deck_of_cards.remove(chosen)
            player1.remove(chosen)
            clear_console()  
        if i == 1:
            print(player2)
            chosen = input("Choose card:")
            if chosen== "p": continue
            placed_deck.append(chosen)
            deck_of_cards.remove(chosen)
            player2.remove(chosen)
            clear_console()  
        if i == 2:
            print(player3)
            chosen = input("Choose card:")
            if chosen == "p": continue
            placed_deck.append(chosen)
            deck_of_cards.remove(chosen)
            player3.remove(chosen)
            clear_console()  
        if i == 3:
            print(player4)
            chosen = input("Choose card:")
            if chosen== "p": continue
            placed_deck.append(chosen)
            deck_of_cards.remove(chosen)
            player4.remove(chosen)
            clear_console()  
        if i == 4:
            print(player5)
            chosen = input("Choose card:")
            if chosen == "p": continue
            placed_deck.append(chosen)
            deck_of_cards.remove(chosen)
            player5.remove(chosen)
            clear_console()  
        if i == 5:
            print(player6)
            chosen = input("Choose card:")
            if chosen == "p": continue
            placed_deck.append(chosen)
            deck_of_cards.remove(chosen)
            player6.remove(chosen)
            clear_console()
          
    if player1 == [] or player2 == [] or player3 == [] or player4 == [] or player5 == [] or player6 == []:
        break
    else:
        continue

print("Game Over")

    
