###########################################
###########################################
########   Social Media Platform  #########
###########################################
###########################################
import re

# We are going to make a class to generate nodes, these nodes are going to store names, the names are the friends of a user.
# The user is not going to have a node, nodes are only used to store his\her friends names.
# When someone uses our software and adds a new user to the platform, this user has no friends yet, so he/she has no linked list.
# The newly added user is gonna be stored in a dictionary, key(Name of the newly registered user) and vale(incremented index)
# After the user registers at our platform he/she is gonna start adding friends, each time he/she adds a friend, a new node will be generated and the friend's name will be stored inside of it

# Let's say 'Nanami' added two friends: 1. (Itadori), 2. (Gojo)
# Now 'Nanami' is stored in a dictionary like this: {"Nanami":0}
# And his friends are stored in two separated nodes inside of a linked list like this: [node1 >> "Itadori", node2>> "Gojo"]
# Let's say 'Ali' added two friends: 1. (Hiba), 2. (Mary)
# Now 'Ali' is stored in the dictionary like this: {"Nanami":0, "Ali":1}
# And his friends are stored in two separated nodes inside of a new linked list like this: [node1 >> "Hiba", node2 >> "Mary"]

# Now we have two different linked lists, for two different people, so where are we gonna store these linked lists?!
# We are going to make a list[], and whenever a person starts adding friends, we are going to make a linked list for him/her and append it to the big list.
# The big list is gonna be something like this:
# list_of_linked_lists: [ [node1 >> "Itadori", node2>> "Gojo"], [node1 >> "Hiba", node2 >> "Mary"] ]

# do you see now why we need to use an index for the user?
# Because if someone asked us to print "Nanami's friend list" which is a linked list inside of a big list, how are we gonna know at what index is his linked list?!!!!!!
# well, his linked list is gonna be at the value stored to his key location: {"Nanami":0} >> 0 is the index of the linked list.

# Each linked list is gonna present the connections of the user(friends, if you have any O_O)
# So -as you see- we need another class to make the list of the linked lists and this is gonna be 'the AdjacencyList' class.
# we will start with the class 'Node'

class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None    # This is called self.__next in the course but I like to use 'ref'

    # We don't need getters or setters for the data, as the data is the friend name and we are not going to change the name(No Editing)
    # We only need getters and setters for the reference 'self.ref'
    def getRef(self):
        return self.ref
    def setRef(self, new_ref):
        self.ref = new_ref



# Now, as Eminem once said: "Let's get down to business..."
# Here we are going to start implementing the LinkedList class :)
# So when someone sends a friend request, our code is gonna generate a link list for his/her connections.
class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0


    # When a user adds a friend, this function will add a new node with the friend's name stored in it to the user's linked list
    def addNewFriend(self, new_friend_name):
        new_friend = Node(new_friend_name)
        if (self.size == 0):
            self.head == new_friend
            self.size += 1
        else:
            new_friend.ref = self.head
            self.head = new_friend
            self.size += 1


    # When a user no more wants to be a friend with someone, this function will delete the node that holds the friend's name from the user's linked list
    def removeFriend(self, friend_name):
        if (self.size == 0):
            print(f"'{friend_name}' is not in the friend list!")
        elif (self.size == 1):
            if friend_name == self.head.data:
                self.head = None
                self.size -= 1
            else:
                print(f"'{friend_name}' is not in the friend list!")
        else:
            current = self.head
            previous = current

            while not (current.ref == None):
                if (friend_name != current.data):
                    previous = current
                    current = current.ref
                else:
                    previous.ref = current.ref
                    current.ref = None
                    self.size -= 1


    # This function will traverse over the user's linked list and print his/her friends name.               
    def showFriendsList(self, username):
        if (self.size == 0):
            print(f"'{username}' has no friends!")
        else:
            print(f"{username} friends list:")
            temp = self.head
            num = 1
            while not (temp.ref == None):
                print(f"{num}. {temp.data}")
                temp = temp.ref
                num += 1
            print(f"{num}. {temp.data}")







