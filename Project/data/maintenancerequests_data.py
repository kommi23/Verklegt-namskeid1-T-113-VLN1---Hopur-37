import csv
from Models.Maintenance_request import *

class MaintenanceRequestData:

    def add_maintenance(maintenance):
        try:
            with open("project/data/csv_files/maintenancerequests.csv", "a", newline='', encoding='utf-8') as csv_file:
                list_writer = csv.writer(csv_file)
                maintenance = Maintenance_request.turn_maintenance_request_into_list(maintenance)
                list_writer.writerow(maintenance)
                return True 
        except: raise
    print("kemst hingað")
    def get_maintenances():
        maintenances = []
        try:
            with open("project/data/csv_files/maintenancerequests.csv", "r", newline='', encoding='utf-8') as csv_file:
                csv_reader = csv.reader(csv_file)
                for line in csv_reader:
                    maintenances.append(Maintenance_request(*line))
            return maintenances
        except: raise

    def get_maintenancerequest_by_ID(ID):
        try:    
                maintenencerequests = []
                with open("Project/data/csv_files/maintenancerequests.csv", "r", newline='', encoding='utf-8') as csv_file:
                    for line in csv_file:
                        line = line.split(",")
                        if id in line[0]:
                            id.append(line)
                    return maintenencerequests
            
        except: raise  

    #Bæta við breyta verkbeiðni
