
###################################################################
###################################################################
############           FCS Midterm Project           ##############
############           Zo Alfiqar Salloum           ###############
#######          Advanced Browser Tabs Simulation           #######
#######          Friday, November 10/11/12, 2023              #####
###################################################################
###################################################################
import json
from bs4 import BeautifulSoup
import requests
import validators



# 1
###################################################################
###################################################################
########### This function displays the software menu ##############
###################################################################
###################################################################
def displayMenu():
    print("###################################################################\n###################################################################")
    print("###\t\t\tWelcome to ABTS!\t\t\t###")
    print("###################################################################\n###################################################################")
    print("The most Advanced Browser Tabs Simulation.\nHere is the Menu, please choose wisely:\n1. Open Tab\n2. Close Tab\n3. Switch Tab\n4. Display All Tabs\n5. Open Nested Tabs\n6. Clear All Tabs\n7. Save Tabs\n8. Import Tabs\n9. Exit ABTS")
    choice = input("Please enter your choice's number: ")
    while (choice != "1") and (choice != "2") and (choice != "3") and (choice != "4") and (choice != "5") and (choice != "6") and (choice != "7") and (choice != "8") and (choice != "9"):
        choice = input("Invalid input! Please enter one of the numbers shown: ")
    choice = int(choice)
    return choice




# 2
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




# 3
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
##  NOTE: I faced some errors with the URL input so extended my   ##
### research and found a library in python to validate a URL.   ###
###      https://snyk.io/blog/secure-python-url-validation/     ###
###################################################################
###################################################################
def getURL():
    url = input("Please enter a valid URL.\nNote: URL should start with 'http://', 'https://'.'\nType your URL here: ")
    validation = validators.url(url)
    while not validation:
        url = input("Please enter a valid URL.\nNote: URL should start with 'http://', 'https://'.'\nType your URL here: ")
    print("Are you sure that",url,"is the tab's URL?\n1. YES\n2. NO")
    confirm = input("Please type 1 or 2: ")
    while (confirm != "1") and (confirm != "2"):
        confirm = input("Invalid input! Please enter 1 or 2: ")
    if confirm == "1":
        return url
    elif confirm == "2":
        return getURL()




# 4
###################################################################
###################################################################
########## This function asks the user to enter an Index, #########
########## handles the user's input and return the Index ##########
###                 If no index is provided,                    ###
###         the function will return (-1) as a value            ###
###################################################################
###################################################################
def getIndex():
    with open("opened_tabs.json") as f:
        data = json.load(f)

    index = input("Please enter the index: ")
    if (index == ""):
        index = -1
        return index

    if (index.isnumeric() != True) or ((int(index) >= 0) != True):
        print("Invalid input! please try again")
        return getIndex()

    if (int(index) >= len(data)):
        print("Input is out of range!\nInput should be <",len(data))
        return getIndex()

    else:
        index = int(index)
        return index




# 5
###################################################################
###################################################################
####    This function will get the file path from the user     ####
###   in order to be used later on to save the current state of  ##
###                          the software                       ###
###################################################################
###################################################################
def getPath():
    print("file path should be something like this.\n>>> (C:\\Users\\'your pc name'\\Desktop\\01.json) <<<")
    file_path = input("Please enter a file path : ")
    while ((".json" in file_path) == False):
        print(">>> Invalid Input! file path should end with /.json / <<<")
        file_path = input("Please try again: ")
    print("Are you sure this is the correct file path?!\n"+">>> "+file_path+" <<<")
    print("1. YES\n2. NO")
    choice = input("Confirm: ")
    if choice == "1":
        return file_path
    elif choice == "2":
        return getPath()
    else:
        print(">>> Invalid Input! <<<")
        return getPath()



# 6
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
    tabs_list = [{"Title":"SE Factory", "URL":"https://sefactory.webflow.io/", "nested":[]}, {"Title":"Google", "URL":"https://google.com/", "nested":[{"Title":"Google02", "URL":"https://google.com/"},{"Title":"Google03", "URL":"https://google.com/"}]}]
    json_string = json.dumps(tabs_list, indent=4)
    with open("opened_tabs.json", "w") as f:
        f.write(json_string)




