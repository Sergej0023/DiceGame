import Displays

def main():

    Displays.Displays.printMenu()
    choice = input("Enter your choice (1 to 5): ")
    match choice:
        case "1":
            Displays.Displays.printBotMenu()
            difficultyLevel = input("Enter your choice (1 to 3): ")
            # create a new game at this point and pass the choice to game constructor and create new AI there?

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




