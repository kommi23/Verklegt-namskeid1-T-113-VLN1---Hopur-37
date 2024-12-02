import csv

class EmployeeData:
    def init(self):
        pass
    def add_employee(self, employee):
        with open("employees.csv", "a") as csv_file:
            csv_file.write(employee)
    def get_employees(self):
        with open("employees.csv", "r") as csv_file:
            csv_reader = csv.reader(csv_file)
            return csv_reader
        
class ProbertyData:
    def init(self):
        self.proberties = []
    def add_property(self, proberty):
        self.proberties.append(proberty)
    def get_proberty(self):
        return self.proberties

class LocationData:
    def init(self):
        self.locations = []
    def get_locations(self):
        return self.locations

class MaintenanceData:
    def init(self):
        self.maintenances = []
    def add_maintenance(self, maintenance):
        self.maintenances.append(maintenance)
    def get_maintenences(self):
        return self.maintenances

class MaintenanceReportData:
    def init(self):
        self.maintenancereport = []
    def add_maintenancereport(self, maintenancereport):
        self.maintenancereport.append(maintenancereport)
    def get_maintenanreport(self):
        return self.maintenancereport

class ContractorReport:
    def init(self):
        self.ContractorReports = []
    def add_contractoreports(self, contractorreport):
        self.ContractorReports.append(contractorreport)
    def get_contractorReports(self):
        return self.add_contractoreports