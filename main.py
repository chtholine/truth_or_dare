import random

if __name__ == "__main__":

    class Game:
        def __init__(self):
            self.players = []

        def number_of_players(self):
            while True:
                i = input("\nTo begin just press ENTER\n-------------------------\nPlayers name: ")
                self.players.append(i)
                if len(i) == 0:
                    self.players.pop(-1)
                    break
            print(f'There are {len(self.players)} players.')

        def gameplay(self):
            truth = ['How many plants you have?', 'Can you cook?', 'What is your favourite band?']
            dare = ['Jump as high as you can', 'Run around the house', 'Make a snack']
            random.shuffle(truth)
            random.shuffle(dare)

            play = True
            while play:
                for player in self.players:
                    # if lists are empty: stop
                    if not truth + dare:
                        play = False
                        print("\nIt seems we're out of questions!\nThanks for playing!")
                        break

                    q1 = input(f"\n{player}, truth or dare? truth/dare ").lower()
                    if q1 == "truth":
                        if not truth:
                            print("\nWe're out of truth questions")
                            break
                        print(truth.pop(0))

                    if q1 == "dare":
                        if not dare:
                            print("\nWe're out of dare questions")
                            break
                        print(dare.pop(0))

                    q2 = input("Do you want to continue? yes/no ")
                    if q2 == 'no':
                        play = False
                        print("\nThanks for playing!")
                        break

    my_game = Game()
    my_game.number_of_players()
    my_game.gameplay()
