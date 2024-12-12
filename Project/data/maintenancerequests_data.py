import csv

class MaintenanceRequestData:
    def add_maintenance(maintenance):
        try:
            with open("maintenancerequest.csv", "a", newline='', encoding='utf-8') as csv_file:
                csv_file.write(maintenance)
                return True 
        except: raise
    print("kemst hingað")
    def get_maintenances():
        maintenances = []
        try:
            with open("maintenancerequests.csv", "r", newline='', encoding='utf-8') as csv_file:
                csv_reader = csv.reader(csv_file)
                for line in csv_reader:
                    maintenances.append(line)
            return maintenances
        except: raise

    def get_maintenancerequest_by_ID(ID):
        try:    
                maintenencerequests = []
                with open("Project/data/csv_files/maintenancerequests.csv", "r", newline='', encoding='utf-8') as csv_file:
                    for line in csv_file:
                        line = line.split(",")
                        if ID in line[0]:
                            ID.append(line)
                    return maintenencerequests
            
        except: raise  

    #Bæta við breyta verkbeiðni
