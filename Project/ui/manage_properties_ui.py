
class Manage_properties():
    def display_menu():
        os.system("clear")
        
        print("1. Create new property")
        print("2. Search for property")
        print("3. Change property")
        print("4. List all properties")
        print("0. Go back")

        choice = int(input())

        if choice == 1:
            add_property()

def add_property():
    fields = ["ID", "Condition", "Additional maintenance", "Location"]
    user_inputs = {}
    
    for field in fields:
        os.system("clear")

        for key, value in user_inputs.items():
            print(f"{key}: {value}")
        
        print(f"{field}: ", end="")
        user_inputs[field] = input()
    
    os.system("clear")
    for key, value in user_inputs.items():
        print(f"{key}: {value}")

    print("Press 1. to confirm that the information is right: ")
    confirmation = int(input())

    if confirmation == 1:
        new_property = Property(user_inputs["ID"], user_inputs["Condition"], user_inputs["Additional maintenance"], user_inputs["Location"])
        LL_property.add_property(new_property)


import os
from Models.Property import *
from ui.manager_ui import *
from logic.logic_wrapper import * 