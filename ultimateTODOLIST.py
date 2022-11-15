# David Liddle 11/11/2022
# COM S 127 - Assignment 5

# add a clear function to clear the screen between transitions from the main menu and the application menu

import pickle, sys
from os import system, name
from time import sleep

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

# This function initializes a todolist as a python dicitonary with 5 sub categories of a list
def initList():
    todoList = {}
    todoList['backlog'] = []
    todoList['todo'] = []
    todoList['in_progress'] = []
    todoList['in_review'] = []
    todoList['done'] = []
    
    return todoList

# This function saves the created list as a pickled data structure
def saveList(todoList):
    try:
        listName = input("Enter List Name (Exclude .lst Extension): ")
        with open('./' + listName + '.lst', 'wb') as pickle_file:
            pickle.dump(todoList, pickle_file)
    except:
        print("ERROR (saveList): /{0}.lst is not a valid file name!".format(listName))
        sys.exit()

# Function that reloads the saved pickle file and deserializes it
def loadList():
    try:
        listName = input("Enter List Name (Exclude .lst Extension): ")
        with open('./' + listName + '.lst','rb') as pickle_file:
                    todoList = pickle.load(pickle_file)
    except:
        print("ERROR (loadList): ./{0}.lst was not found!".format(listName))
        sys.exit()

    return todoList

# this function returns three values whether or not the item exists within the list
def checkItem(item, todoList):
    itemFound = False
    keyName = ""
    index = -1
    for keys in todoList.keys():
        if (item in todoList[keys]):
            itemFound = True
            keyName = keys
            index = todoList[keys].index(item)
        
    return itemFound, keyName, index
    
# Add an Item to the todo list
def addItem(item, toList, todoList):
    itemFound, keyName, index = checkItem(item, todoList) 
    if (itemFound):
        print(f'The item: {item} is located at key: {keyName}, index {index}')

    else:
        todoList[toList].append(item)
    
    return todoList

# Delete item if itemFound == true
def deleteItem(item, todoList):
    itemFound, keyName, index = checkItem(item, todoList)
    if (itemFound):
        todoList[keyName].pop(index)
    else:
        print(f'The item: {item} was not found.')

    return itemFound, todoList 

# Move Item from one index of a list to the other
def moveItem(item, toList, todoList):       
    itemFound, keyName, index = checkItem(item, todoList)
    if (keyName in todoList):
        addItem(item, toList, todoList)
        deleteItem(item, todoList)
# Prints todoList dictionary for the user to see
def printTODOList(todoList):
    for keys in todoList:
        print(f'{keys}: {todoList[keys]}')

# This function executes the Application Menu
def runApplication(todoList):
    clear()
    while True:
        print(66*'-')
        choice = input("APPLICATION MENU: \n\ta: add ITEM to list\n\tm: move ITEM\n\td: delete ITEM\n\ts: save list \n\tq: quit to main menu \n")
        print()

        if choice == "a":
            clear()
            print("TODO list CATEGORIES: ")
            for keys in todoList.keys():
                print('\t' + keys)
            print()
            
            # create a variable from user input to be added to the list
            item = input("Enter an ITEM to be added to a CATEGORY of the list: ")
            toList = input("Enter the full CATEGORY name: ")
            keysList = list(todoList.keys())
            if toList not in keysList:
                raise Exception("Enter only a CATEGORY that is listed")

            addItem(item, toList, todoList)
            print()
            print(f'ITEM: {item} added to CATEGORY {toList}:')
            print()
            printTODOList(todoList)
            sleep(3)
            clear()
        
        elif choice == "m":
            
            # Check to see if any of the lists in the data structure have items in them.
            item = input("Enter an item name is to be moved: ")  
            todoListValues = list(todoList.values())
            todoListValuesAppended = []
            print(todoListValues)
            for i in range(0, len(todoListValues)):
                for j in range(0, len(todoListValues[i])):
                    todoListValuesAppended.append(todoListValues[i][j])
            if todoListValuesAppended == []:
                raise Exception("There are no values to move.")
            elif item not in todoListValuesAppended:
                raise Exception("The inputted value is not in the list")     
            else:
                print("Here are the categories of the list: ")
                print()
                for keys in todoList.keys():
                    print(keys)
                print()
                toList = input("Enter the category of the list the item will be added to. ")
                print()
                deleteItem(item, todoList)
                addItem(item, toList, todoList) 
                printTODOList(todoList) 
        
        elif choice == "d":
           item = input("Enter the item name that is to be deleted: ")
           print(f'ITEM: {item} deleted.')
           deleteItem(item, todoList)
           print()
           printTODOList(todoList)
           sleep(3)
           clear() 
        
        elif choice == "s":
            saveList(todoList)
            print("Saving List...")
            print()
            printTODOList(todoList)

        elif choice == "q":
           print("Returning to MAIN MENU...")
           print()
           main()
           break

    return todoList

# Main and Main Menu
def main():
    taskOver = False
    clear()
    print("The ultimate TODO List")
    print()
    print("    %%%")
    print("   =====")
    print("  &%&%%%&")
    print("  %& < <%")
    print("   &\__/")
    print("    \ |____")
    print("   .', ,  ()")
    print("  / -.  _)|") 
    print(" |_(_.    |")
    print(" '-'\  )  |")
    print(" mrf )    |")
    print("    /  .  ).")
    print("   /    _. |")
    print(" /'---':.-'|")
    print("(__.' /    /")
    print(" \   ( /  /")
    print("  \ /  _  |") 
    print("   \  |  '|")
    print("   | . \  |")
    print("   |(     |") 
    print("   |  \ \ |")
    print("    \  )\ |")
    print("   __)/ / \\")
    print("--*--(_.Ooo*----")
    print()
    print("By: David Liddle")
    print("[COM S 127 B]")
    print()
    sleep(2)
    clear()

    while taskOver == False:
        print(66*'-')
        choice = input("MAIN MENU \n\tn: new list \n\tl: load list \n\tq: quit\n")
        print()

        if choice == "n":
            todoList = initList()
            clear()
            print('NEW TODO LIST INITIALIZED')
            print(66*'-')
            print('LIST/CATEGORIES: ')
            print()
            printTODOList(todoList)
            print('...')
            sleep(2)
            clear()
            runApplication(todoList)
    
        elif choice == "l":
            todoList = loadList()
            printTODOList(todoList)
            runApplication(todoList)

        elif choice == "q":
            taskOver = True
            print("Goodbye!")
            print()
            sleep(2)
            clear()
        else:
            clear()
            print("Please enter one of the MAIN MENU arguments")
            print()

if __name__ == "__main__":
    main()