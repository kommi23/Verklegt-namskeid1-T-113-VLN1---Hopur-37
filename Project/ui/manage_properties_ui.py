import os
<<<<<<< HEAD
from logic.logic_wrapper import * 
=======
from Models.Property import *
from ui.manager_ui import *

import os
from logic.logic_wrapper import * 

>>>>>>> main

class Manage_properties():
    def display_menu():
        os.system("Clear")
        
        print("1. Create new property")
        print("2. Search property by location")
        print("3. Update property")
        print("4. List all properties")
        print("0. Go back")

        choice = int(input())
        valid_choices = [1, 2, 3, 4, 0]

        if choice not in valid_choices:
            print("Please enter a valid choice!: ")
            I_understand = None
            I_understand = input("Enter anything to continue")
            if I_understand != None:
                Manage_properties.display_menu()

        if choice == 1:
            pass

        if choice == 2:
            list_properties_by_location()

        if choice == 3: 
            update_property_information()

        if choice == 4:

            list_proberties()
     # end def

    def list_properties():
        properties = []
        properties = LL_property.get_all_properties_lw()
                
        if not properties:
            print("No properties found)
                  
      """
            list_properties()
<<<<<<< Updated upstream

        if choice == 0:
            Manager_ui.display_menu()
           
"""

<<<<<<< HEAD
def list_properties():
    properties = []
    properties = LL_property.get_all_proberties_LL()
=======
     # end def

def list_properties():
        properties = []
        properties = LL_property.get_all_properties_lw()
                
        if not properties:
            print("No properties found")
                  

=======
>>>>>>> main
        else:
            for i in properties:
                print(i)

<<<<<<< HEAD
def list_properties_by_location():
=======
    def list_properties_by_location():
>>>>>>> main
        
        os.system("clear")
        
        allLocations = []
        allLocations = LL_location.list_all_locations()

        count : int = 0
        for loc in allLocations:
            if count == 0:
                pass
            else: 
                print ("    ", str(count), ") " , loc.location)
<<<<<<< HEAD
>>>>>>> Stashed changes
=======
>>>>>>> main
            
            count = count +1
        # end for 
        print ("    0) to Go back")
        

<<<<<<< HEAD
<<<<<<< Updated upstream
    else:
=======
=======
>>>>>>> main

        location_search = int(input())
        opt = int(location_search)
        selected = None
        if opt == 0: 
            # Go back 
            return
        elif opt > len(allLocations):
            # out of bounds of the array
            print("WTF!! ")
        else:
            selected = allLocations[opt]

        properties = LL_property.get_properties_by_location_data_LL(selected.location.strip())
    
        if len(properties) == 0:
<<<<<<< HEAD
            print("No properties found for this location: ", selected.location)
>>>>>>> Stashed changes
=======
            print("No properties found for this locatio: ", selected.location)
>>>>>>> main
        for i in properties:
                print(i)    
        

"""
    def add_property():
        fields = ["ID", "Condition", "Additional maintenance", "Location"]
        user_inputs = {}
        
        for field in fields:
            os.system("clear")

            for key, value in user_inputs.items():
                print(f"{key}: {value}")
            
            print(f"{field}: ", end="")
            user_inputs[field] = input()
       

def add_property():

    
    fields = ["ID", "Condition", "Additional maintenance", "Location"]
    user_inputs = {}
    
    for field in fields:

        os.system("clear")
        for key, value in user_inputs.items():
            print(f"{key}: {value}")

        print("Press 1. to confirm that the information is right: ")
        confirmation = int(input())

        if confirmation == 1:
            new_property = Property(user_inputs["ID"], user_inputs["Condition"], user_inputs["Additional maintenance"], user_inputs["Location"])
            LL_property.add_property(new_property)

<<<<<<< HEAD
<<<<<<< Updated upstream
=======
"""
def update_property_information():
        id = int(input("Enter the ID of the property you want to update: "))
        info_change = input("Do you want to change condition or maintenance: ").lower()
        new_info = input(f"What is the new {info_change}: ")
>>>>>>> Stashed changes
=======
"""
    def update_property_information():
        id = int(input("Enter the ID of the property you want to update: "))
        info_change = input("Do you want to change condition or maintenance: ").lower()
        new_info = input(f"What is the new {info_change}: ")
>>>>>>> main

        info_list = {
            "condition" :1,
            "maintenance" : 2
        }

        if info_change not in info_list:
            print(f"Error: information not found")

        LL_property.change_property_lw(id, new_info, info_list[info_change])

<<<<<<< HEAD
    LL_property.change_property_lw(id, new_info, info_list[info_change])

import os
from Models.Property import *
from ui.manager_ui import *

=======
>>>>>>> main
