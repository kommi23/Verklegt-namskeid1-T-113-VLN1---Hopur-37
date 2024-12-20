import csv
from Models.Maintenance_request import Maintenance_request


class MaintenanceRequestData:
    def __init__(self):
        pass

    def add_maintenance(self, maintenance):
        try:
            with open("Project/data/csv_files/maintenances.csv", "a", newline='', encoding='utf-8') as csv_file:
                list_writer = csv.writer(csv_file)
                maintenance_as_list = Maintenance_request.turn_maintenance_request_into_list(maintenance)
                list_writer.writerow(maintenance_as_list)                
                return True 
        except: raise
        
    def get_maintenances(self):
        maintenances = []
        try:
            with open("Project/data/csv_files/maintenances.csv", "r", newline='', encoding='utf-8') as csv_file:
                csv_reader = csv.reader(csv_file)
                for line in csv_reader:
                    maintenence_request = Maintenance_request(*line) #We want to return a list og Model classes
                    maintenances.append(maintenence_request)
            return maintenances
        except: raise

    def get_maintenancerequest_by_ID(self,ID): #virkar svona
        try:    
                #maintenencerequests = []
                with open("Project/data/csv_files/maintenances.csv", "r", newline='', encoding='utf-8') as csv_file:

                    csv_reader = csv.reader(csv_file)
                    for line in csv_reader:
                        if ID in line[0]:
                            #maintenencerequests.append(line)
                            maintenance = Maintenance_request(*line)
                            return maintenance
            
        except: raise  

    def update_maintenancerequest_data(self,maintenance_id, updated_data,  what_data: int):
        new_file = []
        try:
            with open("Project/data/csv_files/maintenances.csv", "r", newline='', encoding='utf-8') as csv_file:
                list_reader = csv.reader(csv_file)
                for row in list_reader:
                    if row[0] == str(maintenance_id): 
                        row[int(what_data)] = updated_data
                        
                    new_file.append(row)
            
            with open("Project/data/csv_files/maintenances.csv", "w", newline='', encoding='utf-8') as new_csv_file:
                list_writer = csv.writer(new_csv_file)
                list_writer.writerows(new_file)
            return True
        except: raise      

    def add_maintenancereport_data(self,maintenance_id, employee_id, report):
        new_file = []
        try:
            with open("Project/data/csv_files/maintenances.csv", "r", newline='', encoding='utf-8') as csv_file:
                list_reader = csv.reader(csv_file)
                for row in list_reader:
                    if row[0] == str(maintenance_id): 
                        row[7] = employee_id
                        row[8] = report
                        row[9] = "Ready"
                    new_file.append(row)
            
            with open("Project/data/csv_files/maintenances.csv", "w", newline='', encoding='utf-8') as new_csv_file:
                list_writer = csv.writer(new_csv_file)
                list_writer.writerows(new_file)
            return True
        except: raise      


    def approve_maintenancereport_data(self,maintenance_id):
        new_file = []
        try:
            with open("Project/data/csv_files/maintenances.csv", "r", newline='', encoding='utf-8') as csv_file:
                list_reader = csv.reader(csv_file)
                for row in list_reader:
                    if row[0] == str(maintenance_id):    
                        row[int(9)] = "Closed"
                    new_file.append(row)
           
            with open("Project/data/csv_files/maintenances.csv", "w", newline='', encoding='utf-8') as new_csv_file:
                list_writer = csv.writer(new_csv_file)
                list_writer.writerows(new_file)
            return True
        except: raise      

    def get_maintenancereports_by_property(self,property): #EKKI NOTAÐ
        try:    
                with open("Project/data/csv_files/maintenances.csv", "r", newline='', encoding='utf-8') as csv_file:

                    csv_reader = csv.reader(csv_file)
                    for line in csv_reader:
                        if property in line[1]:
                            #maintenencerequests.append(line)
                            maintenance = Maintenance_request(*line)
                            return maintenance
            
        except: raise  

