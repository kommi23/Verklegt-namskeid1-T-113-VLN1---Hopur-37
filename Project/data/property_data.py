import csv
from Models.Property import *

class PropertyData:
    def __init__(self):
        pass
    
    def get_singular_property_data(self, property_number): 
        try:    
            with open("Project/data/csv_files/properties.csv", "r", newline='', encoding='utf-8') as csv_file:
                for line in csv_file:
                    line = line.split(",")
                    if property_number in line[0]:
                        return line
        except: 
            return None 
        
    def add_property_data(self, property):
        try:
           
            with open("Project/data/csv_files/properties.csv", "a", newline='\n', encoding='utf-8') as csv_file:
                list_writer = csv.writer(csv_file)
                new_property_as_list = Property.turn_property_into_list(property)
                list_writer.writerow(new_property_as_list)
                return "Success!"
        except: raise

    def get_all_proberties_data(self):
        properties = []
        try:
            with open("Project/data/csv_files/properties.csv", newline='', encoding='utf-8') as csv_file:
                csv_reader = csv.reader(csv_file)
                for line in csv_reader:
                    property = Property(*line)
                    properties.append(property)

            return properties
                
        except: raise

    def get_properties_by_location_data(self, location):
        try:    
                properties = []
                with open("Project/data/csv_files/properties.csv", "r", newline='', encoding='utf-8') as csv_file:
                    
                    for line in csv_file:
                        line = line.strip("\n").split(",")
                        if location in line[-1]:
                            property = Property(*line)
                            properties.append(property)
                    return properties
        except: raise          


    def delete_property_data(self, property_number):  
        new_file = []
        try:
            with open("Project/data/csv_files/properties.csv", "r", newline='', encoding='utf-8') as csv_file:
                list_reader = csv.reader(csv_file)
                for row in list_reader:
                    if row[0]!= property_number:
                        new_file.append(row)
           
            with open("Project/data/csv_files/properties.csv", "w", newline='', encoding='utf-8') as new_csv_file:
                list_writer = csv.writer(new_csv_file)
                list_writer.writerows(new_file)
            return True
        except: raise


    def update_property_data(self, property_id, updated_data, what_data):
        new_file = []
        try:
            with open("Project/data/csv_files/properties.csv", "r", newline='', encoding='utf-8') as csv_file:
                list_reader = csv.reader(csv_file)
                for row in list_reader:
                    if row[0] == str(property_id): 
                        row[int(what_data)] = updated_data
                        
                    new_file.append(row)
            
            with open("Project/data/csv_files/properties.csv", "w", newline='', encoding='utf-8') as new_csv_file:
                list_writer = csv.writer(new_csv_file)
                list_writer.writerows(new_file)
            return True
        except: raise      