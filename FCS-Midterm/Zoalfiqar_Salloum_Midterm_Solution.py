
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
        getTitle()


