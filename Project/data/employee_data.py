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
            
    def get_employees(self):
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