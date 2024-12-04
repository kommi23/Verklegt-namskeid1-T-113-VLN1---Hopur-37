import csv

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
            with open("maintenancereports.csv", "r") as csv_file:
                maintenancereports = []
                csv_reader = csv.reader(csv_file)
                for line in csv_reader:
                    maintenancereports.append(line)
            return maintenancereports
        except: return None 