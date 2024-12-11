from ui.manager_ui import *
import os

class Mainmenu_UI:
    def display_menu():
                os.system("clear")

                print("\nMain Menu")
                print("1. Employee")
                print("2. Manager")
                print("3. Contractor")
                print("0. Exit")
                choice = input("Enter your choice: ")
                if choice == '1':
                     pass
                elif choice == '2':
                    Manager_ui.display_menu()
                elif choice == '3':
                     pass
                elif choice == '0':
                    pass