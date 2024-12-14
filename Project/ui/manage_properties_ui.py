import os
from Models.Property import * 
from ui.manager_ui import *
import os
from logic.logic_wrapper import * 


class Manage_properties():
    def display_menu():        
        print("\n=== Property Menu ===")
        print("1. Create new property")
        print("2. Search property by location")
        print("3. Update property")
        print("4. List all properties")
        print("0. Go back")

        choice = (input())

        if choice == "1":
            add_property()
        if choice == "2":
            list_properties_by_location()
        if choice == "3": 
            update_property_information()
        if choice == "4":
            list_properties()                  
        if choice == "0":
            Manager_ui.display_menu()
        else: 
            print("Please choose a valid input!")
            Manage_properties.display_menu()

def list_properties():
        properties = []
        properties = LL_property.get_all_properties_lw()
                
        if not properties:
            print("No properties found")
        else:
            for i in properties:
                print(i)
        
        return Manage_properties.display_menu()

def list_properties_by_location():    
    allLocations = []
    allLocations = LL_location.list_all_locations()

    count : int = 0
    for loc in allLocations:
        if count == 0:
            pass
        else: 
            print ("    ", str(count), ") " , loc.location)
        
        count = count +1
    print ("     0 )  Go back")

    try:
        location_search = int(input())
        if location_search == 0: 
        # Go back 
            return Manage_properties.display_menu()
    except ValueError: 
        print("Please entert a valid input") 
        return list_properties_by_location()

    selected = None
    opt = int(location_search)
    
    try: # var upprunulega með:  if opt > len(allLocations): return "blabla", en það náði ekki að catch-a error við stress test
            selected = allLocations[opt]
            properties = LL_property.get_properties_by_location_data_LL(selected.location.strip())

            if len(properties) == 0:

                print("No properties found for this location: ", selected.location)
            for i in properties:
                    print(i)    
            Manage_properties.display_menu()
    except: 
        print("Please select a valid location")
        return list_properties_by_location()
       

def add_property():
    list_of_locations = ["Nuuk", "Kulusuk", "Þórshöfn", "Tingwall", "Reykjavik"]
    list_of_conditions = ["good", "fair", "bad"]
    id = None
    condition = None
    additional = None
    location = None

    while id == None or not id.isnumeric():
        id = input("ID: ")
        if not id.isnumeric():
            print("Please enter a valid ID!")
    
    while condition == None or condition not in list_of_conditions:
        print(list_of_conditions)
        condition = input("Condition: ")
        condition = condition.lower()
        if condition not in list_of_conditions:
            print("Please set condition as good, fair or bad")

    while additional == None:
        additional = input("Additional Maintenance: ")

    while location == None or location not in list_of_locations:
        location = input("Location: ")
        if location not in list_of_locations:
            print("Not a valid location, please select one of: Nuuk, Kulusuk, Þórshöfn, Tingwall or Reykjavik")

    print(f"ID: {id}")
    print(f"Condition: {condition}")
    print(f"Additional maintenance: {additional}")
    print(f"Location: {location}")
    print("Press 1. to confirm that the information is right, press anything else to restart: ")
    confirmation = str(input())    

    if confirmation == "1": 
        new_property = Property(id, condition, additional, location)
        LL_property.add_property_lw(new_property)
        return Manage_properties.display_menu()
    else:
        print("Employee not added")
        return Manage_properties.display_menu()

def update_property_information():
    id = input("Enter the ID of the property you want to update: ")
    info_change = input("Do you want to change condition or maintenance: ").lower()
    new_info = input(f"What is the new {info_change}: ")

    info_list = {
        "condition" :1,
        "maintenance" : 2
    }
    if info_change not in info_list:
        print(f"Error: information {info_change} not found")
        return Manage_properties.display_menu()
    else:
        print("\nYou have entered the following details:")
        print(f"ID: {id}")
        print(f"{info_change}: {new_info} ")

        print("Press 1. to confirm that the information is right: ")

        try:
            confirmation = int(input())
            if confirmation == 1:
                LL_property.change_property_lw(id, new_info, info_list[info_change])
                return Manage_properties.display_menu()
        except:
            print("Property information not changed")
            return Manage_properties.display_menu()
        

 
    

