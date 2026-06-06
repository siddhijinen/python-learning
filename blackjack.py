import random

logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def check_for_ace(hand):
    if 11 in hand:
        hand[hand.index(11)] = 1
        return True
    return False

def condition_check(comp, human):
    if sum(human) > 21:
        ace_present = check_for_ace(human)
        if ace_present:
            return condition_check(comp = comp, human = human)
        else:
            print(f"\nYour cards: {human}, current score: {sum(human)} ")
            print("You lost!\n")
            return True
    elif sum(comp) > 21:
        ace_present = check_for_ace(comp)
        if ace_present:
            return condition_check(comp = comp, human = human)
        else:
            print(f"\nYour cards: {human}, current score: {sum(human)} ")
            print(f"Computer's cards: {comp}, current score: {sum(comp)} ")
            print("You win!\n")
        return True
    elif sum(comp) == 21:
        if sum(human) == 21:
            print(f"\nYour cards: {human}, final score: {sum(human)} ")
            print(f"Computer's cards: {comp}, final score: {sum(comp)} ")
            print("It's a tie!\n")
            return True
        else:
            print(f"\nComputer's Blackjack: {comp}, final score: {sum(comp)}!")
            print("You lost!\n")
            return True
    elif sum(human) == 21:
        print(f"\nYour Blackjack: {human}, final score: {sum(human)}!!")
        print(f"Computer's cards: {comp}, final score: {sum(comp)} ")
        print("You win!\n")
        return True
    else:
        return False

play_game = True

while play_game:
    user_play = input("Do you want to play a game of blackjack? Type 'y' to play: ")
    if not user_play == "y":
        play_game = False
        print("Game Ended.")
    else:
        my_cards = []
        computers_cards = []
        print("\n"*100)
        print(logo)
    #Round 1
        my_cards.append(random.choice(cards))
        computers_cards.append(random.choice(cards))

        #Round 2
        my_cards.append(random.choice(cards))
        computers_cards.append(random.choice(cards))

        if sum(computers_cards) >= 21 or sum(my_cards) >= 21:
            condition_check(comp= computers_cards, human= my_cards)
            continue
        else:
            print(f"Your cards: {my_cards}, current score: {sum(my_cards)} ")
            print(f"Computer's first card: {computers_cards[0]}")
            while sum(computers_cards) < 21 and sum(my_cards) < 21:
                draw_card = input("\nType 'y' to get another card, type 'n' to pass: ")
                if draw_card == "y":
                    my_cards.append(random.choice(cards))
                    if condition_check(comp = computers_cards, human= my_cards):
                        break
                    else:
                        print(f"Your cards: {my_cards}, current score: {sum(my_cards)} ")
                        print(f"Computer's first card: {computers_cards[0]}")
                elif draw_card == "n":
                    break
                else:
                    print("Invalid input. Game ended.")
            if sum(my_cards) < 21:
                while sum(computers_cards) < 17:
                    computers_cards.append(random.choice(cards))

                if condition_check(comp = computers_cards, human= my_cards):
                    continue
                elif sum(my_cards) <= 21 and sum(computers_cards) <= 21:
                    my_total = sum(my_cards)
                    computers_total = sum(computers_cards)
                    if my_total > computers_total:
                        print("\nYou won!\n")
                    elif my_total < computers_total:
                        print("\nYou lost!\n")
                    else:
                        print("\nIt's a tie!\n")
                    print(f"Your final cards: {my_cards}, final score: {sum(my_cards)} ")
                    print(f"Computer's final cards: {computers_cards}, final score: {sum(computers_cards)} \n\n")
                    continue
    continue