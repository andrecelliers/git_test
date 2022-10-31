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

userInput = int(input("Choose an input: "))

while userInput != 7:
    if userInput == 1:
        print("You've selected view all projects")
        userInput = int(input("Choose an input: "))
    if userInput == 2:
        print("You've selected view all tasks")
        userInput = int(input("Choose an input: "))
    if userInput == 3:
        print("You've selected create new project")
        userInput = int(input("Choose an input: "))
    if userInput == 4:
        print("You've selected create new task")
        userInput = int(input("Choose an input: "))
    if userInput == 5:
        print("You've selected delete project")
        userInput = int(input("Choose an input: "))
    if userInput == 6:
        print("You've selected delete a task")
        userInput = int(input("Choose an input: "))
    else:
        print("Unknown command.")
        userInput = int(input("Choose an input: "))

print("\n ## Thanks for using the Assignment Tracker! ## " + '\n')

