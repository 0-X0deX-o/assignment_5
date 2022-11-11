# David Liddle 11/11/2022
# COM S 127 - Assignment 5

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

# figure out what this portion of the code does
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
    # TODO: Use the checkItem function to see if the specified 'item' already exists in the dictionary
    # of lists. If the item is not in the dictionary of lists, add it to the list specified by the 'toList'
    # variable. If the item is already in the dictionary of lists, print an error message specifying:
    # - the name of the item
    # - the keyName of the list where the item is found
    # - the index of the item in the list
    # Return the todoList data structure after it has been modified (or not) (1 pt.)

def addItem(item, toList, todoList):
    # TODO: Use the checkItem function to see if the specified 'item' already exists in the dictionary
    # of lists. If the item is not in the dictionary of lists, add it to the list specified by the 'toList'
    # variable. If the item is already in the dictionary of lists, print an error message specifying:
    # - the name of the item
    # - the keyName of the list where the item is found
    # - the index of the item in the list
    # Return the todoList data structure after it has been modified (or not) (1 pt.)
    itemFound, keyName, index = checkItem(item, todoList) 
    if (is_in_todoList):
        print(f'The item: {item} is located at key: {keyName}, index {index}')

    else:
        todoList[toList].append(item)
    
    return todoList

def deleteItem(item, todoList):
    itemFound, keyName, index = checkItem(item, todoList)
    if (is_in_todolist):
        todoList[x].pop(y)
    else:
        print(f'The item: {item} was not found.')

    return itemFound, todoList 


# Input validation for a python object



# class the determines entries?
#    what should the sub attributes of an object be

# What are the specifics of a how data changes when serialized?
# Plan to learn web assembly
