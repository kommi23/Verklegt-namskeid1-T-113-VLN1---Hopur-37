import os

class Manage_contractors:
    def display_menu():
        os.system("clear")

        print("1. Create new Contractor")
        print("2. Change Contractors")
        
        choice = input("Enter your choice: ")

        if choice == 1:
            add_contractor()



def add_contractor():
    pass