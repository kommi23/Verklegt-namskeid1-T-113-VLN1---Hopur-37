import csv

class EmployeeData:
    def __init__():
        pass
    def add_employee(employee):
        try:
            with open("Project/data/csv_files/employees.csv", "a", newline='', encoding='utf-8') as csv_file:
                list_writer = csv.writer(csv_file)
                list_writer.writerow(employee)
                return True 
        except: raise 
            
    def get_employees():
        employees = []
        try:
            with open("Project/data/csv_files/employees.csv", "r", newline='', encoding='utf-8') as csv_file:
                csv_reader = csv.reader(csv_file)
                for line in csv_reader:
                    employees.append(line)
            return employees
        except: 
            raise ValueError("Shit no work")
        
    def get_singular_employee(employee_id): 
        try:    
                with open("Project/data/csv_files/employees.csv", "r", newline='', encoding='utf-8') as csv_file:
                    for line in csv_file:
                        line = line.split(",")
                        if employee_id in line[0]:
                            return line    
        except: raise  

    def get_employees_by_location(location): 
        try:    
                employees = []
                with open("Project/data/csv_files/employees.csv", "r", newline='', encoding='utf-8') as csv_file:
                    for line in csv_file:
                        line = line.split(",")
                        if location in line[-1]:
                            employees.append(line)
                    return employees
            
        except: raise  

    def delete_employee(Employee_id):   
        new_file = []
        try:
            with open("Project/data/csv_files/employees.csv", "r", newline='', encoding='utf-8') as csv_file:
                list_reader = csv.reader(csv_file)
                for row in list_reader:
                    if row[0]!= Employee_id:
                        new_file.append(row)
            
            with open("Project/data/csv_files/employees.csv", "w", newline='', encoding='utf-8') as new_csv_file:
                list_writer = csv.writer(new_csv_file)
                list_writer.writerows(new_file)
            return True
        except: raise

    def employee_data_change(Employee_id, updated_data, what_data): #breytti þannig "what_data" er sent til okkar og segir þá til um hvaða row verður f breytingum 
        new_file = []
        try:
            with open("Project/data/csv_files/employees.csv", "r", newline='', encoding='utf-8') as csv_file:
                list_reader = csv.reader(csv_file)
                for row in list_reader:
                    if (row[0] == Employee_id and row[what_data] != updated_data): #er ekki búinn að prófa að run-a kóðann en vonandi kemur þetta í veg fyrir tvö files
                        row[what_data] = updated_data
                        new_file.append(row)
                    new_file.append(row)
            
            with open("Project/data/csv_files/employees.csv", "w", newline='', encoding='utf-8') as new_csv_file:
                list_writer = csv.writer(new_csv_file)
                list_writer.writerows(new_file)
            return True
        except: raise      


    #held fyrri kóðanum hér f neðan til öryggis 

        """
        

    def employee_change_email(Employee_id, new_email): #bætast við tvö files ef emailið er sama, þarf að tékka í logic eða ui
        new_file = []
        try:
            with open("Project/data/csv_files/employees.csv", "r", newline='', encoding='utf-8') as csv_file:
                list_reader = csv.reader(csv_file)
                for row in list_reader:
                    if row[0] == Employee_id:
                        row[2] = new_email
                        new_file.append(row)
                    new_file.append(row)
            
            with open("Project/data/csv_files/employees.csv", "w", newline='', encoding='utf-8') as new_csv_file:
                list_writer = csv.writer(new_csv_file)
                list_writer.writerows(new_file)
            return True
        except: raise    

    def employee_change_work_phone(Employee_id, new_work_phone): #bætast við tvö files ef síminn er sama, þarf að tékka í logic eða ui
        new_file = []
        try:
            with open("Project/data/csv_files/employees.csv", "r", newline='', encoding='utf-8') as csv_file:
                list_reader = csv.reader(csv_file)
                for row in list_reader:
                    if row[0] == Employee_id:
                        row[4] = new_work_phone
                        new_file.append(row)
                    new_file.append(row)
            
            with open("Project/data/csv_files/employees.csv", "w", newline='', encoding='utf-8') as new_csv_file:
                list_writer = csv.writer(new_csv_file)
                list_writer.writerows(new_file)
            return True
        except: raise    

    def employee_change_personal_phone(Employee_id, new_personal_phone): #bætast við tvö files ef síminn er sama, þarf að tékka í logic eða ui
        new_file = []
        try:
            with open("Project/data/csv_files/employees.csv", "r", newline='', encoding='utf-8') as csv_file:
                list_reader = csv.reader(csv_file)
                for row in list_reader:
                    if row[0] == Employee_id:
                        row[5] = new_personal_phone
                        new_file.append(row)
                    new_file.append(row)
            
            with open("Project/data/csv_files/employees.csv", "w", newline='', encoding='utf-8') as new_csv_file:
                list_writer = csv.writer(new_csv_file)
                list_writer.writerows(new_file)
            return True
        except: raise    

    def employee_change_location(Employee_id, new_location): #bætast við tvö files ef location er sama, þarf að tékka í logic eða ui
        new_file = []
        try:
            with open("Project/data/csv_files/employees.csv", "r", newline='', encoding='utf-8') as csv_file:
                list_reader = csv.reader(csv_file)
                for row in list_reader:
                    if row[0] == Employee_id:
                        row[6] = new_location
                        new_file.append(row)
                    new_file.append(row)
            
            with open("Project/data/csv_files/employees.csv", "w", newline='', encoding='utf-8') as new_csv_file:
                list_writer = csv.writer(new_csv_file)
                list_writer.writerows(new_file)
            return True
        except: raise    

    def employee_change_address(Employee_id, new_address): #bætast við tvö files ef address er sama, þarf að tékka í logic eða ui
        new_file = []
        try:
            with open("Project/data/csv_files/employees.csv", "r", newline='', encoding='utf-8') as csv_file:
                list_reader = csv.reader(csv_file)
                for row in list_reader:
                    if row[0] == Employee_id:
                        row[3] = new_address
                        new_file.append(row)
                    new_file.append(row)
            
            with open("Project/data/csv_files/employees.csv", "w", newline='', encoding='utf-8') as new_csv_file:
                list_writer = csv.writer(new_csv_file)
                list_writer.writerows(new_file)
            return True
        except: raise    
         """   