
class Manage_properties():
    def display_menu():
        os.system("clear")
        
        print("1. Create new property")
        print("2. Search property by location")
        print("3. Update property")
        print("4. List all properties")
        print("0. Go back")

        choice = int(input())

        if choice == 1:
            add_property()
        if choice == 2:
            pass
        if choice == 3: 
            update_property_information()
        if choice == 4:
            list_properties()
           

def list_properties():
    properties = []
    properties = LL_property.get_all_proberties_LL()
            
    if not properties:
        print("No properties found.")

    else:
        for i in properties:
            print(i)


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


def update_property_information():
    id = int(input("Enter the ID of the property you want to update: "))
    info_change = input("Do you want to change condition or maintenance: ").lower()
    new_info = input(f"What is the new {info_change}: ")

    info_list = {
        "condition" :1,
        "maintenance" : 2
    }

    if info_change not in info_list:
        print(f"Error: information not found")

    LL_property.change_property_lw(id, new_info, info_list[info_change])

import os
from Models.Property import *
from ui.manager_ui import *

import os
from logic.logic_wrapper import * 