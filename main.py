import random


class Game:
    def __init__(self):
        self.players = []

    def number_of_players(self):
        while True:
            names = input("\nTo begin just press ENTER\n-------------------------\nPlayers name: ")
            self.players.append(names)
            if len(names) == 0:
                self.players.pop(-1)
                break
        if len(self.players) == 0:
            exit("At least one player is needed!")
        print(f'There are {len(self.players)} players.')

    def gameplay(self):
        truth = ['How many plants you have?', 'Can you cook?', 'What is your favourite band?']
        dare = ['Jump as high as you can', 'Run around the house', 'Make a snack']
        random.shuffle(truth)
        random.shuffle(dare)
        play = True
        while play:
            for player in self.players:
                if not truth + dare:
                    play = False
                    print("\nIt seems we're out of questions!\nThanks for playing!")
                    break
                choice = input(f"\n{player}, truth or dare? truth/dare ").lower()
                if choice in ['truth' or 't']:
                    if not truth:
                        print("\nWe're out of truth questions")
                        break
                    print(truth.pop(0))

                if choice in ['dare', 'd']:
                    if not dare:
                        print("\nWe're out of dare questions")
                        break
                    print(dare.pop(0))

                continue_q = input("Do you want to continue? yes/no ").lower()
                if continue_q in ['no', 'n']:
                    play = False
                    print("\nThanks for playing!")
                    break


if __name__ == "__main__":
    main = Game()
    main.number_of_players()
    main.gameplay()
