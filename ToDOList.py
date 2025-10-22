from tkinter import *

#program Functions

def addToDofunction():
    thereNewTask = newTaskEntry.get()
    if thereNewTask != "":
        tasksListBox.insert(END, thereNewTask)
    else:
        print("Please enter a task.")    

    

def deleteToDofunction():
    tasksListBox.delete(ANCHOR)

    


#program starts here

CodeSoft_root = Tk()

CodeSoft_root.title("To-Do List Application")
CodeSoft_root.geometry("600x500")
CodeSoft_root.config(bg="#f3efe8")
CodeSoft_root.resizable(0,0)

#End of the GUI window configuration

#Listbox to display tasks
tasksListBox = Listbox()
tasksListBox.pack()

#Button for adding tasks
addToDo = Button(text="Add New Task", command=addToDofunction)
addToDo.pack()

#Button for deleting tasks
deleteToDo = Button(text="Delete Task", command=deleteToDofunction)
deleteToDo.pack()

#Input field for adding new tasks
newTaskEntry = Entry()
newTaskEntry.pack()

CodeSoft_root.mainloop()




