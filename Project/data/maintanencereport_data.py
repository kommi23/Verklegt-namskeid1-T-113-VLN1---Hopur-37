import csv

class MaintenanceReportData:
    def __init__():
        pass
    def add_maintenancereport(maintenancereport):
        try:
            with open("maintenancereports.csv", "a", newline='', encoding='utf-8') as csv_file:
                csv_file.write(maintenancereport) 
                return True
        except: raise        
    def get_maintenancereport():
        try:
            with open("maintenancereports.csv", "r", newline='', encoding='utf-8') as csv_file:
                maintenancereports = []
                csv_reader = csv.reader(csv_file)
                for line in csv_reader:
                    maintenancereports.append(line)
            return maintenancereports
        except: raise 

    def get_maintenancereports_by_property(property):
        try:    
                maintenencereports = []
                with open("Project/data/csv_files/maintenancereports.csv", "r", newline='', encoding='utf-8') as csv_file:
                    for line in csv_file:
                        line = line.split(",")
                        if property in line[-1]:
                            maintenencereports.append(line)
                    return maintenencereports
            
        except: raise  

    def get_maintenancereports_by_date(date):
        try:    
                maintenencereports = []
                with open("Project/data/csv_files/maintenancereports.csv", "r", newline='', encoding='utf-8') as csv_file:
                    for line in csv_file:
                        line = line.split(",")
                        if date in line[1]:
                            maintenencereports.append(line)
                    return maintenencereports
            
        except: raise  

    def get_maintenancereports_by_employee(employee_id):
        try:    
                maintenencereports = []
                with open("Project/data/csv_files/maintenancereports.csv", "r", newline='', encoding='utf-8') as csv_file:
                    for line in csv_file:
                        line = line.split(",")
                        if employee_id in line[2]:
                            maintenencereports.append(line)
                    return maintenencereports
            
        except: raise  

    def get_maintenancereports_by_status(status):
        try:    
                maintenencereports = []
                with open("Project/data/csv_files/maintenancereports.csv", "r", newline='', encoding='utf-8') as csv_file:
                    for line in csv_file:
                        line = line.split(",")
                        if status in line[3]:
                            maintenencereports.append(line)
                    return maintenencereports
            
        except: raise  

    def get_maintenancereports_by_priority(priority):
        try:    
                maintenencereports = []
                with open("Project/data/csv_files/maintenancereports.csv", "r", newline='', encoding='utf-8') as csv_file:
                    for line in csv_file:
                        line = line.split(",")
                        if priority in line[4]:
                            maintenencereports.append(line)
                    return maintenencereports
            
        except: raise  