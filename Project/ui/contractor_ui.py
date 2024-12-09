from tabulate import tabulate # type: ignore
from logic.contractor_logic import Contractor
from input_dictionaries import input_dictionaries

class ContractorUI:
    def __init__(self):
        self.logic = Contractor
    
    def display_contractors(self):
            contractors = logic.get_contractor_list()
            if not contractors:
                print("")
                return
            else:
                table = [c['id'], c['name'], c['location'], c['gsm'], c['address'], c['opening_hours']]
                print(tabulate(table, headers=["ID", "Name", "Location", "GSM", "Address", "Opening hours"], tablefmt="grid"))
            

    def add_contractor(self):
        try:
            id = input("Enter Contractor's ID: ")
            name = input("Enter Contractor's Name: ")
            location = input("Enter Contractor's Location: ")
            gsm = input("Enter Contractor's Phone Number: ")
            address = input("Enter Contractor's Address: ")
            opening_hours = input("Enter Contractor's Opening Hours: ")

            self.logic.add_contractor(Contractor)
            print("Contractor has been added")
        except input_dictionaries: # vantar að bæta við 
             print("Some error") # réttu exceptions
    
    def update_contractor(self):
         try:
            id = input("Enter Contractor's ID to Update: ")
            info_change = input("Enter Contractor's Information to change (e.g., name, address): ").lower()
            new_info = input("Enter new {info_change} here: ")
            
            self.logic.update_contractor(id)

    

#except input_dictionaries: bæti við þegar það er tilbuið



