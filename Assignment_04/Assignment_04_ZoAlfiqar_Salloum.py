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
                self.size += 1
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
                print("Task was successfully saved!")

    def dequeue(self):
        if (self.size == 0):
            return -99

        else:
            print("Task",self.head.description,"was marked as completed and moved to history!")
            temp = self.head
            temp.setCompleted(True)
            self.head = self.head.ref
            temp.ref = None
            self.size -= 1
            return temp.ID, temp.description, temp.priority, temp.completed
        

    def displayTasks(self):
        print("Incomplete tasks:")
        if self.size == 0:
            print("No tasks to show!")
        elif self.size == 1:
            print("Task priority:", self.head.priority, "Task description:", self.head.description, ">>>", self.head.completed)
        else:
            temp = self.head
            while(temp is not None):
                print("Task priority:", self.head.priority, "Task description:", self.head.description, ">>>", self.head.completed)
                temp = temp.ref


    def getTaskWithID(self):
        id = input("Please enter the task id: ")
        while (id.isnumeric() != True) or ((int(id) >= 0) != True):
            id = input("Invalid input! Please enter a valid id: ")
        id = int(id)
        temp = self.head
        while temp is not None:
                if temp.getID() == id:
                    return temp.getDescription()
                else:
                    temp = temp.ref
        if temp == None:
            return ("No task was found!")


        



class History:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, ID, description, priority, completed):
        task_completed = NewTask(ID, description, priority, completed)
        task_completed.ref = self.head
        self.head = task_completed
        self.size += 1
        

    def showLastCompletedTask(self):
        if self.size == 0:
            print("No completed tasks!")
        else:
            print("Last completed task:\nTask priority: ", self.head.priority, "\nTask description: ", self.head.description, "\n>>>", "Completed")


    def displayHistory(self):
        print("Completed tasks:")
        temp = self.head
        if self.size == 0:
            print("No Completed tasks to show!")
        elif self.size == 1:
            print("Task priority: ", self.head.priority, ".Task description: ", self.head.description, ">>>", "Completed")
        else:
            temp = self.head
            while(temp is not None):
                print("Task priority: ", self.head.priority, ".Task description: ", self.head.description, ">>>", "Completed")
                temp = temp.ref


        





tasks = PriorityQueue()
completed_tasks = History()

def addNewTask():
    description = input("Please enter the task description: ")
    priority = input("Please enter an integer value representing the priority of the task, higher values indicate higher priority: ")
    while not (priority.isnumeric() is True) or (int(priority) >= 0 == True):
        priority = input("Invalid input! Please enter an integer value bigger than 0: ")
    priority = int(priority)
    id = tasks.createId()

    tasks.enqueue(id, description, priority, completed=False)




def displayMenu():
    print("##############################\n  Welcome to the Task Manager\n##############################\n1. Add a new task.\n2. Show a task.\n3. Mark the highest priority task as completed\n4. Display all tasks\n5. Display tasks that are not completed.\n6. Display the last completed task.\n7. Exit\n--------------------\n")
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

    #Getting a task from the queue given a task id
    if choice == 2:
        print(tasks.getTaskWithID())
        main()

    #Marking the highest priority task as completed and putting it in the task history.
    if choice == 3:
       marked_as_completed = tasks.dequeue()
       if marked_as_completed == -99:
           print("No tasks to be marked as completed!")
       else:
        id = marked_as_completed[0]
        description = marked_as_completed[1]
        priority = marked_as_completed[2]
        completed = marked_as_completed[3]
        completed_tasks.push(id, description, priority, completed)
        main()


    #Displaying all tasks in order of priority.
    if choice == 4:
        tasks.displayTasks()
        completed_tasks.displayHistory()
        main()


    #Displaying only the tasks that are not completed.
    if choice == 5:
        tasks.displayTasks()


    #Displaying the last completed task.
    if choice == 6:
        completed_tasks.showLastCompletedTask()


    if choice == 7:
        print("Thanks for using my task manager.")

main()









