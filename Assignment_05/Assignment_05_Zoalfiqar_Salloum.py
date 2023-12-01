###########################################
###########################################
########   Social Media Platform  #########
###########################################
###########################################























def displayMenu():
    print(">>>>   Welcome to SMP   <<<<")
    print("1. Add new user to the platform.\n2. Remove User from the platform.\n3. Send a friend request.\n4. Remove a friend from your list\n5. View your list of friends.\n6. View the list of users on the platform.\n7. Exit")
    choice = input("Please choose a number: ")
    while (choice != "1") and (choice != "2") and (choice != "3") and (choice != "4") and (choice != "5") and (choice != "6") and (choice != "7"):
        choice = input("Invalid input! Please choose one of the shown numbers: ")
    choice = int(choice)
    return choice

