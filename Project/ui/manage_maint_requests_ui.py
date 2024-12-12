import os
from logic.logic_wrapper import *
from Models.Maintenance_request import *

class Manage_maintenance_requests:
    def maint_requests_menu():
        os.system("clear")

        print("1. Display all Maintenance Requests")
        print("2. Add Maintenance Request")
        print("3. Update Maintenance Request")
        print("0. Go back")




    def add_maint_requests():
        fields = ["ID", "Property Number", "Description", "Priority", "Date", "Recurring Task" "Employee ID"]
        
        user_input = {}

        # Collecting input from the user for each field
        for field in fields:
            user_input[field] = input(f"Enter {field}: ")

        print("\nYou have entered the following details:")
        for field, value in user_input.items():
            print(f"{field}: {value}")

        confirmation = input("\nPress 1 to confirm, or any other key to cancel: ")

        if confirmation == "1":
            new_maint_request = Maintenance_Request(
                user_input["ID"], 
                user_input["Property Number"], 
                user_input["Description"], 
                user_input["Priority"], 
                user_input["Date"], 
                user_input["Total Cost"], 
                user_input["Recurring Task"], 
                user_input["Employee ID"]
            )

            # Call logic layer to add the maintenance request
            LL_maint_request.add_maint_request(new_maint_request)

            print("\nMaintenance request added successfully!")
        user_input = {}
        
        for i in user_input:

        print line
        if confirmation == 1:
            new_maint_request = Maintenance_Request(user_input["ID"], user_input["Property Number"], user_input["Description"], user_input["Priority"], user_input["Date"], user_input["Total Cost"], user_input["Recurring Task"], user_input["Employee ID"])
            LL_maint_request.add_maint_request(new_maint_request)
            
    def update_maint_requests():
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
        
            
            LL_maintenance_request.update_maint_requests(Id, new_info, info_list[info_change])
            print(f"Maintenance {info_change} updated successfully")