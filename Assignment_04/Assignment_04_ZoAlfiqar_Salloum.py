###########################################
###########################################
####           FCS CYCLE 49            ####
####           Assignment 4            ####
####           Task Manager            ####
###########################################
###########################################

class NewTask:
    def __init__(self, ID, description, priority, completed = False):
        self.ID = ID
        self.description = description
        self.priority = priority
        self.completed = completed
        self.ref = None

    def getID(self):
        return self.ID
    def getDescription(self):
        return self.description
    def getPriority(self):
        return self.priority
    def getCompleted(self):
        return self.completed
    
    def setID(self, new_ID):
        self.ID = new_ID
    def setDescription(self, new_description):
        self.description = new_description
    def setPriority(self, new_priority):
        self.priority = new_priority
    def setCompleted(self, new_completed):
        self.completed = new_completed


class PriorityQueue:
    def __init__(self):
        self.head = None
        self.size = 0
        






def addNewTask():
    description = input("Please enter the task description: ")
    priority = input("Please enter an integer value representing the priority of the task, higher values indicate higher priority: ")




def displayMenu():
    print("Welcome to the Task Manager!\n1. Add a new task.\n2. Show a task.\n3. Mark the highest priority task as completed\n4. Display all tasks\n5. Display tasks that are not completed.\n6. Display the last completed task.\n7. Exit")
    choice = input("Please enter your choice's number: ")
    while ((choice != "1") and (choice != "2") and (choice != "3") and (choice != "4") and (choice != "5") and (choice != "6") and (choice != "7")):
        choice = input("Invalid input! Please enter your choice's number: ")
    return choice

def main():
    choice = displayMenu()

    #Adding a new task to the task manager.
    if choice == 1:
        









