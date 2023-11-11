
###################################################################
###################################################################
###################### FCS Midterm Project ########################
###################### Zo Alfiqar Salloum #########################
############### Advanced Browser Tabs Simulation ##################
################### Friday, November 10, 2023 #####################
###################################################################
###################################################################
import json





###################################################################
###################################################################
##### This function creates a JSON file so we can save data  ######
##### (User's Updates) to it. File's name is (Opened Tabs).  ######
##### I did a long research about JSON to learn how to use it  ####
##### and Here are all the links to all websites that I surfed.  ##
##### Links are not only for this function but for all functions ##
######################## related to JSON.  ########################
##### https://docs.python.org/3/tutorial/inputoutput.html     #####
##### https://docs.python.org/3/library/json.html#module-json  ####
### https://docs.python.org/3/reference/compound_stmts.html#with ##
# https://www.geeksforgeeks.org/append-to-json-file-using-python/ #
########### https://www.youtube.com/watch?v=ttQidKChD4c ########### 
########### https://www.youtube.com/watch?v=a2pYgIuVCxE ###########
########### https://www.youtube.com/watch?v=jABj-SEhtBc ###########
########### https://www.youtube.com/watch?v=QrRcZmDaO_I ###########
###################################################################
###################################################################
#                 ** A VERY IMPORTANT NOTE **                     #
#          Please Comment the Function below after                #
#          you run the software for the first time,               #
#         otherwise the JSON file will be recreated               #
#           again every time you run this software                #
#           and you will lose all your saved data!                #
#   and also comment the function inside the Main() function      #
###################################################################
###################################################################
def createJsonFile():
    tabs_list = [{"Title":"SE Factory", "URL":"https://sefactory.webflow.io/", "nested":[]}]
    json_string = json.dumps(tabs_list)
    with open("opened_tabs.json", "w") as f:
        f.write(json_string)





###################################################################
###################################################################
#### This function takes the new updates as a new JSON file and ###
######## replace it with the older version of the same file #######
###################################################################
###################################################################
def updateJsonFile(new_updates, filename = "opened_tabs.json"):
    with open(filename, "w") as f:
        json.dump(new_updates, f, indent=2)




###################################################################
###################################################################
### This function will load the JSON file, make a temporary copy ##
###### of its data, append the new tab data to the temporary ######
######## copy then return the temporary copy of data to be ########
### replaced later by using another function with the old data ####
### in the JSON file. The function will take three parameters to ##
### make a new tab (New Dictionary) and then add the dictionary ###
############# to the list of dictionaries / tabs. #################
###################################################################
###################################################################
def openNewTab(title, url, nested_list):
    with open("opened_tabs.json") as f:
        data = json.load(f)
        new_tab = {"Title":title,"URL":url, "Nested":[]}
        data.append(new_tab)
        return data




###################################################################
###################################################################
########### This function displays the software menu ##############
###################################################################
###################################################################
def displayMenu():
    print("Welcome to ABTS.\nThe most Advanced Browser Tabs Simulation.\nHere is the Menu, please choose wisely:\n1. Open Tab\n2. Close Tab\n3. Switch Tab\n4. Display All Tabs\n5. Open Nested Tabs\n6. Clear All Tabs\n7. Save Tabs\n8. Import Tabs\n9. Exit ABTS")
    choice = input("Please enter your choice's number: ")
    while (choice != "1") and (choice != "2") and (choice != "3") and (choice != "4") and (choice != "5") and (choice != "6") and (choice != "7") and (choice != "8") and (choice != "9"):
        choice = input("Invalid input! Please enter one of the numbers below: ")
    choice = int(choice)
    return choice




###################################################################
###################################################################
###### This function asks the user to enter a tab's title, ########
########## handles the user's input and return a title ############
###################################################################
###################################################################
def getTitle():
    title = input("Please enter the tab's title: ")
    print("Are you sure that",title,"is the tab's title?\n1. YES\n2. NO")
    confirm = input("Please type 1 or 2: ")
    while (confirm != "1") and (confirm != "2"):
        confirm = input("Invalid input! Please enter 1 or 2: ")
    if confirm == "1":
        return title
    elif confirm == "2":
        return getTitle()





###################################################################
###################################################################
###### This function asks the user to enter the tab's URL, ########
############ handles the user's input and return a URL ############
############################### ## ################################
##  NOTE: I did a research to know how to check if the user's    ##
##  input is a valid URL. I found so many methods and finally    ##
##  chose .startwith() method. Here is the link of the page:    ###
##    https://www.geeksforgeeks.org/python-check-url-string/     ##
###################################################################
###################################################################
def getURL():
    url = input("Please enter a valid URL.\nNote: URL should start with 'http:', 'https:' or 'www.'\nType your URL here: ")
    while (url.startswith("https:") != True) and (url.startswith("http:") != True) and (url.startswith("www.") != True):
        url = input("Invalid URL!\nPlease enter a valid URL.\nNote: URL should start with 'http:', 'https:' or 'www.'\nType your URL here: ")
    print("Are you sure that",url,"is the tab's URL?\n1. YES\n2. NO")
    confirm = input("Please type 1 or 2: ")
    while (confirm != "1") and (confirm != "2"):
        confirm = input("Invalid input! Please enter 1 or 2: ")
    if confirm == "1":
        return url
    elif confirm == "2":
        return getURL()





###################################################################
###################################################################
########## This function asks the user to enter an Index, #########
########## handles the user's input and return the Index ##########
###################################################################
###################################################################
def getIndex():
    index = input("Please enter the index: ")
    while (index.isnumeric() != True) or ((int(index) >= 0) != True):
        index = input("Invalid input! Index should be an integer and > 0.\nPlease enter the index again: ")
    return index





###################################################################
###################################################################
###                This is the Main Function.                   ###
###  it calls all required functions for the software to run    ###
###                        Peacefully                           ###
###################################################################
###################################################################
def main():

    createJsonFile()

    choice = displayMenu()  

    if choice == 1:  #1. Open Tabs
        title = getTitle()
        url = getURL()
        nested_tab = []
        data_updates = openNewTab(title, url, nested_tab)
        updateJsonFile(data_updates)
        print("New tab titled:",title,"\nwith the URL:",url,"\nWas successfully opened!")

    if choice == 2:
        





main()


