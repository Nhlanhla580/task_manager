import datetime

fileOpen = open(r'C:\Users\nhlanhla.nkosi\Dropbox\Nhlanhla Nkosi-48928\Introduction to Programming\Task 25\tasks.txt','r+')  # open/create files in write mode
userOpen = open(r'C:\Users\nhlanhla.nkosi\Dropbox\Nhlanhla Nkosi-48928\Introduction to Programming\Task 25\user.txt','r+')  # open/create files in write and read mode


def print_menu():
    print("Please select one of the following options: ")
    print('r - register a user')
    print('a - add task')
    print('va - view all tasks')
    print('vm - view my tasks')
    if username == 'admin':
        print("ds - Display statistics")
        print("gr - generate report")
        print('e - exit\n')
    print

check = ''
x = False
y = False
taskAssignedTo = ""
isTask_Complete = "No"
assignDate = datetime.datetime.now()
completeDate = ""
username = input("Enter a username: ")
password = input("Enter a Password: ")
storedUsers = ""
storedPassword = ""
logCounter = 0
errorMessage = "Incorrect username or password, please try again."
taskCounter = 0
titleCounter = 0
newCounter = 0
task_Sequence = 0
newVar = ""
taskDictionary = {}
dicCounter = 0
noSum = 0
yesSum = 0
monthsDictionary = {"Jan": 1,
                    "Feb": 2,
                    "Mar": 3,
                    "Apr": 4,
                    "May": 5,
                    "Jun": 6,
                    "Jul": 7,
                    "Aug": 8,
                    "Sep": 9,
                    "Oct": 10,
                    "Nov": 11,
                    "Dec": 12}
per_user_count = 0
overDueCounter = 0
test = ''
userTaskCount = ''
userPercentage = ''
test2 =''
checkCounter = 0
test3 = ''
no_and_uncomplete = ''
userNoCount = ''
yesUserCount = ''
percentageNoUser=''
percentageYesUser=''

# task title stored in a list which i will use when formatting my tasks in a user friendly manner

taskTitles = ["Assigned To:\t ", "Task:\t\t ", "Task Description: ", "Date assigned: ", "Due Date: \t", "Task Completed: "]
lenTitiles = len(taskTitles)

for line in userOpen:
    storedUsers += line.split(",")[0]
    storedUsers += "\n"
    storedPassword += line.split()[1]
    storedPassword += "\n"
    lenUsers = len(storedUsers.split())

while x == False :
      if password == storedPassword.split()[logCounter] and username == storedUsers.split()[logCounter]:
            print("\nWelcome to the Task Management Program:\n")
            print_menu()
            x = True
      elif password != storedPassword.split()[logCounter] or username != storedUsers.split()[logCounter]:
            logCounter+=1
      if logCounter == lenUsers:
          print(errorMessage)
          logCounter = 0
          username = input("Enter a username: ")
          password = input("Enter a Password: ")

userSelection = input("Enter Selection: ")

