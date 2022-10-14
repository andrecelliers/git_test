#!usr/bin/python3


"""
Create a dictionary of at least 10 programming terms. Ask the user to input a term, then show the definition as well as open
a Wikipedia article for the associated term. If the term is not known, tell the user, and suggest terms they may be interested in learning instead.
Accept repeated user input until they quit. 

When you run the program it should have a welcome section and be nicely formatted. When ran from the terminal it should open a seperate website
example:  firefox https:wikipedia.strings & 
Look up sleep function to delay firefox opening. 

[Each term its own glossary?]
[Provide user a list of terms]
[yes/no to open webpage]
[Provide a list of known terms]
[split glossary into multiple dictionaries]
[use a list to reference glossary]
Use one for loop. One while loop. One if else statement.

##### PLACEHOLDER WEBSITE IF STATEMENT #######

userYesNo = input("\n Would you like to know more? [yes/no]" + "\n")
        if userYesNo == 'yes':
            webbrowser.open('https://www.google.com/')

"""

###Introduction Statement###

import webbrowser


print("\n### Programming Language Glossary ###\n" + "\nHere are some terms that I know: " + "\n" +
"\n\t- String" + "\n\t- Int" + "\n\t- Dictionary" + "\n\t- Cast" + "\n\t- For loop" + '\n')



###Glossary containing definitions###

glossary = {
    'string'        :'Data type in python consisting of a sequence of characters.',
    'int'           :'Data type in python consisting of a whole numerical value.',
    'dictionary'    :'Data structure in python used to store both keys and values.',
    'concatenate'   :'To join two or more strings together to create a new string.',
    'list'          :'Data type used to store a collection of data.',
    'cast'          :'Definition of cast.',
    'for loop'      :'Defintion of for loop.',
    'while loop'    :'Definition of while loop.',
    'if loop'       :'Definition of if loop.',
    'tuple'         :'A collection of data similar to a list, but a tuple can not be changed once declared.'
}

url = {
    'string': 'https://en.wikipedia.org/wiki/String_(computer_science)',
    'int': 'https://en.wikipedia.org/wiki/Integer_(computer_science)', 
    'dictionary'    :'https://en.wikipedia.org/wiki/Associative_array',
    'concatenate'   :'https://en.wikipedia.org/wiki/Concatenation',
    'list'          :'https://en.wikipedia.org/wiki/List_(abstract_data_type)',
    'cast'          :'https://en.wikipedia.org/wiki/Type_conversion',
    'for loop'      :'https://en.wikipedia.org/wiki/For_loop',
    'while loop'    :'https://en.wikipedia.org/wiki/While_loop',
    'if loop'       :'https://en.wikipedia.org/wiki/Conditional_(computer_programming)#If%E2%80%93then(%E2%80%93else)',
    'tuple'         :'https://en.wikipedia.org/wiki/Tuple'
}


###Asks the user for a definition### 

userInput = input("Enter the term you would like to know the definition of, when finished enter 'end':").lower().strip()



###This while loop will continue prompting the user for definitions until they enter 'end'. The if statement will print the corresponding definition if it's in the glossary###
while userInput != 'end':
    if userInput in glossary:
        print("\nHere is the definition of " + userInput + "! " + "\n\t" + glossary[userInput])
        userYesNo = input("\n Would you like to know more about " + userInput + "? [yes/no]" + "\n")
        if userYesNo == 'yes':
            webbrowser.open(url[userInput])
        userInput = input("\nWhat else would you like to know? Enter 'end' when finished: ").lower().strip()       
    else:
        print("\nSorry, my programmer didn't provide me with the definition of " + userInput + ". ")
        userYesNo = input("\n Would you like to google that? [yes/no]" + "\n")
        if userYesNo == 'yes':
            webbrowser.open('www.google.com')
        userInput = input("\nWhat else would you like to know? Enter 'end' when finished: ").lower().strip()



#Closing statement
print('\n ### I hope you learned something useful today! ###')











