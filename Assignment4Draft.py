#!/usr/bin/python3

##############################################     
##   Author: Andre Celliers                 ##
##   Date:   2022-10-30                     ##
##   Title:  Assignment 4 PROG1700          ##
##############################################

"""
Personal Project Tracker

Please choose one of the following entries:
1. View all projects
2. View all tasks
3. Create new project
4. Create new task
5. Delete project
6. Delete a task
7. Quit the program

"""
import sqlite3
from sqlite3 import Error
import Assignment4Functions as f

print("\n\t\t### Welcome to the Assignment Tracker!! ###" + '\n\n' + "Here are the following commands available to you, to choose a command enter the corresponding number." + '\n' + "\t\n 1. View all projects" + "\t\n 2. View all tasks" + "\t\n 3. Create new project" + "\t\n 4. Create new task" + "\t\n 5. Delete project" + "\t\n 6. Delete a task" + "\t\n 7. Quit the program")

userInput = (input("Choose an input: "))

database = r"ass4.db"
conn = f.create_connection(database)
f.create_table_for_projects(conn)
f.create_table_for_tasks(conn)

while userInput != "7":
    if userInput == "1":
        print("You've selected view all projects")
        f.select_all_projects(conn)
        userInput = (input("Choose another input: "))
    elif userInput == "2":
        print("You've selected view all tasks")
        f.select_all_tasks(conn)
        userInput = (input("Choose another input: "))
    elif userInput == "3":
        print("You've selected create new project")
        f.create_project(conn)
        project = ('Andre App with Python and SQL', '2015-01-01', '2015-01-30')
        project_id = f.create_project(conn, project)
        userInput = (input("Choose another input: "))
    elif userInput == "4":
        print("You've selected create new task")
        f.create_task(conn)
        task_1 = ('Complete the third task', 1, 1, 2, '2015-01-01', '2015-01-02')
        f.create_task(conn, task_1)    
        userInput = (input("Choose another input: "))
    elif userInput == "5":
        print("You've selected delete project")
        userInput = (input("Choose another input: "))
    elif userInput == "6":
        print("You've selected delete a task")
        userInput = (input("Choose another input: "))
    else:
        print("Unknown command.")
        userInput = (input("Choose another input: "))

print("\n ## Thanks for using the Assignment Tracker! ## " + '\n')


# def main():
    # database = r"sqlitetut2.db"
    # conn = f.create_connection(database)
    # #create tables
    # if conn is not None:
    #     f.create_table(conn, f.sql_create_projects_table)
    #     f.create_table(conn, f.sql_create_tasks_table)

# main()

