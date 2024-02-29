import Displays
import Game
import Difficulty
import Computer
import HighScore



def main():

    playerName = input("Welcome to Pig! Enter the name of player one: ") #if we want to show highscores for a player, we need the name before the menu?
    HighScore.HighScore()

    Displays.Displays.printMenu()
    while True:
        choice = input("Enter your choice (1 to 5): ")
        match choice:
            case "1":
                Displays.Displays.printBotMenu()
                difficultyLevel = input("Enter your choice (1 to 4): ")
                if difficultyLevel in {"1", "2", "3"}:               
                    game = Game(playerName) #starts a game with a username and difficulty lvl
                    computer = Computer(Difficulty.Difficulty(int(difficultyLevel)).name)
                elif difficultyLevel == "4":
                    Displays.Displays.printMenu()
                else:
                    print("Enter a valid choice")

            case "2":
                player2Name = input("Enter the name of player two: ")
            case "3":
                HighScore.HighScore.displayScores(playerName)
            case "4":
                Displays.Displays.printRules()
            case "5":
                False

if __name__ == '__main__':
    main()


