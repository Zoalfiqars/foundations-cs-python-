###########################################
###########################################
########   Social Media Platform  #########
###########################################
###########################################
import re

platform_users = {}

class Node:
    def __init__(self, username):
        self.username = username
        self.ref = None

    def getUsername(self):
        return self.username
    def getRef(self):
        return self.ref
     


class UserLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0


    def checkIfFriendExists(self, new_friend):
         if self.size == 0:
              return new_friend
         else:
              temp = self.head
              while not (temp == None):
                   if temp.username == new_friend:
                        return -99
                   else:
                        temp = temp.ref
              return new_friend
                


    def addNewFriendship(self, new_friend):
        new_friend = self.checkIfFriendExists()
        if new_friend == -99:
            print("You already have this person in your friend list!")
        else:
            new_friend = Node(new_friend)
            new_friend.ref = self.head
            self.head = new_friend
            self.size += 1
          


class AdjacencyList:
     def __init__(self):
          self.graph = []

     def addNewLinkedList(self, new_linked_list):
          self.graph.append(new_linked_list)

     def addNewEdge(self,index,username):
          self.graph[index].append(UserLinkedList.addNewFriendship(username))
          









# This function gets the new username from the user as an input, validates it, checks if the it already exists in the platform
# then if it is new, it adds the new username to the dictionary and gives it a value.
# The value will be used later on as the index of the linked list that saves the user's connections (Friends)
def addNewUserToPlatform():
    username = input("Username should be 8 to 25 characters long, and can only contain these characters (_ . %).\nPlease enter a unique user name: ")
    pattern = r'^[a-zA-Z0-9_.%]+$'
    while not ( (re.match(pattern,username) is True) or ((8 <= len(username) <= 25) is True) ):
        username = input("Invalid username!\nNote: Username should be between 8 and 25 characters and can only contain these characters (_ .).\nPlease enter a unique user name: ")
    while (username in platform_users):
            print(">>> Error: Username already used! please try a different one.")
            return addNewUserToPlatform()
    platform_users[username] = len(platform_users)
    print(f"'{username}' was successfully added to the platform!")
    print(platform_users)



# This function takes a username from the user as an input and checks if it is in the database (dictionary),
# then it removes the user but before that it changes the values of the dictionary if it is bigger than the value of the deleted user
def removeUserFromPlatform():
    username = input("Please enter the username you want to remove: ")
    while not ((8 <= len(username) <= 25) is True):
        username = input("Invalid username!\nNote: Username should be between 8 and 25 characters.\nPlease try again: ")
    while not (username in platform_users):
            print(">>> Error: Username was not found! please try a different one.")
            return removeUserFromPlatform()
    temp = platform_users[username]
    del platform_users[username]
    print(f"'{username}' was successfully removed from the platform!")
    for key,value in platform_users.items():
         if value > temp:
              platform_users[key] = value - 1
    print(platform_users)





def checkIfUserInPlatform(username_num):
    if username_num == 1:
        username_01 = input("Please enter the first username: ")
        while not ((8 <= len(username_01) <= 25) is True):
            username_01 = input("Invalid username!\nNote: Username should be between 8 and 25 characters.\nPlease try again: ")
        while not (username_01 in platform_users):
                print(">>> Error: Username was not found! please try a different one.")
                return checkIfUserInPlatform(1)
        return username_01
    elif username_num == 2:
        username_02 = input("Please enter the second username: ")
        while not ((8 <= len(username_02) <= 25) is True):
            username_02 = input("Invalid username!\nNote: Username should be between 8 and 25 characters.\nPlease try again: ")
        while not (username_02 in platform_users):
            print(">>> Error: Username was not found! please try a different one.")
            return checkIfUserInPlatform(2)
        return username_02





def getUserValue(username):
     for key, value in platform_users.items():
          if key == username:
               return value







# This function shows all the users that are registered at the platform.
def viewPlatformUsers():
     if len(platform_users) == 0:
          print("-----------------------------")
          print("No users to show, the platform is empty!")
          print("-----------------------------")
     else:
          num = 1
          print("-----------------------------")
          print("Users of the platforms are:")
          for key in platform_users:
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



def main():
    platform_linked_lists = AdjacencyList()

    choice = displayMenu()

    if choice == 1:
        username = addNewUserToPlatform()
        new_linked_list = UserLinkedList()
        platform_linked_lists.addNewLinkedList(new_linked_list)
        main()
        


    if choice == 2:
         removeUserFromPlatform()


    if choice == 3:
         user_01 = checkIfUserInPlatform(1)
         user_02 = checkIfUserInPlatform(2)
         while(user_01 == user_02):
              print("You can't send a request from a username to itself!\nPlease try again!")
              user_01 = checkIfUserInPlatform(1)
              user_02 = checkIfUserInPlatform(2)
         user01_index = getUserValue(user_01)
         user02_index = getUserValue(user_02)

         platform_linked_lists.addNewEdge(user01_index,user_01)
         platform_linked_lists.addNewEdge(user02_index,user_02)








    if choice == 6:
         viewPlatformUsers()
         main()


    if choice == 7:
        print("Thank you for using my software!")

main()
