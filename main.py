import Displays
import Game
import Difficulty
import Computer


def askPlayerName():
    return input("Player name: ")

def main():

    Displays.Displays.printMenu()
    choice = input("Enter your choice (1 to 5): ")
    match choice:
        case "1":
            Displays.Displays.printBotMenu()
            difficultyLevel = input("Enter your choice (1 to 4): ")
            if difficultyLevel in {"1", "2", "3"}:               
                playerName = askPlayerName()
                game = Game(playerName) #starts a game with a username and difficulty lvl
                computer = Computer(Difficulty.Difficulty(int(difficultyLevel)).name)
            elif difficultyLevel == "4":
                pass
            else:
                print("Enter a valid choice")

        case "2":
            pass
        case "3":
            pass
        case "4":
            Displays.Displays.printRules()
        case "5":
            exit()

if __name__ == '__main__':
    main()


