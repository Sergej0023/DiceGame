from Displays import Displays
from Game import Game  # needs this otherwise Game class wont work
from Computer import Computer
from Computer import Computer
from HighScore import HighScore
from Difficulty import Difficulty
from Player import Player


def main():
    playerName = input("Welcome to Pig! Enter the name of player one: ") 
    playerOne = Player(playerName)
    HighScore()

    while True:
        Displays.printMenu()
        choice = input("Enter your choice (1 to 5): ")
        match choice:
            case "1":
                Displays.printBotMenu()
                difficultyLevel = input("Enter your choice (1 to 4): ")
                if difficultyLevel in {"1", "2", "3"}:
                    computer = Computer(difficultyLevel)
                    game = Game(playerOne, "", computer, "c")  # starts a game with a username and difficulty lvl
                    game.pig()
                elif difficultyLevel == "4":
                    Displays.printMenu()
                else:
                    print("Enter a valid choice")

            case "2":
                player2Name = input("Enter the name of player two: ")
                playerTwo = Player(player2Name)
                game = Game(playerOne, playerTwo, "", "p")
                game.pig()
            case "3":
                HighScore.displayScores(playerName)
            case "4":
                Displays.printPlayerOptions()
                option = input("\nEnter your choice (1 to 3): ")
                match option:
                    case "1": 
                        pass
                    case "2":
                        newUsername = input("What's the new username: ")
                        playerOne.changeUsername(newUsername)
            case "5":
                Displays.printRules()
            case "6":
                break
            case default:
                print("Enter a valid")


if __name__ == '__main__':
    main()
