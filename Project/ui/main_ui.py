
class Mainmenu_ui:
    def display_menu():
                os.system("clear")

                print("\nMain Menu")
                print("1. Employee")
                print("2. Manager")
                print("0. Exit")

                choice = input("Enter your choice: ")
                valid_choices = ["1","2","0"]

                if choice not in valid_choices:
                    print("Please enter a valid choice!")
                    I_understand = None
                    I_understand = input("Enter anything to continue")
                    if I_understand != None:
                        Mainmenu_ui.display_menu()

                if choice == '1':
                    Employee_ui.display_menu()
                elif choice == '2':
                    Manager_ui.display_menu()
                elif choice == '0':
                    quit()


from ui.manager_ui import *
from ui.employee_ui import *
import os