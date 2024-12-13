import csv
from Models.Employee import *


class EmployeeData:
    def __init__():
        pass

    def write_employe_data(employee):
        try:
            with open("Project/data/csv_files/employees.csv", "a", newline='', encoding='utf-8') as csv_file:
                list_writer = csv.writer(csv_file)
                employee_as_list = Employee.turn_employee_into_list(employee)
                list_writer.writerow(employee_as_list)
                return True 
        except: raise 
    
    def get_singular_employee_data(employee_id): 
        try:    
                with open("Project/data/csv_files/employees.csv", "r", newline='', encoding='utf-8') as csv_file:
                    for line in csv_file:
                        line = line.split(",")
                        if str(employee_id) in line[0]:
                            employee = Employee(*line)
                            return employee
        except: raise  
            
    def get_employees_data():
        employees = []
        try:
            with open("Project/data/csv_files/employees.csv", "r", newline='', encoding='utf-8') as csv_file:
                csv_reader = csv.reader(csv_file)
                
                for line in csv_reader:
                    employee = []
                    employee = Employee(*line)
                    employees.append(employee)
            return employees
        except: 
            raise ValueError("Shit no work")
        
    

    def get_employees_location_data(location: str) -> list: 
        try:    
                employees = []
                with open("Project/data/csv_files/employees.csv", "r", newline='', encoding='utf-8') as csv_file:
                    csv_reader = csv.reader(csv_file)
                    for line in csv_reader:
                        if location in line[-1]:
                            employee = Employee(*line)
                            employees.append(employee)
                    return employees
            
        except: raise  

    def delete_employee_data(Employee_id):   
        new_file = []
        try:
            with open("Project/data/csv_files/employees.csv", "r", newline='', encoding='utf-8') as csv_file:
                list_reader = csv.reader(csv_file)
                for row in list_reader:
                    if row[0]!= Employee_id:
                        new_file.append(row)
            
            with open("Project/data/csv_files/employees.csv", "w", newline='', encoding='utf-8') as new_csv_file:
                list_writer = csv.writer(new_csv_file)
                list_writer.writerows(new_file)
            return True
        except: raise




    def update_employee_data(Employee_id, updated_data, what_data: int): #breytti þannig "what_data" er sent til okkar og segir þá til um hvaða row verður f breytingum 
        new_file = []
        try:
            with open("Project/data/csv_files/employees.csv", "r", newline='', encoding='utf-8') as csv_file:
                list_reader = csv.reader(csv_file)
                for row in list_reader:
                    if row[0] == str(Employee_id): 
                        row[int(what_data)] = updated_data
                        
                    new_file.append(row)
            
            with open("Project/data/csv_files/employees.csv", "w", newline='', encoding='utf-8') as new_csv_file:
                list_writer = csv.writer(new_csv_file)
                list_writer.writerows(new_file)
            return True
        except: raise      


import csv
from Models.Employee import *
