# -*- coding: utf-8 -*-

from datetime import datetime
now = datetime.now()


def date(): #Funktion die bei eintippen von date() immer dieses Datum wiedergibt
    return "%s.%s.%s" % ( now.day, now.month, now.year)








class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

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
    elif status == "no" or "NO" or "No":
        importance = raw_input("Is this task your priority?(yes/no)\n>> ")
        todolist.append(task) #schreibt den Beitrag hinten dran
        tododict[task] = False
        if importance == "yes":
            todolist.pop() #löscht den letzten Eintrag
            todolist.insert(0, task) #setzt den Beitrag an erster Stelle
            tododict[task] = True #Ich brauche nicht als erstes die Liste anzugeben und dann die Nummer des Eintrags, kann auch direkt task in den dict eingeben und er sucht den Namen im dict und setzt diesen TRue/False

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
            print bcolors.HEADER + bcolors.BOLD + "%s.%s %s" % (t, todolist[i], date()) + bcolors.ENDC

        elif tododict[todolist[i]] is False:
            print "%s.%s %s" % (t, todolist[i], date())
        todo_file.write("\n%s.%s %s" % (t, todolist[i], date()))# add task into the TXT file


    print bcolors.UNDERLINE + "\nCompleted tasks:" + bcolors.ENDC
    todo_file.write("\n\nCompleted tasks:")  # write into the TXT file
    for i in range(len(donelist)):
        t = i + 1
        print "%s.%s %s " %(t, donelist[i], date())
        todo_file.write("\n%s.%s %s" % (t, donelist[i], date()))  # add task into the TXT file

    print bcolors.OKBLUE + "\n\nYou have already finished %s tasks of %s tasks" % (len(donelist), len(todolist)+len(donelist)) + bcolors.ENDC

    todo_file.write("\n\nYou have already finished %s tasks of %s tasks!" % (len(donelist), len(todolist)+ len(donelist)))



print "\n\n\nEND"