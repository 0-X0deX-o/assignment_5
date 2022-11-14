# David Liddle 11/11/2022
# COM S 127 - Assignment 5

#X1 init list
#X2 save list
#X3 load list
#X4 check item
#X5 add item
#X6 delete item
#X7 move item
# 8 printTODOList
# 9 run application
# 10 main


import pickle, sys

# This function initializes a todolist as a python dicitonary with 5 sub categories of a list
def initList():
    todoList = {}
    todoList['backlog'] = []
    todoList['todo']
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
    if (is_in_todolist):
        todoList[x].pop(y)
    else:
        print(f'The item: {item} was not found.')

    return itemFound, todoList 

# Move Item from one index of a list to the other
def moveItem(item, toList, todoList):       
    itemFound, keyName, index = checkItem(item, todoList)
    if (keyName in todoList):
    addItem(item, toList, todoList)
    deleteItem(item, todolist)

def printTODOList(todoList):
    for keys in example_dict:
        print(f'{keys}: {example_dict[keys]}')

def runApplication(todoList):
    while True:
        print(66*'-')
        choice = input("APPLICATION MENU: [a]dd to backlog, [m]ove item, [s]ave list, or [q]uit to main menu?: ")
        prine()

        if choice == "a":
            for keys in example_dict.keys():
                print('Here are the categories of the list.\n\t' + keys)
            # create a variable from user input to be added to the list
            item = input("Enter an item to be added to a category of the list: ")
            
            # Yeah, get some input validation in there.
            toList = input("Enter the category name: ")

            addItem(item, toList)
            printTODOList(todoList)
        
        elif choice == "m":
            # Check to see if any of the lists in the data structure have items in them.
            itemsInList = False    
            for keys in todoList.keys():
                if todoList[keys] != []:
                    itemsInList = True
            # </code>
            pass
        
        elif choice == "d":
            # </code>
            pass

        elif choice == "s":
            saveList(todoList)
            print("Saving List...")
            print()
            printTODOList(todoList)

        elif choice == "q":
            # </code>
           print("Returning to MAIN MENU...")
           print()

    return todoList

# Main
def main():
    taskOver = False

    print("The ultimate TODO List")
    print()

    print("By: David Liddle")
    print("[COM S 127 B]")
    print()

while taskOver == False:
    print(66*'-')
    choice = input("MAIN MENU: [n]ew list, [l]oad list, or [q]uit?: ")
    print()

    if choice == "n":
        todoList = initList()
        
        printTODOList(todoList)
        
        runApplication(todoList)
    
    elif chioce == "l":
        todoList = loadList()

        printTODOList(todoList)

        runApplication(todoList)

    elif choice == "q":
        taskOver = True
        print("Goodbye!")
        print()

    else:
        print("Please enter [n], [l], or [q]...")
        print()

if __name__ == "__main__":
    main()
# Input validation for a python object



# class the determines entries?
#    what should the sub attributes of an object be

# What are the specifics of a how data changes when serialized?
# Plan to learn web assembly
