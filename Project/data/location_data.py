import csv

class LocationData:
    def __init__():
        pass
                
    def get_locations_data():
        locations = []
        try:
            with open("locations.csv", "r", newline='', encoding='utf-8') as csv_file:
                csv_reader = csv.reader(csv_file)
                for line in csv_reader:
                    locations.append(line)
            return locations
        except: raise 

    def update_location_data(location, updated_data, what_data): #breytti þannig "what_data" er sent til okkar og segir þá til um hvaða row verður f breytingum 
        new_file = []
        try:
            with open("Project/data/csv_files/locations.csv", "r", newline='', encoding='utf-8') as csv_file:
                list_reader = csv.reader(csv_file)
                for row in list_reader:
                    if row[0] == location: #er ekki búinn að prófa að run-a kóðann en vonandi kemur þetta í veg fyrir tvö files
                        row[what_data] = updated_data
                        
                    new_file.append(row)
            
            with open("Project/data/csv_files/locations.csv", "w", newline='', encoding='utf-8') as new_csv_file:
                list_writer = csv.writer(new_csv_file)
                list_writer.writerows(new_file)
            return True
        except: raise      