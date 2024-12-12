
class Manage_properties():
    def display_menu():
        os.system("clear")
        
        print("1. Create new property")
        print("2. Search property by location")
        print("3. Search property by condition")
        print("4. List all properties")
        print("0. Go back")

        choice = int(input())

        if choice == 1:
            add_property()
            pass
        if choice == 2:
            list_properties_by_location()
        if choice == 3: 
            pass
        if choice == 4:
            list_proberties()
           

def list_proberties():
    properties = []
    properties = LL_property.get_all_proberties_LL()
            
    if not properties:
        print("No properties found.")

    else:
        for i in properties:
            print(i)

def list_properties_by_location():
    
    os.system("clear")
    
    print("1. Properties in Reykjavík")
    print("2. Properties in Nuuk")
    print("3. Properties in Kulusuk")
    print("4. Properties in Þórshöfn")
    print("5. Properties in Tingwall")
    print("6. Properties in Þórshöfn")
    print("0. Go back")

    location_search = int(input())
    
    valid_locations = {
        1: "Reykjavík",
        2: "Nuuk",
        3: "Kulusuk",
        4: "Þórshöfn",
        5: "Tingwall",
        6: "Þórshöfn"
    }
    if location_search in valid_locations:
        location = valid_locations[location_search]
        properties = LL_property.get_properties_by_location_data_LL(location)
        for i in properties:
            print(i)
    elif location == 0:
        pass # go back 
    else: 
        print("invalid input")

  
       



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

import os
from logic.logic_wrapper import * 