######################################
########### Assignment_03 ############
######################################
import math
# You need to simulate student data by creating a list of dictionaries. Each dictionary represents a
# student's information with the following fields:
# • 'ID' (integer): The student's unique identifier.
# • 'Name' (string): The student's name.
# • 'Age' (integer): The student's age.
# • 'Major' (string): The student's major.
# • 'GPA' (float): The student's grade point average.

# Your task is to implement functions that simulate API endpoints for retrieving student
# information. Your program should start by displaying the following menu:

# 1. Get Student by ID
# 2. Get All Students
# 3. Get Students by Major
# 4. Add Student
# 5. Find Common Majors
# 6. Delete Student
# 7. Calculate Average GPA
# 8. Get Top Performers
# 9. Exit
# - - - - - - - - - - - - - - -

# Choice 1: This function takes the student data and a student's ID as arguments and returns the
# information of the student with the given ID.
# Choice 2: This function takes the student data as an argument and returns a list of all students'
# information.
# Choice 3: This function takes the student data and a major as arguments and returns a list of
# students in the specified major.
# Choice 4: This function takes the student data, a name, an age, a major, and a GPA as arguments
# and adds a new student to the data.
# Choice 5 This function takes two student data lists as arguments and returns a set of common
# majors found in both lists.
# Choice 6: This function takes the student data and a student's ID as arguments and removes the
# student with the given ID from the data.
# Choice 7: This function takes the student data as an argument and returns the average GPA of
# all the students in the data.
# Choice 8: This function takes the student data and the number of top-performing students to
# retrieve as arguments. It returns a tuple of the specified number of students with the highest
# GPAs (the tuple should have the name of those students).
# Choice 9: This choice terminates the program.

student_data = [
  {"ID": 1, "Name":"Ali", "Age":21, "Major":"Mathematics", "GPA":3.7}, {"ID":2, "Name":"Ahmad", "Age":21, "Major":"History", "GPA":3.6}, 
  {"ID":3, "Name":"Yara", "Age":20, "Major":"Computer Science", "GPA":3.2}, {"ID":4, "Name":"Eliea", "Age":22, "Major":"Psychology", "GPA":3.8}, 
  {"ID":5, "Name":"Mohamad", "Age":19, "Major":"Engineering", "GPA":3.1}, {"ID":6, "Name":"Hanan", "Age":23, "Major":"English", "GPA":3.9}, 
  {"ID":7, "Name":"Omar", "Age":20, "Major":"Mathematics", "GPA":2.8}, {"ID":8, "Name":"Reem", "Age":23, "Major":"Engineering", "GPA":3.5}, 
  {"ID":9, "Name":"Yazan", "Age":21, "Major":"Psychology", "GPA":3.4}, {"ID":10, "Name":"Ola", "Age":20, "Major":"History", "GPA":2.8},
  {"ID":11, "Name":"Rida", "Age":22, "Major":"Engineering", "GPA":3.3}, {"ID":12, "Name":"Hasan", "Age":22, "Major":"Computer Science", "GPA":3.4},
  {"ID":13, "Name":"Ali", "Age":19, "Major":"Mathematics", "GPA":3.7}, {"ID":14, "Name":"Hasan", "Age":23, "Major":"Psychology", "GPA":3.1},
  {"ID":15, "Name":"Kareem", "Age":20, "Major":"English", "GPA":3.7}, {"ID":16, "Name":"Zoalfiqar", "Age":33, "Major":"Computer Science", "GPA":4}]

student_data02 = [
  {"ID": 1, "Name":"Ali", "Age":21, "Major":"Art", "GPA":3.7}, {"ID":2, "Name":"Ahmad", "Age":21, "Major":"History", "GPA":3.6}, 
  {"ID":3, "Name":"Yara", "Age":20, "Major":"Computer Science", "GPA":3.2}, {"ID":4, "Name":"Eliea", "Age":22, "Major":"Music", "GPA":3.8}, 
  {"ID":5, "Name":"Mohamad", "Age":19, "Major":"Engineering", "GPA":3.1}, {"ID":6, "Name":"Hanan", "Age":23, "Major":"Arabic", "GPA":3.9}, 
  {"ID":7, "Name":"Omar", "Age":20, "Major":"Art", "GPA":2.8}, {"ID":8, "Name":"Reem", "Age":23, "Major":"Engineering", "GPA":3.5}, 
  {"ID":9, "Name":"Yazan", "Age":21, "Major":"Music", "GPA":3.4}, {"ID":10, "Name":"Ola", "Age":20, "Major":"History", "GPA":2.8},
  {"ID":11, "Name":"Rida", "Age":22, "Major":"Engineering", "GPA":3.3}, {"ID":12, "Name":"Hasan", "Age":22, "Major":"Computer Science", "GPA":3.4},
  {"ID":13, "Name":"Ali", "Age":19, "Major":"Art", "GPA":3.7}, {"ID":14, "Name":"Hasan", "Age":23, "Major":"Music", "GPA":3.1},
  {"ID":15, "Name":"Kareem", "Age":20, "Major":"Arabic", "GPA":3.7}, {"ID":16, "Name":"Zoalfiqar", "Age":33, "Major":"Computer Science", "GPA":4}]

