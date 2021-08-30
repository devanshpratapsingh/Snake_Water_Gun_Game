import random
di = {"s": "Snake", "w": "Water", "g": "Gun"}


def main ():
    num_of_chances = 1
    human_point = 0
    computer_point = 0
    print("****** Welcome to Game of Snake Water Gun ******")
    print('\nPress "q" to exit the game\n')
    for key, value in di.items():
        print('press "',key,'" for', value)

    while True:
        try:
            chances = int(input("\nHow many times you want to play?: "))

        except ValueError:
            end = input("Enter a valid number. If you want to exit game, press 'q'")
            if end == "q":
                exit()
            continue
        else:
            break
    
    name = input('\nEnter player name: ')

    while num_of_chances <= chances:

        computer = random.choice(list(di.keys()))
        player = input('\nEnter your choice: ').lower()

        if player == "q" or player == "Q":
            exit()
        elif player == "s" or player == "w" or player == "g":

            print('                                             Your choice: ', di[player])
            print('                                             Computer choice: ', di[computer])

            if player == computer:
                print('\n                                               **Draw**')
            elif player == "s" and computer == "g":
                print("\n                                               **Computer wins**")
                computer_point = computer_point + 1
            elif player == "s" and computer == "w":
                print("\n                                               **Player wins**")
                human_point = human_point + 1
            elif player == "w" and computer == "s":
                print("\n                                               **Computer wins**")
                computer_point = computer_point + 1
            elif player == "w" and computer == "g":
                print("\n                                               **Player wins**")
                human_point = human_point + 1
            elif player == "g" and computer == "w":
                print("\n                                               **Computer wins**")
                computer_point = computer_point + 1
            elif player == "g" and computer == "s":
                print("\n                                               **Player wins**")
                human_point = human_point + 1
            print("\nChances left: ", chances - num_of_chances)
            num_of_chances += 1
        else:
            print('Invalid input. Try again')

    print("\n                                                                FINAL RESULT")                  
    print("\n                                                            Computer:",computer_point, name.capitalize(),":", human_point)

    if computer_point > human_point:
        print("\n                                           ************** Computer Wins The Game ***************")
    if computer_point < human_point:
        print("\n                                          ************* ", name.capitalize(), "Wins The Game *****************")
    if computer_point == human_point:
        print("\n                                              *****************The Game Is Draw *****************")
    again = input('Press "y" to play again or press any key to quit: ')
    if again == "y":
        num_of_chances  = 1
    elif again != "y":
        exit()


    main()


main()
