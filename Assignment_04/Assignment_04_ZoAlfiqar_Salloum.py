###########################################
###########################################
####           FCS CYCLE 49            ####
####           Assignment 4            ####
####           Task Manager            ####
###########################################
###########################################




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
        









