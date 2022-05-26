import secrets
import string
from func import *

while quit != "q":

    menu = input("\n select operation:\n" + "1. new\n" + "2. open\n"+ "3. purge\n ")

    if(menu == "new"):
        generator()
        default_save()
        exit_message()   
    elif(menu == "open"):
        open_file()
        exit_message()
    elif(menu == "purge"):
        print("//WARNING// Your all saved Passes are going to delete.")
        response = input("\n(y or n)- ")
        if (response == "y" or "yes"):
            purge()
            print("Task completed!")
    else:
        print("invalid response\n")
    quit = input("Type q to quit.")