# Now we need a class to control the linked lists that were made when people were adding friends
class AdjacencyList:
    def __init__(self):
        self.platform_users = {}  # This is the dictionary that will store the users registered to the platform with indices for each user's linked list
        self.graph = [] # This is the list_of_linked_lists



    # This function will take the user input as a name, validate it then it will add the name to the dictionary as a key and give it a value.
    def addNewUserToThePlatform(self):
        new_user = input("Username should be 8 to 25 characters long, and can only contain these characters (_ . %).\nPlease enter a unique user name: ")
        pattern = r'^[a-zA-Z0-9_.%]+$'
        while not ( (re.match(pattern,new_user) is True) or ((8 <= len(new_user) <= 25) is True) ):
            new_user = input("Invalid username!\nNote: Username should be between 8 and 25 characters and can only contain these characters (_ .).\nPlease enter a unique user name: ")
        while (new_user in self.platform_users):
                print(">>> Error: Username already used! please try a different one.")
                return self.addNewUserToThePlatform()
        self.platform_users[new_user] = len(self.platform_users)
        print(f"'{new_user}' was successfully added to the platform!")
        print(self.platform_users)




    # This function will take user input, validate it, then it will delete it from the dictionary.
    def removeUserFromPlatform(self):
        print(self.platform_users)
        user_to_be_removed = input("Please enter the username you want to remove: ")
        while not (8 <= len(user_to_be_removed) <= 25):
            user_to_be_removed = input("Invalid username!\nNote: Username should be between 8 and 25 characters.\nPlease try again: ")
        while (user_to_be_removed not in self.platform_users):
                print(">>> Error: Username was not found! please try a different one.")
                return self.removeUserFromPlatform()
        temp = self.platform_users[user_to_be_removed]
        del self.platform_users[user_to_be_removed]
        print(f"'{user_to_be_removed}' was successfully removed from the platform!")
        for key,value in self.platform_users.items():
            if value > temp:
                self.platform_users[key] = value - 1
        print(self.platform_users)




    
    def checkIfUserInPlatform(self):
        user_name = input("Please enter the username: ")
        while not (8 <= len(user_name) <= 25):
            user_name = input("Invalid username!\nNote: Username should be between 8 and 25 characters.\nPlease try again: ")
        while not (user_name in self.platform_users):
                print(">>> Error: Username was not found! please try a different one.")
                return self.checkIfUserInPlatform()
        return user_name




    def getUserLinkedListIndex(self, user_name):
        for key, value in self.platform_users.items():
            if key == user_name:
                print(f"User '{user_name}' was found")
                return value





    def addConnection(self, linked_list_index, user_name_to_be_added):
        if (linked_list_index >= len(self.graph)):
            new_linked_list = LinkedList()
            new_linked_list.addNewFriend(user_name_to_be_added)
            self.graph.append(new_linked_list)
            
        if (0 <= linked_list_index < len(self.graph)):
            self.graph[linked_list_index].addNewFriend(user_name_to_be_added)




    def removeConnection(self, linked_list_index, user_name_to_be_removed):
        self.graph[linked_list_index].removeFriend(user_name_to_be_removed)
        print(f"'{user_name_to_be_removed}' was successfully removed from the friends list")




# Here we want to check if the user has a linked list or not to avoid getting an error
# if someone wanted to view the friends of a user giving an index but this user has no linked list
# then the index will be out of range.
    def checkIfIndexIsInGraph(self, index):
        if (0 <= index < len(self.graph)):
            return index
        else:
            return -99





    # This function shows all the users that are registered at the platform.
    def viewPlatformUsers(self):
        if len(self.platform_users) == 0:
            print("-----------------------------")
            print("No users to show, the platform is empty!")
            print("-----------------------------")
        else:
            num = 1
            print("-----------------------------")
            print("Users of the platforms are:")
            for key in self.platform_users:
                    print(f"{num}. {key}")
                    num += 1
            print("-----------------------------")












def displayMenu():
    print(">>>>   Welcome to SMP   <<<<")
    print("1. Add new user to the platform.\n2. Remove User from the platform.\n3. Send a friend request.\n4. Remove a friend from your list\n5. View your list of friends.\n6. View the list of users on the platform.\n7. Exit")
    choice = input("Please choose a number: ")
    while (choice != "1") and (choice != "2") and (choice != "3") and (choice != "4") and (choice != "5") and (choice != "6") and (choice != "7"):
        choice = input("Invalid input! Please choose one of the shown numbers: ")
    choice = int(choice)
    return choice


platform_graph = AdjacencyList()

def main():
    choice = displayMenu()

    if choice == 1:  
        platform_graph.addNewUserToThePlatform()
        print("--------------")
        main()
        
    if choice == 2:
        platform_graph.removeUserFromPlatform()
        print("--------------")
        main()


    if choice == 3:
        user_name_01 = platform_graph.checkIfUserInPlatform()
        user_name_02 = platform_graph.checkIfUserInPlatform()

        user_01_index = platform_graph.getUserLinkedListIndex(user_name_01)
        user_02_index = platform_graph.getUserLinkedListIndex(user_name_02)

        platform_graph.addConnection(user_01_index, user_name_02)
        platform_graph.addConnection(user_02_index, user_name_01)
        print(f"'{user_name_01}' and '{user_name_02}' are now friends!")
        print("--------------")
        main()


    if choice == 4:
        user_name_01 = platform_graph.checkIfUserInPlatform()
        user_name_02 = platform_graph.checkIfUserInPlatform()

        user_01_index = platform_graph.getUserLinkedListIndex(user_name_01)
        print(user_01_index)
        user_02_index = platform_graph.getUserLinkedListIndex(user_name_02)
        print(user_02_index)

        platform_graph.removeConnection(user_01_index, user_name_02)
        platform_graph.removeConnection(user_02_index, user_name_01)

        print("--------------")
        main()

    if choice == 5:
        user_name = platform_graph.checkIfUserInPlatform()
        user_index = platform_graph.getUserLinkedListIndex(user_name)
        check_status = platform_graph.checkIfIndexIsInGraph(user_index)
        if check_status == -99:
            print(f"'{user_name}' has no friends!")
        else:
            platform_graph.graph[user_index].showFriendsList(user_name)

        print("--------------")    
        main()

    if choice == 6:
        platform_graph.viewPlatformUsers()
        print("--------------")
        main()


    if choice == 7:
        print("Thank you for using my software!")

main()