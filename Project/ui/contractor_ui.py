from tabulate import tabulate # type: ignore
from logic.contractor_logic import Contractor
from logic.logic_wrapper import ll_employee
from Project.ui.input_validators import Input_validators

class ContractorUI:
    def __init__(self):
        self.logic = Contractor
    
    def contractor_menu(self):
        print("Contractor Menu")
        print("1. Display Contractors")
        print("2. Add Contractor")
        print("3. Update Contractor")
        print("4. View Contractor Reviews")
        print("5. Add Contractor Review")
        print("6. View Maintenance History")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            self.display_contractors
        elif choice == '2':
            self.add_contractor
        elif choice == '3':
            self.update_contractor
        elif choice == '4':
            self.view_reviews
        elif choice == '5':
            self.add_review
        elif choice == '6':
            self.view_maintenance_history
        elif choice == '7':
            print("Exititng..")
        else:
            print("Invalid choice, try again")    

    def display_contractors(self):
            contractors = logic.get_contractor_list()
            if not contractors:
                print("")
                return
            else:
                table = [
                    [con['id'], con['name'], con['location'], con['gsm'], con['address'], con['opening_hours']]
                    for con in contractors]
                
                print(tabulate(table, headers=["ID", "Name", "Location", "GSM", "Address", "Opening hours"], tablefmt="grid"))
            

    def add_contractor(self):
        try:
            id = input("Enter Contractos ID: ")
            name = input("Enter Contractos Name: ")
            location = input("Enter Contractos Location: ")
            gsm = input("Enter Contractos Phone Number: ")
            address = input("Enter Contractos Address: ")
            opening_hours = input("Enter Contractos Opening Hours: ")

            self.logic.add_contractor(Contractor)
            print("Contractor has been added")
        except Input_validators: # vantar að bæta við 
            print("Some error") # réttu exceptions
    
    def update_contractor(self):
        try:
            id = input("Enter Contractos ID to Update: ")
            info_change = input("Enter Contractos Information to change (e.g., name, address): ").lower()
            new_info = input("Enter new here: ")

            # vantar dictlista hér til að tengja við uppls
            
            self.logic.update_contractor(id, {info_change: new_info})
            print(f"Contractor with ID {id} updated successfully")
        except Input_validators:
            print("Some error") # bæti við
    
    def view_reviews(self):
        try:
            id = input("Enter Contractors ID to View Reviews: ")
            reviews = self.logic.get_contractor_review(id)
            if not reviews:
                print("No reviews available")
            else:
                for i in reviews:
                    print(f"- {i}")
        except Input_validators:
            print("Invalid input. Try again.")
    
    def add_review(self):
        try:
            id = input("Enter Contractors ID to add a review too: ")
            review = input("Enter your review: ")  

            self.logic.add_contractor_review(id, {review})
            print(f"New review for {id} has been added")
        except Input_validators:
            print("some error")
    
    def view_maintenance_history(self):
        try:
            id = input("Enter Contractors ID to view maintenance history: ")
            history = self.logic.search_contractor_maintenance_history(id)
            if not history:
                print("No maintenance history available.")
            else:
                for i in history:
                    print(f"- {i}")
        except Input_validators:
            print("some error")

    
#except Input_validators: bæti við þegar það er tilbuið



