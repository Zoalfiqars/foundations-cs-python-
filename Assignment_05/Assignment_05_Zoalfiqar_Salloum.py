###########################################
###########################################
########   Social Media Platform  #########
###########################################
###########################################

class NewUsername:
    def __init__(self, username):
        self.username = username
        self.user_friends = []
        self.ref = None

    def getUsername(self):
        return self.username
    
    def getRef(self):
        return self.ref
    
    def setUsername(self, new_username):
        self.username = new_username
    
    def setRef(self, new_ref):
        self.ref = new_ref


class FriendList:
    def __init__(self):
        self.platform_users = {}
        self.list_of_connections = []
        self.head = None
        self.size = 0

    def addNewUser(self, new_user):
        if new_user not in self.platform_users:
            new_user = NewUsername(new_user)
            self.platform_users[new_user] = len(self.list_of_connections)
            self.list_of_connections.append(new_user.user_friends)
    
        for key in self.platform_users:
            print(new_user.username)
        print(self.list_of_connections)


fl = FriendList()
fl.addNewUser("Ali")
    





















def displayMenu():
    print(">>>>   Welcome to SMP   <<<<")
    print("1. Add new user to the platform.\n2. Remove User from the platform.\n3. Send a friend request.\n4. Remove a friend from your list\n5. View your list of friends.\n6. View the list of users on the platform.\n7. Exit")
    choice = input("Please choose a number: ")
    while (choice != "1") and (choice != "2") and (choice != "3") and (choice != "4") and (choice != "5") and (choice != "6") and (choice != "7"):
        choice = input("Invalid input! Please choose one of the shown numbers: ")
    choice = int(choice)
    return choice