# 7
###################################################################
###################################################################
#### This function takes the new updates as a new JSON file and ###
######## replace it with the older version of the same file #######
###################################################################
###################################################################
def updateJsonFile(new_updates, filename = "opened_tabs.json"):
    with open(filename, "w") as f:
        json.dump(new_updates, f, indent=2)





# 8
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




# 9
###################################################################
###################################################################
########### This function will close the tab with the #############
#####            index that the user has chosen              ######
###          (Delete the dictionary from the list)              ###
###################################################################
###################################################################
def closeChosenTab(index):
    if index == "":
        with open("opened_tabs.json") as f:
            data = json.load(f)
            data.remove(data[-1])
            return data
    else:
        with open("opened_tabs.json") as f:
            data = json.load(f)
            data.remove(data[index])
            return data




# 10
##################################################################################################
##################################################################################################
###       This function will get the index from the user and send a request to the website     ###
###                   to get the HTML of the page and display it as an output                  ###
##################################################################################################
###                                           NOTE                                             ###
#####                           If no index were entered, index = -1.                        #####
##################################################################################################
###       These are the links of the websites I checked to learn about web scraping.           ###
###                         https://en.wikipedia.org/wiki/Web_scraping                         ###
###            https://www.geeksforgeeks.org/what-is-web-scraping-and-how-to-use-it/           ###
###                         https://www.youtube.com/watch?v=bargNl2WeN4                        ###
### https://stackoverflow.com/questions/73370965/import-bs4-could-not-be-resolved-from-source  ###
###         https://scrapeops.io/python-web-scraping-playbook/installing-beautifulsoup/        ### 
##################################################################################################
##################################################################################################
def displayTabContent(index):
    with open("opened_tabs.json") as f:
            data = json.load(f)
            url = data[index]["URL"]
            page = requests.get(url)
            html_soup = BeautifulSoup(page.text, "html.parser")
            print(html_soup.prettify()) 



# 11
###################################################################
###################################################################
###      This function will get the titles of the parents       ###
###            and the nested tabs and display them             ###
###################################################################
###################################################################
def printAllTitles():
    with open("opened_tabs.json", "r") as f:
        data = json.load(f)
        for i in data:
            print(i["Title"])
            for nested_tabs in i["nested"]:
                print("   Nested tab >>> "+nested_tabs["Title"])
            print("-----------")




# 12
###################################################################
###################################################################
###      This function will use an index, title and url that    ###
###    were entered by the user then make a new dictionary and  ###
###    append it to the list inside of the dictionary with the  ###
###                       provided index.                       ###
###################################################################
###################################################################
def addNestedTab(index,title,url):
    nested_tab = {"Title":title, "URL":url}
    with open("opened_tabs.json","r") as f:
        data = json.load(f)
        data[index]["nested"].append(nested_tab)
    return data




# 13
###################################################################
###################################################################
###        This function will close all opened tabs             ###
###################################################################
###################################################################
def closeAllTabs():
    with open("opened_tabs.json","r") as f:
        data = json.load(f)
        data.clear()
        return data



        
# 14
###################################################################
###################################################################
###     This function takes a file path as a parameter and      ###
###   saves the current state of the opened tabs to that file   ###
###################################################################
###################################################################
def saveCurrentState(file_path):
    with open("opened_tabs.json","r") as f:
        data = json.load(f)
        with open(file_path, "w") as f:
            json.dump(data, f, indent=4)




