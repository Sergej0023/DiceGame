from Displays import Displays
from Game import Game
from Computer import Computer
from HighScore import highscore
from HumanPlayer import HumanPlayer


def main():
    player_name = input("Welcome to Pig! Enter the name of player one: ")
    player_one = HumanPlayer()
    player_one.username = player_name

    highscore()

    while True:
        Displays.print_menu()
        choice = input("Enter your choice (1 to 5): ")

        match choice:
            case "1":
                Displays.print_bot_menu()
                difficulty_level = input("Enter your choice (1 to 4): ")

                if difficulty_level in {"1", "2", "3"}:
                    computer = Computer(difficulty_level)
                    game = Game(player_one, computer)  # starts a game with a username and difficulty lvl
                    game.pig()

                elif difficulty_level == "4":
                    Displays.print_menu()

                else:
                    print("Enter a valid choice")

            case "2":
                player_two_name = input("Enter the name of player two: ")
                player_two = HumanPlayer()
                player_two.username = player_two_name

                game = Game(player_one, player_two)
                game.pig()

            case "3":
                highscore.display_scores()

            case "4":
                Displays.print_player_options()
                option = input("\nEnter your choice (1 to 3): ")

                match option:
                    case "1":
                        pass

                    case "2":
                        new_username = input("What's the new username: ")
                        player_one.username = new_username

            case "5":
                Displays.print_rules()

            case "6":
                break

            case default:
                print("Enter a valid")


if __name__ == '__main__':
    main()
