def main():

    main_menu = """
    │ - - - - - - - - - - - - - - - │
    │           Pig Game            │
    │ - - - - - - - - - - - - - - - │
    │ 1. Play versus bot            │
    │ 2. Play with another player   │
    │ 3. Show highscores            │
    │ 4. Rules                      │
    │ 5. Quit                       │
    │ - - - - - - - - - - - - - - - │

    """
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
    print(main_menu)
    choice = input("Enter your choice (1 to 5): ")
    match choice:
        case "1":
            print(bot_menu)
            difficultyLevel = input("Enter your choice (1 to 3): ")
            # create a new game at this point and pass the choice to game constructor and create new AI there?

        case "2":
            pass
        case "3":
            pass
        case "4":
            pass
        case "5":
            exit()

if __name__ == '__main__':
    main()




