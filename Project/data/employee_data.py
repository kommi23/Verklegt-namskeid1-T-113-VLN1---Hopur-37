import csv

class EmployeeData:
    def __init__(self):
        pass
    def add_employee(self, employee):
        try:
            with open("employees.csv", "a", newline='', encoding='utf-8') as csv_file:
                list_writer = csv.writer(csv_file)
                list_writer.writerow(employee)
                return True 
        except: raise 
            
    def get_employees():
        employees = []
        try:
            with open("Project/data/csv_files/employees.csv", "r", newline='', encoding='utf-8') as csv_file:
                csv_reader = csv.reader(csv_file)
                for line in csv_reader:
                    employees.append(line)
            return employees
        except: raise 
    def get_singular_employee(self): 
        try:    
                with open("Project/data/csv_files/employees.csv", "r", newline='', encoding='utf-8') as csv_file:
                    for line in csv_file:
                        line = line.split(",")
                        if self in line[0]:
                            return line
            
        except: raise  

    def delete_employee(Employee_id):   
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
