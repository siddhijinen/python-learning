from game_data import data
import art
import random

print(art.logo)

new_game = True

while new_game:
    visited_people = []
    player_in_game = True
    personA = random.choice(data)
    visited_people.append(personA['name'])

    score = 0

    while player_in_game:
        personB = random.choice(data)
        while personB['name'] in visited_people:
            personB = random.choice(data)
        visited_people.append(personB['name'])

        print(f"Compare A: {personA['name']}, a {personA['description']}, from {personA['country']}")
        print(art.vs)
        print(f"Against B: {personB['name']}, a {personB['description']}, from {personB['country']}")

        followersA = personA['follower_count']
        followersB = personB['follower_count']

        if followersA > followersB:
            correct_answer = "A"
        else:
            correct_answer = "B"

        print(correct_answer)
        print(visited_people)

        answer = input("Who has more followers? Type 'A' or 'B': ").upper()
        if answer == correct_answer or followersA == followersB:
            score += 1
            if len(visited_people) == len(data):
                print("You've won the game!")
                player_in_game = False
                break
            print("\n" * 100, art.logo)
            print(f"\nYou're right! Current score : {score}")
            personA = personB
            continue
        else:
            print("\n" * 100, art.logo)
            print(f"\nSorry that's wrong. Final score : {score}")
            visited_people = []
            player_in_game = False
    restart_game = input("Do you want to restart? Type 'y' to restart.").lower()
    if not restart_game == "y":
        print("Game Ended.")
        new_game = False
        break