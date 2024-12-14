import os
from Models.Property import * 
from logic.logic_wrapper import LogicWrapper


class Manage_properties():
    def __init__(self, llw: LogicWrapper):
        self.llw : LogicWrapper= llw

    def display_menu(self):        
        while True:
            print("\n=== Property Menu ===")
            print("1. Create new property")
            print("2. Search property by location")
            print("3. Update property")
            print("4. List all properties")
            print("0. Go back")
            #print("--Press any other button for Main Menu--")

            choice = (input())

            if choice == "1":
                add_property(self)
            if choice == "2":
                list_properties_by_location(self)
            if choice == "3": 
                update_property_information(self)
            if choice == "4":
                list_properties(self)                  
            if choice == "0":
                return
            else: 
                input("incorrect input, try again..")
            

def list_properties(self):
        properties = []
        properties = self.llw.get_all_properties_lw()
                
        if not properties:
            print("No properties found")
        else:
            for i in properties:
                print(i)
        
        return

def list_properties_by_location(self):    
    while True:
        allLocations = []
        allLocations = self.llw.list_all_locations()

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
                return
        except ValueError: 
            smu = input("Please entert a valid input or 0 for back") 
            if smu == 0: 
                return

        selected = None
        opt = int(location_search)
    
        try: # var upprunulega með:  if opt > len(allLocations): return "blabla", en það náði ekki að catch-a error við stress test
            selected = allLocations[opt]
            properties = self.llw.get_properties_by_location_data_LL(selected.location.strip())

            if len(properties) == 0:

                print("No properties found for this location: ", selected.location)
            for i in properties:
                    print(i)    
            return
        except: 
            input("Please select a valid location")
            
       

def add_property(self):
    print("ID:")

    fields = ["ID", "Condition", "Additional maintenance", "Location"]
    user_inputs = {}
    
    for field in fields:
        os.system("clear")

        for key, value in user_inputs.items():
            print(f"{key}: {value}")
        
        
        user_inputs[field] = input(f"Enter Property {field}: ")
    
    
    for key, value in user_inputs.items():
        print(f"{key}: {value}")
        
    confirmation = (input("Press 1. to confirm that the information is right: "))

    try:
        confirmation_int = int(confirmation)
    except:
        print("Employee was not added")
        return 
    
    if confirmation_int == 1: 
        ("1")
        new_property = Property(user_inputs["ID"], user_inputs["Condition"], user_inputs["Additional maintenance"], user_inputs["Location"])
        LogicWrapper.add_property_lw(new_property)
        return
    else:
        print("Employee not added")
        return 

def update_property_information(self):
    id = input("Enter the ID of the property you want to update: ")
    info_change = input("Do you want to change condition or maintenance: ").lower()
    new_info = input(f"What is the new {info_change}: ")

    info_list = {
        "condition" :1,
        "maintenance" : 2
    }
    if info_change not in info_list:
        print(f"Error: information {info_change} not found")
        return 
    else:
        print("\nYou have entered the following details:")
        print(f"ID: {id}")
        print(f"{info_change}: {new_info} ")

        try:
            confirmation = int(input("Press 1. to confirm that the information is right: "))
            if confirmation == 1:
                LogicWrapper.change_property_lw(info_list[info_change])
                return 
        except:
            print("Property information not changed")
            return 
        

 
    

