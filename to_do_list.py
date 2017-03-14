# -*- coding: utf-8 -*-



"""class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'"""

print "Welcome to the TODO task management program!"

donelist = [ ]

todolist = [ ]

tododict = { }


while True:
    task = raw_input("\nPlease enter a TODO task: ")
    print "Your task is: " + task + "\n"
    status = raw_input("Was the task completed yet? (yes/no)\n>> ")
    if status == "yes":
        donelist.append(task)
        tododict[donelist[len(donelist)-1]] = True
    elif status == "no" or "NO" or "No":
        todolist.append(task)
        importance = raw_input("Is this task your priority?(yes/no)\n>> ")
        if importance == "yes":
            tododict[todolist[len(todolist)-1]] = True
        elif importance == "no":
            tododict[todolist[len(todolist)-1]] = False


    newtask = raw_input("\nWould you like to enter new task? (yes/no)\n>> ")
    if newtask == "yes":
        continue
    elif newtask == "no":
        break

with open("todo.txt", "w+") as todo_file: # open the TXT file (or create a new one)

    print bcolors.UNDERLINE + "\nIncompleted tasks:" + bcolors.ENDC
    todo_file.write("\nIncompleted tasks:") # write into the TXT file
    for i in range(len(todolist)):
        t = i + 1
        if tododict[todolist[i]] is True:
            print bcolors.HEADER + bcolors.BOLD + "%s.%s" % (t, todolist[i]) + bcolors.ENDC

        elif tododict[todolist[i]] is False:
            print "%s.%s" % (t, todolist[i])
        todo_file.write("\n%s. %s" % (t, todolist[i]))# add task into the TXT file


    print bcolors.UNDERLINE + "\nCompleted tasks:" + bcolors.ENDC
    todo_file.write("\n\nCompleted tasks:")  # write into the TXT file
    for i in range(len(donelist)):
        if tododict[donelist[i]] is True:
            t = i + 1
            print "%s. %s" %(t, donelist[i])
            todo_file.write("\n%s.%s" %(t, donelist[i]))  # add task into the TXT file

    print bcolors.OKBLUE + "\nYou have already finished %s tasks of %s tasks" % (len(tododict)-len(donelist), len(tododict)) + bcolors.ENDC

    todo_file.write("\nYou have already finished %s tasks of %s tasks!" % (len(tododict)-len(donelist), len(tododict)))



print "\n\n\nEND"