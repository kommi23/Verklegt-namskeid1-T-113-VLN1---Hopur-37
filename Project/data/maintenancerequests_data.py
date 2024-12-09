import csv

class MaintenanceData:
    def __init__():
        pass
    def add_maintenance(maintenance):
        try:
            with open("maintenances.csv", "a", newline='', encoding='utf-8') as csv_file:
                csv_file.write(maintenance)
                return True 
        except: raise
    def get_maintenences():
        maintenances = []
        try:
            with open("maintenances.csv", "r", newline='', encoding='utf-8') as csv_file:
                csv_reader = csv.reader(csv_file)
                for line in csv_reader:
                    maintenances.append(line)
            return maintenances
        except: raise