new_student = {}

def desMenu():
    print("The Menu:\n1. Get Student by ID\n2. Get All Students\n3. Get Students by Major\n4. Add Student\n5. Find Common Majors\n6. Delete Student\n7. Calculate Average GPA\n8. Get Top Performers\n9. Exit")


def getStudentByID (lst, id_input, index): #Choice 1: This function takes the student data and a student's ID as arguments and returns the information of the student with the given ID.
    if (index > len(lst)-1):
        print("Student was not found.")
        return
    elif lst[index]["ID"] == id_input:
        for i in lst[index]:
           print(i+":", lst[index][i])
        return
    elif lst[index]["ID"] != id_input:
        index += 1
        getStudentByID(lst, id_input, index)
    
def getAllStudents(lst):  # Choice 2: This function takes the student data as an argument and returns a list of all students' information.
   lst_of_lists = []
   for i in lst:
      student_list = []
      for key, value in i.items():
         student_list.append(key)
         student_list.append(value)
      lst_of_lists.append(student_list)
   for i in lst_of_lists:
    print(i)
         

       

def getStudentsByMajor(lst,major):    # Choice 3: This function takes the student data and a major as arguments and returns a list of students in the specified major.
   if major == 1: #Computer Science
      final_lst = []
      for i in lst:
         if i["Major"] == "Computer Science":
            final_lst.append(i)
      print(final_lst)

   if major == 2: #Mathematics
      final_lst = []
      for i in lst:
         if i["Major"] == "Mathematics":
            final_lst.append(i)
      print(final_lst)

   if major == 3: #History
      final_lst = []
      for i in lst:
         if i["Major"] == "History":
            final_lst.append(i)
      print(final_lst)

   if major == 4: #Psychology
      final_lst = []
      for i in lst:
         if i["Major"] == "Psychology":
            final_lst.append(i)
      print(final_lst)

   if major == 5: #Engineering
      final_lst = []
      for i in lst:
         if i["Major"] == "Engineering":
            final_lst.append(i)
      print(final_lst)

   if major == 6: #English
      final_lst = []
      for i in lst:
         if i["Major"] == "English":
            final_lst.append(i)
      print(final_lst)

def getName(new_student_name, confirm):  # Choice 4 (1): This function gets the student's name.
  if confirm == 1:
    new_student["Name"] = new_student_name
    return
  elif confirm == 2:
    new_student_name = input("please enter the student's name again: ")
    print("New student's name is: ",new_student_name)
    confirm = input("Confirm?\n1. Yes\n2. No\ntype the number of your choice: ")
    while not confirm.isnumeric():
      confirm = input("Invalid input, Confirm?\n1. Yes\n2. No\ntype 1 or 2 please!: ")
    confirm = int(confirm)
    getName(new_student_name, confirm)
  else:
    print("Invalid input, please chose 1 or 2!")
    print("New student's name: ",new_student_name)
    confirm = input("Confirm?\n1. Yes\n2. No\ntype 1 or 2 please!: ")
    while not confirm.isnumeric():
      confirm = input("Invalid input, Confirm?\n1. Yes\n2. No\ntype 1 or 2 please!: ")
    x = int(confirm)
    getName(new_student_name, x)

def getAge():  # Choice 4 (2): This function gets the student's Age.
  age = input("Please enter age: ")
  while (age.isnumeric() != True) or ((int(age) >= 18) != True):
    age = input("Error! Age should be a number and over 18: ")
  new_student["Age"] = age

def getMajor():  # Choice 4 (3): This function gets the student's Major.
  maj02 = input("Please chose a Major by entering it's number:\n1. Computer Science\n2. Mathematics\n3. History\n4. Psychology\n5. Engineering\n6. English\ntype a number: ")
  maj_lst02 = [1,2,3,4,5,6]
  while (maj02.isnumeric() != True) or ((int(maj02) in maj_lst02) != True):
    maj02 = input("Invalid Input!\nPlease chose a Major by entering it's number:\n1. Computer Science\n2. Mathematics\n3. History\n4. Psychology\n5. Engineering\n6. English\ntype number: ")
  maj02 = int(maj02)

  if maj02 == 1:
    new_student["Major"] = "Computer Science"

  if maj02 == 2:
    new_student["Major"] = "Mathematics"

  if maj02 == 3:
    new_student["Major"] = "History"

  if maj02 == 4:
    new_student["Major"] = "Psychology"

  if maj02 == 5:
    new_student["Major"] = "Engineering"

  if maj02 == 6:
    new_student["Major"] = "English"

