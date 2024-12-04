import csv

class EmployeeData:
    def __init__(self):
        pass
    def add_employee(self, employee):
        try:
            with open("employees.csv", "a", newline='', encoding='utf-8') as csv_file:
                csv_file.write(employee)
                return True 
        except:
            return None 
    def get_employees(self):
        employees = []
        try:
            with open("employees.csv", "r", newline='', encoding='utf-8') as csv_file:
                csv_reader = csv.reader(csv_file)
                for line in csv_reader:
                    employees.append(line)
            return employees
        except:
            return None
    def get_singular_employee(self, employee): 
        try:    
            with open("filefile.csv", "r", newline='', encoding='utf-8') as csv_file:
                for line in csv_file:
                    if employee in line:
                        return employee
        except: 
            return None 
                
class ProbertyData:
    def __init__(self):
        pass
    def add_property(self, proberty):
        try:
            with open("properties.csv", "a", newline='', encoding='utf-8') as csv_file:
                csv_file.write(proberty)
                return True
        except: return None
    def get_proberty(self):
        properties = []
        try:
            with open("properties.csv", newline='', encoding='utf-8') as csv_file:
                csv_reader = csv.reader(csv_file)

                for line in csv_reader:
                    properties.append(line)
            return properties
        except: return None

class LocationData:
    def __init__(self):
        pass
    def get_locations(self):
        locations = []
        try:
            with open("locations.csv", "r", newline='', encoding='utf-8') as csv_file:
                csv_reader = csv.reader(csv_file)
                for line in csv_reader:
                    locations.append(line)
            return locations
        except: return None

class MaintenanceData:
    def __init__(self):
        pass
    def add_maintenance(self, maintenance):
        try:
            with open("maintenances.csv", "a", newline='', encoding='utf-8') as csv_file:
                csv_file.write(maintenance)
                return True 
        except: return None
    def get_maintenences(self):
        maintenances = []
        try:
            with open("maintenances.csv", "r", newline='', encoding='utf-8') as csv_file:
                csv_reader = csv.reader(csv_file)
                for line in csv_reader:
                    maintenances.append(line)
            return maintenances
        except: return None

class MaintenanceReportData:
    def __init__(self):
        pass
    def add_maintenancereport(self, maintenancereport):
        try:
            with open("maintenancereports.csv", "a") as csv_file:
                csv_file.write(maintenancereport) 
                return True
        except: return None        
    def get_maintenanreport(self):
        try:
            with open("maintenancereports.csv", "r", newline='', encoding='utf-8') as csv_file:
                maintenancereports = []
                csv_reader = csv.reader(csv_file)
                for line in csv_reader:
                    maintenancereports.append(line)
            return maintenancereports
        except: return None 
class ContractorReport:
    def __init__(self):
        pass
    def add_contractoreports(self, contractorreport):
        try:
            with open("contractorreports.csv", "a", newline='', encoding='utf-8') as csv_file:
                csv_file.write(contractorreport)
                return True
        except: return None
    def get_contractorReports(self):
        contractorreports = []
        try:
            with open("contractorreports.csv", "r", newline='', encoding='utf-8') as csv_file:
                contractorreports = []
                csv_reader = csv.reader(csv_file)
                for line in csv_reader:
                    contractorreports.append(line)
            return contractorreports      
        except: return None 
        