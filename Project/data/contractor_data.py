import csv

class ContractorData:
    def __init__(self):
        pass
    def add_contractor(contractor):
        try:
            with open("Project/data/csv_files/contractors.csv", "a", newline='', encoding='utf-8') as csv_file:
                list_writer = csv.writer(csv_file)
                list_writer.writerow(contractor)
                return True 
        except: raise     

    def get_contractor():
        contractors = []
        try:
            with open("Project/data/csv_files/contractors.csv", "r", newline='', encoding='utf-8') as csv_file:
                csv_reader = csv.reader(csv_file)
                for line in csv_reader:
                    contractors.append(line)
            return contractors
        except: 
            raise ValueError("Shit no work")
        
    def get_singular_employee(contractor): 
        try:    
                with open("Project/data/csv_files/contractors.csv", "r", newline='', encoding='utf-8') as csv_file:
                    for line in csv_file:
                        line = line.split(",")
                        if contractor in line[0]:
                            return line
            
        except: raise  

    def get_contractor_by_location(contractor): 
        try:    
                contractors = []
                with open("Project/data/csv_files/contractors.csv", "r", newline='', encoding='utf-8') as csv_file:
                    for line in csv_file:
                        line = line.split(",")
                        if contractor in line[-1]:
                            contractors.append(line)
                    return contractors
            
        except: raise  

    def delete_contractor(contractor):   
        new_file = []
        try:
            with open("Project/data/csv_files/contractors.csv", "r", newline='', encoding='utf-8') as csv_file:
                list_reader = csv.reader(csv_file)
                for row in list_reader:
                    if row[0]!= contractor:
                        new_file.append(row)
            
            with open("Project/data/csv_files/contractors.csv", "w", newline='', encoding='utf-8') as new_csv_file:
                list_writer = csv.writer(new_csv_file)
                list_writer.writerows(new_file)
            return True
        except: raise

#þarf að bæta við contractor change