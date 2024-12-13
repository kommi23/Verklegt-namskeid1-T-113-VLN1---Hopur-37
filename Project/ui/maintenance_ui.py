
from logic.logic_wrapper import *
from Models.Maintenance_request import *

class Maintenance_UI:
    def display_menu():
        

        print("\n=== Maintenance Menu ===")
        print("1. Manager")
        print("2. Employee")
        print("0. Go back")

        choice = (input("Enter your choice: "))
        valid_choices = ["1", "2" , "0"]

        if choice not in valid_choices:
            print("Please enter a valid choice: ")
            return
        elif choice == '1':
            Maintenance_UI.manager_maintenance_requests_menu()
        
        elif choice == '2':
            pass


    


    def manager_maintenance_requests_menu():

        print("1. Display all Maintenance Requests")
        print("2. Add Maintenance Request")
        print("3. Update Maintenance Request")
        print("0. Go back")

        choice = (input("Enter your choice: "))
        valid_choices = ["1", "2", "3", "0"]

        if choice not in valid_choices:
            print("Please enter a valid choice: ")
            return
        elif choice == '1':
            display_all_maintenance_requests()
        elif choice == '2':
            add_maintenance_requests()




            
def add_maintenance_requests():
    print("\n=== Add New Maintenance Request ===")
    fields = ["Id","Property Number","Description","Priority","Date","Budget","Recurring Task","Employee ID"]
    user_input = {}

    
    for field in fields:
        user_input[field] = input(f"Enter Maintenance Request {field}: ")

    
    print("\nYou have entered the following details:")
    for key, value in user_input.items():
        print(f"{key}: {value}")

    
    confirmation = input("\nPress 1 to confirm or any other key to cancel: ")

    if confirmation == "1":
        
            new_maintenance = Maintenance_request(
                user_input["Id"],
                user_input["Property Number"],
                user_input["Description"],
                user_input["Priority"],
                user_input["Date"],
                user_input["Budget"],
                user_input["Recurring Task"],
                user_input["Employee ID"]
            )

            Maintenance_request_logic.add_maintenance_request_logic(new_maintenance)
            print("\nMaintenance request added successfully!")
    else:
         print("Something went worng")    

def display_all_maintenance_requests():
        requests = LW_maintenance_request.get_all_maintenance_requests_lw()
        if not requests:
            print("\nNo maintenance requests found.")
            return

        print("\nAll Maintenance Requests:")
        for request in requests:
            print(request)

            
def update_maintenance_requests():
        id = input("Enter Maintenance Number: ")
        info_change = input("Enter what information to change (e.g, Property Number, Date): ").lower()
        new_info = input("Enter new information: ")

        info_list = { 
            
            "id": 1, 
            "property": 2,
            "description": 3,
            "priority": 4,
            "date": 5,
            "recurrin_task": 6,
            "employee_id": 7
        }

        print(info_list[info_change])

        if info_change not in info_list:
            print("Information not found")
            return
        
            
            LW_maintenance_request.update_maint_requests(Id, new_info, info_list[info_change])
            print(f"Maintenance {info_change} updated successfully")