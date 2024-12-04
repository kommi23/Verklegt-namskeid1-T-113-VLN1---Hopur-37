import csv

class ProbertyData:
    def __init__(self):
        pass
    def add_property(self, proberty):
        try:
            with open("properties.csv", "a", newline='', encoding='utf-8') as csv_file:
                csv_file.write(proberty)
                return True
        except: return None
    def get_proberty(self):
        properties = []
        try:
            with open("properties.csv", newline='', encoding='utf-8') as csv_file:
                csv_reader = csv.reader(csv_file)

                for line in csv_reader:
                    properties.append(line)
            return properties
        except: return None