while y == False:
    if userSelection == "vm":
        for line in fileOpen:
            task_Sequence += 1
            newVar += line
            taskDictionary[str(task_Sequence)] = line
            if username in line:
                print("Task No.", "\t\t " + str(task_Sequence))
                for t in line.split(","):
                    print(taskTitles[titleCounter], "\t" + t)
                    titleCounter += 1
                    if titleCounter >= lenTitiles:
                        titleCounter = 0
                        y = True
        print("Enter the number of the task you would like to edit\n")
        choice = input("Make a selection or enter '-1' to go back to menu: \n")
        if choice in taskDictionary:
            for i in taskTitles:
                print(i, "\t" + taskDictionary[choice].split(',')[dicCounter])
                dicCounter += 1
            edit = input(
                "If you would like to mark task as complete enter 'y' and to change due date and reassign enter 'change': ")
            if edit == "y":
                taskDictionary[choice] = taskDictionary[choice].replace("No", "Yes")


                for p in taskDictionary:
                    newVar = [p for p in taskDictionary.values()]
                for line in newVar:
                    check += line
                print("Done!")
                fileOpen.close()
                fileOpen = open('tasks.txt','w')
                fileOpen.write(check)

            if edit == "change" and "Yes" not in taskDictionary[choice].split(',')[5]:
                reassign = input("Do you want to 'Reassign' user, 'Change due date' or 'Both' ?").lower()
                if reassign == "reassign":
                    user = input(" Please enter the username: ")
                    taskDictionary[choice] = taskDictionary[choice].replace(taskDictionary[choice].split(',')[0], user)
                    for p in taskDictionary:
                        newVar = [p for p in taskDictionary.values()]
                    for line in newVar:
                        check += line
                    print("Done!")
                    fileOpen.close()
                    fileOpen = open('tasks.txt','w')
                    fileOpen.write(check)
                elif reassign == "change due date":
                    due = input("Please enter the due date e.g 60 Oct 2020: ")
                    taskDictionary[choice] = taskDictionary[choice].replace(taskDictionary[choice].split(',')[4], due)
                    for p in taskDictionary:
                        newVar = [p for p in taskDictionary.values()]
                    for line in newVar:
                        check += line
                    print("Done!")
                    fileOpen.close()
                    fileOpen = open('tasks.txt','w')
                    fileOpen.write(check)
                elif reassign == "both":
                    user = input(" Please enter the username: ")
                    due = input("Please enter the due date e.g 6 Oct 2020: ")
                    taskDictionary[choice] = taskDictionary[choice].replace(taskDictionary[choice].split(',')[0], user)
                    taskDictionary[choice] = taskDictionary[choice].replace(taskDictionary[choice].split(',')[4], due)
                    for p in taskDictionary:
                        newVar = [p for p in taskDictionary.values()]
                    for line in newVar:
                        check += line
                    print("Done!")
                    fileOpen.close()
                    fileOpen = open('tasks.txt','w')
                    fileOpen.write(check)
                print(taskDictionary[choice].split(",")[::])

        elif choice == '-1':
            print_menu()
            userSelection = input("Enter Selection: ")

        # if user selects to add a task, user will be prompted accordingly and tasks will be added as per the format secified

    if userSelection == "a":
        fileOpen = open('tasks.txt','r+')
        for line in fileOpen:
            username = input("Enter a username: ")
            title = input("What is the Title of Task: ")
            taskDescription = input("Brief description of the task: ")
            print("Please enter dates as the example format e.g '5 Oct 2019' ")
            dueDate = input("Please enter the due date: ")
            assignDate = datetime.datetime.now()
            isTask_Complete = "No"
            a = fileOpen.write(
                  "\n" + username + "," + " " + title + "," + " " + taskDescription + "," + " " + str(
                        assignDate.strftime(
                            "%d" + " " + "%b" + " " + "%Y")) + "," + " " + dueDate + "," + " " + isTask_Complete)
            print("task has been added!")
            y = True

# r will allow you to register user only as admin user, otherwise will allow you to make another selection

    if userSelection == "r" and username == "admin":
        print("\nPlease enter the username first, then the password and confirm")
        username = input("Enter a username: ")
        password = input("Enter a Password: ")
        passConfirm = input("Please Confirm your Password: ")
        if username in storedUsers.split()[::]:
            while y == False:
                print("\nusername exists Please enter a different username: ")
                username = input("Enter a username: ")
                password = input("Enter a Password: ")
                passConfirm = input("Please Confirm your Password: ")
                if passConfirm == password and username not in storedUsers.split()[::]:
                    r = userOpen.write("\n" + username + "," + " " + password)
                    print("User has been added!")
                    y = True
        elif passConfirm == password:
            r = userOpen.write("\n" + username + "," + " " + password)
            print("User has been added!")
            y = True


        elif passConfirm != password:
            while y == False:
                print("\nPassword Confirmation did not match: ")
                username = input("Enter a username: ")
                password = input("Enter a Password: ")
                passConfirm = input("Please Confirm your Password: ")
                if passConfirm == password:
                    r = userOpen.write("\n" + username + "," + " " + password)
                    print("User has been added!")
                    y = True

    elif userSelection == "r" and username != "admin":
        print("\nSorry you are not the admin! , Please make another selection: ")
        print_menu()
        userSelection = input("Enter Selection: ")

# if user makes selection to view all tasks, code will loop through the lines and format the results in user friendly manner with the relevent title from my list

    if userSelection == "va":
        fileOpen = open('tasks.txt','r+')
        for line in fileOpen:
            for t in line.split(","):
                print(taskTitles[titleCounter], "\t" + t)
                titleCounter += 1
                if titleCounter >= lenTitiles:
                    titleCounter = 0
                    y = True

# this option is only available for admin user only to see how many users and tasks there are
    if userSelection == "ds" and username == "admin":
        fileOpen = open('tasks.txt','r+')
        userOpen = open('user.txt', 'r+')
        for line in fileOpen:
            lenTask = len(line.split()[0])
            taskCounter+=1
        print("\nThe Total amount of users {}\nThe total number of Task is {}".format(lenUsers,taskCounter))
        y = True
    elif userSelection == "s" and username != "admin":
        print("invalid selection")
        y = True

# this option is available for admin only to generate reports
# check how may Yes's and No's i have

    if userSelection == "gr" and username == "admin":
        fileOpen = open('tasks.txt','r+')
        userOpen = open('user.txt', 'r+')
        for line in fileOpen:
            lenTask = len(line.split()[0])
            taskCounter+=1
            if "Yes" in line.split(',')[5]:
               yesSum +=1
            elif "No" in line.split(',')[5]:
                noSum += 1

