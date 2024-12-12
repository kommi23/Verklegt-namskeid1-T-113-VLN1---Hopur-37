import csv
from Models.Location import *

class LocationData:
    def __init__():
        pass
                
    def get_locations_data():
        locations = []
        try:
            with open("project/data/csv_files/locations.csv", "r", newline='', encoding='utf-8') as csv_file:
                csv_reader = csv.reader(csv_file)
                for line in csv_reader:
                    location = Location(*line)
                    locations.append(location)
            return locations
        except: raise 