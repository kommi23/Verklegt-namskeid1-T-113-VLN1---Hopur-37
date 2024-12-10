from ui.manager_menu import *
import os

class Mainmenu_UI:
    def display_menu():
                os.system("clear")

                print("\nMain Menu")
                print("1. Employee")
                print("2. Manager")
                print("4. Contractor")
                print("0. Exit")
                choice = input("Enter your choice: ")
                if choice == '1':
                     pass
                    #EmployeeMenuUI()
                elif choice == '2':
                    ManagerUI.manager_menu()
                elif choice == '3':
                     pass
                elif choice == '0':
                    pass