# the below is to check if a task is overdue, this first checks if the due date year is less than the current year then check if month is greater than or equal to then checks if day is less than today's date

            if line.split(',')[4].split()[2] < assignDate.strftime("%Y"):
                overDueCounter+=1
                if monthsDictionary[line.split(',')[4].split()[1]] >= monthsDictionary.get(
                    assignDate.strftime("%b")) and line.split(',')[4].split()[0] >= assignDate.strftime("%d"):
                    overDueCounter+=1
            elif monthsDictionary[line.split(',')[4].split()[1]] >= monthsDictionary.get(assignDate.strftime("%b")) and line.split(',')[4].split()[0] < assignDate.strftime("%d"):
                print('')
            for i in line.split(',')[0]:
                test+=i
# this checks for the user and the completed yes or no, and adds it to my new variables for me to use to count

            test2 +=line.split(',')[0] + line.split(',')[5]
            if 'No' in line.split(',')[5]:
                userNoCount+=line.split(',')[0] + line.split(',')[5]
            if 'Yes' in line.split(',')[5]:
                yesUserCount+=line.split(',')[0] + line.split(',')[5]


            if 'No' in line.split(',')[5]:
                if line.split(',')[4].split()[2] < assignDate.strftime("%Y"):
                    test3+= line.split(',')[0] + line.split(',')[4]+line.split(',')[5]
                elif monthsDictionary[line.split(',')[4].split()[1]] >= monthsDictionary.get(assignDate.strftime("%b")) and line.split(',')[4].split()[0] < assignDate.strftime("%d"):
                    test3 += line.split(',')[0] + line.split(',')[4] + line.split(',')[5]


# this loops as many times as the amount of users i have and performs my calculations accordingly and add to my new variables then i will write to file and read from file to display onto screen

        for x in storedUsers.split():
            userTaskCount += "The total number of tasks assigned to "+ storedUsers.split()[per_user_count] + ' is ' + str(test.count(storedUsers.split()[per_user_count]))+"\n"
            userPercentage += "The percentage of the total number of task for " + storedUsers.split()[per_user_count] + ' is ' + str(test.count(storedUsers.split()[per_user_count]) / taskCounter * 100)+"\n"
            percentageNoUser += "The percentage of task assigned to the user that have not been completed for " + storedUsers.split()[per_user_count] + ' is ' + str(userNoCount.count(storedUsers.split()[per_user_count]) / test.count(storedUsers.split()[per_user_count]) * 100) +"\n"
            percentageYesUser += "The percentage of task assigned to the user that have been completed for " + storedUsers.split()[per_user_count]+ ' is ' + str(yesUserCount.count(storedUsers.split()[per_user_count]) / test.count(storedUsers.split()[per_user_count]) * 100)+"\n"
            no_and_uncomplete += "The percentage of task assigned to the user that have not been completed and overdue for " +  storedUsers.split()[per_user_count] + ' '+ str(test3.count(storedUsers.split()[per_user_count]) / test.count(storedUsers.split()[per_user_count]) * 100)+"\n"
            per_user_count+=1

        taskOverView = open('task_overview.txt','w') 
        userOverView = open('user_overview.txt','w')  

        taskOverView.write("The total number of Task is {}\n".format(taskCounter))
        taskOverView.write("The Total number of completed is Task {}\n".format(yesSum))
        taskOverView.write("The Total number of uncompleted Task is {}\n".format(noSum))
        taskOverView.write("The total number of overdue Tasks is {}\n".format(overDueCounter))
        taskOverView.write("The percentage of tasks that is incomplete is "+ str(noSum /taskCounter * 100)+"\n")
        taskOverView.write("The percentage of tasks that are overdue is " + str(overDueCounter / taskCounter * 100))



        userOverView.write("The total number of users registered with task_manager.py is {}\n".format(lenUsers))
        userOverView.write("The total number of tasks that have been generated and tracked using the task_manager.py is {}\n".format(taskCounter))
        userOverView.write(userTaskCount)
        userOverView.write(userPercentage)
        userOverView.write(percentageNoUser)
        userOverView.write(percentageYesUser)
        userOverView.write(no_and_uncomplete)
        y = True
    elif userSelection == "gr" and username != "admin":
        print("invalid selection")
        y = True


    taskOverView = open('task_overview.txt','r')
    userOverView = open('user_overview.txt','r')

    print("This is the Task Overview!!\n")
    for line in taskOverView:
        print(line)
    print('\n')
    print("This is the User Overview!!\n")
    for line in userOverView:
        print(line)


# this will exit out of the program



    if userSelection == "e":
        exit(0)


taskOverView.close()
userOverView.close()
userOpen.close()
fileOpen.close()
