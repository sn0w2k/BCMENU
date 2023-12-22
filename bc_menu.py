from termcolor import colored
from pyfiglet import figlet_format
import webbrowser
'''
PLEASE CREDIT SN0W2K FOR MAKING BCMENU!
..OR DON'T..
FOLLOW ME ON GITHUB
'''
print((colored(figlet_format("BC MENU"), color="red")))
def menu():
    option_select = False
    print("1 - Google \n 2 - Youtube \n 3 - Github \n 4 - Exit")
    option = input("\n TYPE OPTION NUMBER: ")
#LAUNCH GOOGLE:
    if option == "1":
        option_select = True
        print("Loading Google...")
        webbrowser.open("https://www.google.com/")
        if True:
            print("Load Successful.")
            quit()
        if False:
            print("Load Failed. \n Try Again...")
            quit()
#LAUNCH YOUTUBE:
    if option == "2":
        option_select = True
        print("Loading Youtube...")
        webbrowser.open("https://www.youtube.com/")
        if True:
            print("Load Successful.")
            quit()
        if False:
            print("Load Failed. \n Try Again...")
            quit()
#LAUNCH GITHUB:
    if option == "3":
        option_select = True
        print("Loading Github...")
        webbrowser.open("https://www.github.com/")
        if True:
            print("Load Successful.")
            quit()
        if False:
            print("Load Failed. \n Try Again...")
            quit()
#QUIT PROGRAM:
    if option == "4":
        option_select = True
        print("Exiting Program... \n Thanks for using BC MENU")
        quit()
#IF NOT OPTION IS SELECTED:
    if option_select == False:
        print("No option selected.")
    while option_select == False:
        menu()
menu()
