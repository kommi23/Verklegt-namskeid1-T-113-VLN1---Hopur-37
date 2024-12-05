import csv

class ProbertyData:
    def __init__(self):
        pass
    
    def get_singular_property(self, property_number): 
        try:    
            with open("filefile.csv", "r", newline='', encoding='utf-8') as csv_file:
                for line in csv_file:
                    line = line.split(",")
                    if property_number in line[0]:
                        return line
        except: 
            return None 
        
    def add_property(self, proberty):
        try:
            with open("properties.csv", "a", newline='', encoding='utf-8') as csv_file:
                csv_file.write(proberty)
                return True
        except: raise

    def get_proberty(self):
        properties = []
        try:
            with open("properties.csv", newline='', encoding='utf-8') as csv_file:
                csv_reader = csv.reader(csv_file)

                for line in csv_reader:
                    properties.append(line)
            return properties
        except: raise

    def delete_property(property_number):  
        new_file = []
        try:
            with open("Project/data/csv_files/employees.csv", "r", newline='', encoding='utf-8') as csv_file:
                list_reader = csv.reader(csv_file)
                for row in list_reader:
                    if row[0]!= property_number:
                        new_file.append(row)
           
            with open("Project/data/csv_files/employees.csv", "w", newline='', encoding='utf-8') as new_csv_file:
                list_writer = csv.writer(new_csv_file)
                list_writer.writerows(new_file)
            return True
        except: raise