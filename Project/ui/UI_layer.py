# For the UI layer
class MenuDisplayer:

    def __init__(self):
        self.files = 
        

    def create_employee(self):
        # Tekur við upplýsingum frá notanda og bætir employee við
        name = input("Enter employee's name: ")
        employee_id = input("Enter employee's ID: ")
        email = input("Enter employee's email: ")
        address = input("Enter employee's address: ")
        work_phone = input("Enter employee's work phone: ")
        personal_phone = input("Enter employee's personal phone: ")
        location = input("Enter employee's location: ")

        headers = ["Name", "Employee ID", "Email", "Address", "Work Phone", "Personal Phone", "Location"]
        data = [name, employee_id, email, address, work_phone, personal_phone, location]
        self.write_to_file("employee", headers, data)
        print("Employee has been added")

    def create_manager(self):
        # Tekur við upplýsingum frá notanda og bætir manager við
        name = input("Enter manager's name: ")
        manager_id = input("Enter manager's ID: ")
        email = input("Enter manager's email: ")
        address = input("Enter manager's address: ")
        work_phone = input("Enter manager's work phone: ")
        personal_phone = input("Enter manager's personal phone: ")
        location = input("Enter manager's location: ")

        headers = ["Name", "Manager ID", "Email"]
        data = [name, manager_id, email, address, work_phone, personal_phone, location]
        self.write_to_file("manager", headers, data)
        print("Manager has been addedd")

    def create_contractor(self):
        # Tekur við upplýsingum frá notanda og bætir verktaka við
        name = input("Enter contractor's name: ")
        contractor_id = input("Enter contractor's ID: ")
        email = input("Enter contractor's email: ")
        reputation = input("Enter contractor's previuos reputation: ")
        headers = ["Name", "Contractor ID", "Email", "reputation"]
        data = [name, contractor_id, email, reputation]
        self.write_to_file("contractor", headers, data)
        print("Contractor has been added")

    def view_records(self, file_choice):
  
    # næ í file útfrá vali notendans(file_choie)
    filename = self.files.get(file_choice)
    if not filename:
        print(f"Invalid choice: '{file_choice}'. Please try again.")
        return

    try:
        #Athugar hvort fileið sé til
        if not os.path.exists(filename):
            print(f"No records found. File '{filename}' does not exist.")
            return

        # Athugar hvort fileið sé tómt
        if os.stat(filename).st_size == 0:
            print(f"No records found. File '{filename}' is empty.")
            return

        
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            print(f"Records in '{filename}':")
            for row in reader:
                print(", ".join(row)) 

    except FileNotFoundError:
        print(f"File '{filename}' not found. Please check the file path.")
    except OSError:
        print(f"An error occurred while accessing the file '{filename}'.")

    

    def employee_menu(self):
        # menu fyrir starfsmenn
        while True:
            print("\nEmployee Menu")
            print("1. Add Employee")
            print("2. View Employees")
            print("3. Back to Main Menu")
            choice = input("Enter your choice: ")
            if choice == '1':
                self.create_employee()
            elif choice == '2':
                self.view_records("employee")
            elif choice == '3':
                break
            else:
                print("Invalid choice. Please try again.")

    def manager_menu(self):
        # menu fyrir manager
        while True:
            print("\nMANAGER MENU")
            print("1. Add Manager")
            print("2. View Managers")
            print("3. Back to Main Menu")
            choice = input("Enter your choice: ")
            if choice == '1':
                self.create_manager()
            elif choice == '2':
                self.view_records("manager")
            elif choice == '3':
                break
            else:
                print("Invalid choice. Please try again.")

    def contractor_menu(self):
        # menu fyrir verktaka
        while True:
            print("\nContractor Menu")
            print("1. Add Contractor")
            print("2. View Contractors")
            print("3. Back to Main Menu")
            choice = input("Enter your choice: ")
            if choice == '1':
                self.create_contractor()
            elif choice == '2':
                self.view_records("contractor")
            elif choice == '3':
                break
            else:
                print("Invalid choice. Please try again.")