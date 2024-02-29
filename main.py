import Displays
import Game
import Difficulty

def main():

    Displays.Displays.printMenu()
    choice = input("Enter your choice (1 to 5): ")
    match choice:
        case "1":
            Displays.Displays.printBotMenu()
            difficultyLevel = input("Enter your choice (1 to 4): ")


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

def verifyDifficultyLvl(difficultyLevel):
    if (difficultyLevel == "1" or difficultyLevel == "2" or difficultyLevel == "3"):
        if difficultyLevel in Difficulty:
            playerName = askPlayerName()
            game = Game(playerName, Difficulty.Difficulty(difficultyLevel).name)

def askPlayerName():
    return input("Player name: ")


