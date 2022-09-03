import random

players = []
truth = ['How many plants you have?', 'Can you cook?', 'What is your favourite band?']
dare = ['Jump as high as you can', 'Run around the house', 'Make a snack']
random.shuffle(truth)
random.shuffle(dare)


def number_of_players():
    choice = True
    while True:
        i = input("\nTo begin just press ENTER\n-------------------------\nPlayers name: ")
        players.append(i)
        if len(i) == 0:
            players.pop(-1)
            break
    print(f'There are {len(players)} players.')


def game():
    play = True
    while play:
        for player in players:
            # if lists are empty: stop
            if not truth + dare:
                play = False
                print("\nIt seems we're out of questions!\nThanks for playing!")
                break

            q1 = input(f"\n{player}, truth or dare? truth/dare ").lower()
            if q1 == "truth":
                print(truth.pop(0))
                if not truth:
                    print("\nWe're out of truth questions")

            if q1 == "dare":
                print(dare.pop(0))
                if not dare:
                    print("\nWe're out of dare questions")



            q2 = input("Do you want to continue? yes/no ")
            if q2 == 'no':
                play = False
                print("\nThanks for playing!")
                break


number_of_players()
game()