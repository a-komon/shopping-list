#Alex 
 
#Function
def list():
    print("Please choose an option. Type in a number between 1-5")
    print("1. Add a task \n 2. View current list \n 3. Mark task completed \n 4. Remove a task \n 5.Remove all items from list \n 6. Sort the list alphabetically \n 7.Print the number of Items on List \n 8. Exit program")

    todo=["bread", "carrot","milk","apple"]
    option=int(input("Option:  "))

    if option ==1:
        item=input("what item do you want to add?")
        todo.append(item)
        print (todo)
        list()
    elif option == 2:
        print (todo)
        list()
    elif option ==3:
        complete=input("what item is complete?")
        x=todo.index(complete)
        todo[x]=complete+" X"
        print(todo)
        list()
    elif option ==4:
        remove=input("What item do you want to remove?")
        todo.remove(remove)
        print(todo)
        list()
    elif option ==5:
        todo.clear()
        print(todo)
        list()
    elif option==6:
      todo.sort()
      print(todo) 
      list()
    elif option ==7:
         print(len(todo))
         list()
    elif option==8:
        ans=input("Would you like to adjust the list?")
        if ans=="yes":
            list()
        elif ans=="no":
            quit()
    
#main
list()
