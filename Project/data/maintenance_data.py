import csv

class MaintenanceData:
    def __init__(self):
        pass
    def add_maintenance(self, maintenance):
        try:
            with open("maintenances.csv", "a") as csv_file:
                csv_file.write(maintenance)
                return True 
        except: return None
    def get_maintenences(self):
        maintenances = []
        try:
            with open("maintenances.csv", "r") as csv_file:
                csv_reader = csv.reader(csv_file)
                for line in csv_reader:
                    maintenances.append(line)
            return maintenances
        except: return None