# 15
#########################################################################################################
#########################################################################################################
###              This function takes a file path as a parameter and imports a JSON file.              ###
###    This function also checks if the imported file is JSON and if it contains a list, otherwise    ###
###                                      it returns an error.                                         ###     
########################################       Used Links        ########################################
###                    https://www.geeksforgeeks.org/read-json-file-using-python/                     ###
### https://stackoverflow.com/questions/55599336/python-handling-exceptions-while-reading-json-files  ###
###                   https://www.geeksforgeeks.org/json-parsing-errors-in-python/                    ###
###                      https://www.geeksforgeeks.org/python-isinstance-method/                      ###
#########################################################################################################
#########################################################################################################
def importJsonFile(file_path):
    try:
        with open(file_path) as f:
            data = json.load(f)
        if isinstance(data, list):
            return data
        else:
            raise ValueError("File doesn't have a List")
    except FileNotFoundError as x:
        print(f"File not found: {x}")
    except json.JSONDecodeError:
        print("Invalid JSON format in the file")
    except ValueError as x:
        print(f"Invalid data in the file: {x}")
    return 





# 16
#####################################################################
#####################################################################
###     This function takes a user's list as a parameter and      ###
###   imports the list from our JSON file, then merges them both  ###
###     in one list and returns it to be uploaded later on with   ###
###                      another function                         ###
#####################################################################
#####################################################################
def mergeLists(imported_list):
    with open("opened_tabs.json","r") as f:
        data = json.load(f)
        for i in imported_list:
            data.append(i)
        return data




# 17
###################################################################
###################################################################
###              This function asks the user if                 ###
###         he/she wants to go back to menu or exit             ###
###################################################################
###################################################################
def backToMenu():
    print("------------")
    user_input = input("1. Back\n2. Exit\nConfirm: ")
    while (user_input != "1") and (user_input != "2"):
        user_input = input("1. Back\n2. Exit\nConfirm: ")
    if user_input == "1":
        main()
    elif user_input == "2":
        print("###################################################################\n###################################################################")
        print("\t>>> Thank You Mr. Georgio for Using ABTS <<<")
        print("###################################################################\n###################################################################")





# 18
###################################################################
###################################################################
###                This is the Main Function.                   ###
###  it calls all required functions for the software to run    ###
###                        Peacefully                           ###
###################################################################
###################################################################
def main():

    createJsonFile()  #NOTE: Please comment this function after the first time you run the software!

    choice = displayMenu()  

    if choice == 1:  #1. Open Tabs
        title = getTitle()
        url = getURL()
        nested_tab = []
        data_updates = openNewTab(title, url, nested_tab)
        updateJsonFile(data_updates)
        print(">>> New tab titled:",title,"\n>>> with the URL:",url,"\n>>> Was successfully opened!")
        backToMenu()

    if choice == 2:  #2. Close Tab
        index = getIndex()
        updates = closeChosenTab(index)
        updateJsonFile(updates)
        print(">>> Tab was successfully closed!")
        backToMenu()

    if choice == 3:  #3. Switch Tab
        index = getIndex()
        displayTabContent(index)
        backToMenu()

    if choice == 4:  #4. Display All Tabs
        printAllTitles()
        backToMenu()

    if choice == 5:  #5. Open Nested Tab
        index = getIndex()
        title = getTitle()
        url = getURL()
        update = addNestedTab(index, title, url)
        updateJsonFile(update)
        print(">>> Nested tab with title:",title,"\n>>> and with the URL:",url,"\n>>> Was successfully opened!")
        backToMenu()

    if choice == 6:  #6. Clear All Tabs
        update = closeAllTabs()
        updateJsonFile(update)
        print(">>> All tabs were successfully closed!")
        backToMenu()

    if choice == 7:  #7. Save Tabs
        file_path = getPath()
        saveCurrentState(file_path)
        print(">>> Data was saved successfully!")
        backToMenu()

    if choice == 8:  #8. Import Tabs
        file_path = getPath()
        imported_list = importJsonFile(file_path)
        #even if the imported file data is not valid or the file doesn't exist, 
        # the code keeps executing and passes the returned value to the next function
        # causing an error. So this while loop down here is to prevent that.
        while imported_list != list:
            file_path = getPath()
            imported_list = importJsonFile(file_path)
        updates = mergeLists(imported_list)
        updateJsonFile(updates)
        print(">>> Data was imported successfully!")
        backToMenu()

    if choice == 9:
        print("###################################################################\n###################################################################")
        print("\t>>> Thank You Mr. Georgio for Using ABTS <<<")
        print("###################################################################\n###################################################################")

main()


