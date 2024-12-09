import csv

class MaintenanceRequ:
    def __init__():
        pass

    def add_maintenance(maintenance):
        try:
            with open("maintenances.csv", "a", newline='', encoding='utf-8') as csv_file:
                csv_file.write(maintenance)
                return True 
        except: raise

    def get_maintenances():
        maintenances = []
        try:
            with open("maintenances.csv", "r", newline='', encoding='utf-8') as csv_file:
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

    def get_maintenancerequest_by_property_number(property_number):
        try:    
                maintenencerequests = []
                with open("Project/data/csv_files/maintenancerequests.csv", "r", newline='', encoding='utf-8') as csv_file:
                    for line in csv_file:
                        line = line.split(",")
                        if property_number in line[1]:
                            maintenencerequests.append(line)
                    return maintenencerequests
            
        except: raise  

    def get_maintenancerequest_by_employee(employee_id):
        try:    
                maintenencerequests = []
                with open("Project/data/csv_files/maintenancerequests.csv", "r", newline='', encoding='utf-8') as csv_file:
                    for line in csv_file:
                        line = line.split(",")
                        if employee_id in line[0]:
                            maintenencerequests.append(line)
                    return maintenencerequests
            
        except: raise  

    #Bæta við breyta verkbeiðni
