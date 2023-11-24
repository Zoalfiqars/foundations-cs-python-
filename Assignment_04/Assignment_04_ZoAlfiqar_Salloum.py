###########################################
###########################################
####           FCS CYCLE 49            ####
####           Assignment 4            ####
####           Task Manager            ####
###########################################
###########################################

class NewTask:
    def __init__(self, ID, description, priority, completed):
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

    def createId(self):
        temp = self.head
        if temp == None:
            id = 1
            return id
        else:
            id = 0
            while(temp is not None):
                temp = temp.ref
                id += 1
            id += 1
            return id
    
    def enqueue(self, ID, description, priority, completed):
        new_node = NewTask(ID, description, priority, completed)

        if(self.size == 0):
            self.head = new_node
            self.size += 1
            print("Task was successfully saved!")

        else:
            if(new_node.priority > self.head.priority):
                new_node.ref = self.head
                self.head = new_node
                size += 1
                print("Task was successfully saved!")

            else:
                temp = self.head
                prev = temp
                while((temp is not None) and (temp.priority >= new_node.priority)):
                    prev = temp
                    temp = temp.ref
                prev.ref = new_node
                new_node.ref = temp
                self.size += 1

    def dequeue(self):
        if (self.size == 0):
            print("No tasks to be marked as completed!")

        else:
            print("Task",self.head.description,"was marked as completed!")
            temp = self.head
            self.head = self.head.ref
            temp.ref = None
            self.size -= 1
            return temp
                    
        





tasks = PriorityQueue()

def addNewTask():
    description = input("Please enter the task description: ")
    priority = input("Please enter an integer value representing the priority of the task, higher values indicate higher priority: ")
    while not (priority.isnumeric() is True) or (int(priority) > 0 is True):
        priority = input("Invalid input! Please enter an integer value bigger than 0: ")
    id = tasks.createId()

    tasks.enqueue(id, description, priority, completed=False)




def displayMenu():
    print("Welcome to the Task Manager!\n1. Add a new task.\n2. Show a task.\n3. Mark the highest priority task as completed\n4. Display all tasks\n5. Display tasks that are not completed.\n6. Display the last completed task.\n7. Exit")
    choice = input("Please enter your choice's number: ")
    while ((choice != "1") and (choice != "2") and (choice != "3") and (choice != "4") and (choice != "5") and (choice != "6") and (choice != "7")):
        choice = input("Invalid input! Please enter your choice's number: ")
    choice = int(choice)
    return choice

def main():
    choice = displayMenu()

    #Adding a new task to the task manager.
    if choice == 1:
        addNewTask()
        


main()









