import csv
from Models.Property import *

class PropertyData:
    def __init__():
        pass
    
    def get_singular_property_data(property_number): 
        try:    
            with open("Project/data/csv_files/properties.csv", "r", newline='', encoding='utf-8') as csv_file:
                for line in csv_file:
                    line = line.split(",")
                    if property_number in line[0]:
                        return line
        except: 
            return None 
        
    def add_property_data(property):
        try:
            with open("Project/data/csv_files/properties.csv", "a", newline='', encoding='utf-8') as csv_file:
                list_writer = csv.writer(csv_file)
                new_property_as_list = Property.turn_property_into_list(property)
                list_writer.writerow(new_property_as_list)
                return True
        except: raise

    def get_proberty_data():
        properties = []
        try:
            with open("Project/data/csv_files/properties.csv", newline='', encoding='utf-8') as csv_file:
                csv_reader = csv.reader(csv_file)

                for line in csv_reader:
                    property = []
                    property = Property.turn_list_into_property(line)
                    properties.append(property)

            return properties
        except: raise

    def get_properties_by_location_data(location):
        try:    
                properties = []
                with open("Project/data/csv_files/properties.csv", "r", newline='', encoding='utf-8') as csv_file:
                    for line in csv_file:
                        line = line.split(",")
                        if location in line[-1]:
                            properties.append(line)
                    return properties
        except: raise          


    def delete_property_data(property_number):  
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


def update_property_data(property_number, updated_data, what_data): #breytti þannig "what_data" er sent til okkar og segir þá til um hvaða row verður f breytingum 
    new_file = []
    try:
        with open("Project/data/csv_files/properties.csv", "r", newline='', encoding='utf-8') as csv_file:
            list_reader = csv.reader(csv_file)
            for row in list_reader:
                if row[0] == property_number: #er ekki búinn að prófa að run-a kóðann en vonandi kemur þetta í veg fyrir tvö files
                    row[what_data] = updated_data
                    
                new_file.append(row)
        
        with open("Project/data/csv_files/properties.csv", "w", newline='', encoding='utf-8') as new_csv_file:
            list_writer = csv.writer(new_csv_file)
            list_writer.writerows(new_file)
        return True
    except: raise      