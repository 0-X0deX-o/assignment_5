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
        else:
            print("ERROR: Please enter [a], [m], [d], [s], [d] or [q].")
            print()

    return todoList

# Function 10: Defining the main function
def main():
    taskOver = False

    print("The Ultimate TODO List")
    print()
    
    # TODO: Have student print their name/ section when the script runs (0.5 pt.)
    print("By: <Student Name>")
    print("[COM S 127 <section>]")
    print()

    while taskOver == False:
        print("-----------------------------------------------------------------")
        choice = input("MAIN MENU: [n]ew list, [l]oad list, or [q]uit?: ")
        print()
        if choice == "n": 
            todoList = initList()

            printTODOList(todoList)
            
            runApplication(todoList)
        elif choice == "l":
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

# Advanced Tasks
#   How to inocrporate into graphical format/visual format

