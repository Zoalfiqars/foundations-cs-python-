
###################################################################
###################################################################
###################### FCS Midterm Project ########################
###################### Zo Alfiqar Salloum #########################
############### Advanced Browser Tabs Simulation ##################
################### Friday, November 10, 2023 #####################
###################################################################
###################################################################
tabs_list = [{"title":"SE Factory", "URL":"https://sefactory.webflow.io/"}]





###################################################################
###################################################################
########### This function displays the software menu ##############
###################################################################
###################################################################
def displayMenu():
    print("Welcome to ABTS.\nThe most Advanced Browser Tabs Simulation.\nHere is the Menu, please choose wisely:\n1. Open Tab\n2. Close Tab\n3. Switch Tab\n4. Display All Tabs\n5. Open Nested Tabs\n6. Clear All Tabs\n7. Save Tabs\n8. Import Tabs\n9. Exit ABTS")





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





def openNewTab(title, url):
    dic = {"Title":title, "URL":url}
    tabs_list.append(dic)
