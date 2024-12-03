import csv

class EmployeeData:
    def __init__(self):
        pass
    def add_employee(self, employee):
        with open("employees.csv", "a") as csv_file:
            csv_file.write(employee)
    def get_employees(self):
        employees = []
        with open("employees.csv", "r") as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                employees.append(line)
            return employees
        
class ProbertyData:
    def __init__(self):
        pass
    def add_property(self, proberty):
        with open("properties.csv", "a") as csv_file:
            csv_file.write(proberty)
    def get_proberty(self):
        properties = []
        with open("properties.csv") as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                properties.append(line)
        return properties

class LocationData:
    def __init__(self):
        pass
    def get_locations(self):
        locations = []
        with open("locations.csv", "r") as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                locations.append(line)
        return locations

class MaintenanceData:
    def __init__(self):
        pass
    def add_maintenance(self, maintenance):
        with open("maintenances.csv", "a") as csv_file:
            csv_file.write(maintenance)
    def get_maintenences(self):
        maintenances = []
        with open("maintenances.csv", "r") as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                maintenances.append(line)
        return maintenances

class MaintenanceReportData:
    def __init__(self):
        pass
    def add_maintenancereport(self, maintenancereport):
        with open("maintenancereports.csv", "a") as csv_file:
            csv_file.write(maintenancereport)        
    def get_maintenanreport(self):
        with open("maintenancereports.csv", "r") as csv_file:
            maintenancereports = []
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                maintenancereports.append(line)
        return maintenancereports

class ContractorReport:
    def __init__(self):
        pass
    def add_contractoreports(self, contractorreport):
        with open("contractorreports.csv", "a") as csv_file:
            csv_file.write(contractorreport)
    def get_contractorReports(self):
        contractorreports = []
        with open("contractorreports.csv", "r") as csv_file:
            contractorreports = []
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                contractorreports.append(line)
        return contractorreports      