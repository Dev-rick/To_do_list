# -*- coding: utf-8 -*-

from datetime import datetime



def date(): #Funktion die bei eintippen von date() immer dieses Datum wiedergibt
    return "%s:%s:%s / %s.%s.%s" % (now.hour, now.minute, now.second, now.day, now.month, now.year)


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
    now = datetime.now()  #Hier wird der Moment definiert in dem die Zeit gespeichert wird.
    task_date = task + "        " + "("+date()+")"  #Hier wird durch die oben genannte Funktion dieser Variable task_date diese gepeicherte Zeit hinzugefügt
    #Jedesmal wenn dieses neu durchlaufen wird wird auch eine neue Zeit gespeichert die dann wieder dieser Variablen zugefügt wird.
    status = raw_input("Was the task completed yet? (yes/no)\n>> ")
    if status == "yes":
        donelist.append(task_date)
    elif status == "no" or "NO" or "No":
        importance = raw_input("Is this task your priority?(yes/no)\n>> ")
        todolist.append(task_date) #schreibt den Beitrag hinten dran
        tododict[task_date] = False
        if importance == "yes":
            todolist.pop() #löscht den letzten Eintrag
            todolist.insert(0, task_date) #setzt den Beitrag an erster Stelle
            tododict[task_date] = True #Hier shreibe ich in den dict. den Namen des task und gib ihm den bool True!
    #Wenn task nicht in ein dict geschrieben wird würde wenn man ihn printen würde er als True oder False erscheinen!
    #Es existiert also parallel ein dict und eine Liste und der dict enthählt die gleichen Namen die auch in der Liste stehen somit kann ich wenn..
    #ich wissen will ob diser todoEintrag den bool True oder False hat frage ich ihn mit dem gleichen Namen somit kann man in einer for schleife testen..
    #ob ein todoEintrag True oder False ist wen man tododict[todolist[i]] anführt somit wird der Name des ersten Eintrag in der Liste als string gestzt der...
    #von dem tododict nun gesucht wird und kann somit die Bedingung stellen if ... == True: -->geschieht etwas.

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
        if tododict[todolist[i]] is True: #Hier ist todolist[i] = den ersten Namen der todoliste!! Somit sucht Python im dict nach diesem Namen!
            print bcolors.HEADER + bcolors.BOLD + "%s.%s" % (t, todolist[i]) + bcolors.ENDC

        elif tododict[todolist[i]] is False:
            print "%s.%s" % (t, todolist[i])
        todo_file.write("\n%s.%s" % (t, todolist[i]))# add task into the TXT file


    print bcolors.UNDERLINE + "\nCompleted tasks:" + bcolors.ENDC
    todo_file.write("\n\nCompleted tasks:")  # write into the TXT file
    for i in range(len(donelist)):
        t = i + 1
        print "%s.%s" %(t, donelist[i])
        todo_file.write("\n%s.%s" % (t, donelist[i]))  # add task into the TXT file

    print bcolors.OKBLUE + "\n\nYou have already finished %s tasks of %s tasks" % (len(donelist), len(todolist)+len(donelist)) + bcolors.ENDC

    todo_file.write("\n\nYou have already finished %s tasks of %s tasks!" % (len(donelist), len(todolist)+ len(donelist)))



print "\n\n\nEND"