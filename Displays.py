class Displays:
    @staticmethod
    def print_rules():
        rules = """
        │ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - |
        |                                                 Rules                                                           |
        │ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - | 
        |                                                                                                                 |
        | Each turn, a player repeatedly rolls a die until either a 1 is rolled or the player decides to "hold":          |
        |                                                                                                                 |
        | If the player rolls a 1, they score nothing and it becomes the next player's turn.                              |
        | If the player rolls any other number, it is added to their turn total and the player's turn continues.          |
        | If a player chooses to "hold", their turn total is added to their score, and it becomes the next player's turn. |
        |                                                                                                                 |
        | The first player to score 100 or more points wins.                                                              |
        |                                                                                                                 |
        | (wikipedia reference)                                                                                           |
        |                                                                                                                 |
        │ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - |
            """
        print(rules)


    @staticmethod
    def print_menu():
        main_menu = """
        │ - - - - - - - - - - - - - - - │
        │           Pig Game            │
        │ - - - - - - - - - - - - - - - │
        │ 1. Play versus bot            │
        │ 2. Play with another player   │
        │ 3. Show highscores            |
        | 4. Player options             │
        │ 5. Rules                      │
        │ 6. Quit                       │
        │ - - - - - - - - - - - - - - - │

        """
        print(main_menu)


    @staticmethod
    def print_bot_menu():
        bot_menu = """
        │ - - - - - - - - - - - - - │
        │     Select Difficulty     │
        │ - - - - - - - - - - - - - │
        │ 1. Easy                   │
        │ 2. Medium                 │
        │ 3. Hard                   |
        | 4. Back                   │
        │ - - - - - - - - - - - - - │

        """
        print(bot_menu)


    @staticmethod
    def print_player_options():
        player_menu = '''
        │ - - - - - - - - - - - - - │
        │     Player Options        │
        │ - - - - - - - - - - - - - │
        │ 1. Previous scores        │
        │ 2. Change name            │
        | 3. Back                   │
        │ - - - - - - - - - - - - - │'''
        print(player_menu)


    @staticmethod
    def print_dice(player, dice):
        if dice == 1:
            print(f"{player.username} rolled {dice}, skip turn")
        else:
            print(f"{player.username} rolled {dice}")


    @staticmethod
    def input_another_turn():
        return input("Another turn? ")


    @staticmethod
    def print_score(score, runningScore):
        print(f"Score {score + runningScore}\n")

    @staticmethod
    def print_win(player):
        print(f"{player.username} won.")