def getGPA():  # Choice 4 (4): This function gets the student's GPA.
  gpa = input("Enter student's GPA: ")
  try:
    float(gpa)
    if 4 >= float(gpa) >= 0 :
      new_student["GPA"] = gpa
    else:
      print("Invalid Input! GPA should be between 0 and 4.")
      getGPA()
    return
  except ValueError:
    print("Invalid Input!")
    getGPA()
    return

common_majors = set()
def getCommonMajors(student_data, student_data02):  #Choice 5: This function takes two student data lists as arguments and returns a set of common majors found in both lists.
  empty_set01 = set()
  empty_set02 = set()
  for i in student_data:
    empty_set01.add(i["Major"])
  for i in student_data02:
    empty_set02.add(i["Major"])
  for i in empty_set01:
    for x in empty_set02:
      if i == x:
        common_majors.add(i)
  return(common_majors)


def removeStudent(student_data, student_id):
   for i in student_data:
      if i["ID"] == student_id:
         print(i, "\nThis student was removed.")
         student_data.remove(i)
      else:
         
         print("Student was not found.")
   print(student_data)


def calculateAverageGPA():
   gpas = []
   for i in student_data:
      gpas.append(i["GPA"])
   list_sum = sum(gpas)
   avr = list_sum / (len(gpas))
   avr = round(avr, 2)
   print("The average GPA is:", avr)



def topPerformers():
   num = input("Please enter the number of the top students you want: ")
   while (num.isnumeric() is not True) or ((int(num) > 0) is not True):
      num = input("Invalid input! Please enter the number of the top students you want: ")
   num = int(num)
   ordered_gpa = sorted(student_data, key=lambda x:x["GPA"], reverse=True)
   top_students = ()
   for i in range(min(num, len(ordered_gpa))):
      top_students += (ordered_gpa[i],)
   return top_students

   



#######################
#### Main Function ####
#######################

def Main():
  desMenu()
  choice = input("Enter your choice's number please: ")
  while (choice.isnumeric() != True) or (int(choice) < 0): 
    choice = input("Invalid choice, Please chose a number out of the list: ")
  choice = int(choice)

  if choice == 1: #1. Get Student by ID
    id = input("Please enter the student's ID to get his/her info: ")
    while (id.isnumeric() != True) or (int(id) < 0):
      id = input("Invalid ID input, please enter a positive integer: ")
    id = int(id)
    getStudentByID(student_data, id, 0)

  if choice == 2: #2. Get All Students
     getAllStudents(student_data)

  if choice == 3: #3. Get Students by Major
     maj = input("Please chose a Major by entering it's number:\n1. Computer Science\n2. Mathematics\n3. History\n4. Psychology\n5. Engineering\n6. English\ntype a number: ")
     maj_lst = [1,2,3,4,5,6]
     while (maj.isnumeric() != True) or ((int(maj) in maj_lst) != True):
        maj = input("Invalid Input!\nPlease chose a Major by entering it's number:\n1. Computer Science\n2. Mathematics\n3. History\n4. Psychology\n5. Engineering\n6. English\ntype number: ")
     maj = int(maj)
     getStudentsByMajor(student_data, maj)   
   
  if choice == 4:  #4. Add Student
     new_student["ID"] = len(student_data)
     new_student_name = input("Enter Full Name Please: ")
     print("New student's name is: ",new_student_name)
     confirm = input("Confirm?\n1. Yes\n2. No\ntype the number of your choice: ")
     while (confirm != "1") and (confirm != "2"):
        confirm = input("Invalid choice!\nConfirm?\n1. Yes\n2. No\ntype the number of your choice: ")
     confirm = int(confirm)
     getName(new_student_name, confirm)
     getAge()
     getMajor()
     getGPA()
     print("The New Student's Info was added:\n", new_student)
     student_data.append(new_student)
     print("New Student List:\n", student_data)

  if choice == 5:  #5. Find Common Majors
     getCommonMajors(student_data, student_data02)
     print(common_majors)

  if choice == 6:  #6. Delete Student
     student_id = input("Please enter the student's ID number: ")
     while (student_id.isnumeric() != True) or (int(student_id) < 0):
      student_id = input("Invalid ID input, please enter a positive integer: ")
     student_id = int(student_id)
     removeStudent(student_data, student_id)

  if choice == 7:  #7. Calculate Average GPA
     calculateAverageGPA()

  if choice == 8:  #8. Get Top Performers
     print(topPerformers())

  if choice == 9:
     print("Thanks for using my software!")
Main()

