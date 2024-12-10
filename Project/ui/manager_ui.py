class manage_employees:
    def display_manage_employee_ui():
        print("1. Create new employee")
        print("2. Search for employee")
        print("3. Change employee")
        choice = input("Enter your choice:")

        if choice == 1:
            pass

class manage_employees_submenus:
    def create_new_employee_submenu():
        fields = ["ID:", "Name:", "SSN:", "Address:","GSM:", "Email:", "Location:"]
        user_inputs = {}
        
        for field in fields:
            os.clear_console()

            for key, value in user_inputs.items:
                print(f"{key}: {value}")
            
            print(f"{field}: ", end="")
            user_inputs[field] = input()
        
        os.clear_console
        for key, value in user_inputs:
            print(f"{key}: {value}")

        print("Press 1. to confirm that the information is right: ")
        confirmation = input()

        if confirmation == 1:
            new_employee = Employee(user_inputs["ID:"], user_inputs["Name:"], user_inputs["SSN:"], user_inputs["Address:"],user_inputs["GSM:"], user_inputs["Email:"], user_inputs["Location:"])
            logic_wrapper.add_employee(new_employee)
            

import os
from logic.logic_wrapper import *
from Models.Employee import *