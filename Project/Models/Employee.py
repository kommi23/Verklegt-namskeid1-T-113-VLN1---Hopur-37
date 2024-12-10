class Employee:
    def __init__(self , employee_id, name, email, address, work_phone, personal_phone, location):
        self.employee_id = employee_id
        self.name = name
        self.email = email
        self.address = address
        self.work_phone = work_phone
        self.personal_phone = personal_phone
        self.location = location

    def turn_employee_into_list(employee):
        employee_as_list = []

        employee_as_list.append(employee.employee_id)
        employee_as_list.append(employee.name)
        employee_as_list.append(employee.email)
        employee_as_list.append(employee.address)
        employee_as_list.append(employee.work_phone)
        employee_as_list.append(employee.personal_phone)
        employee_as_list.append(employee.location)
        print("DEBUG. into turn into list")
        print(employee_as_list)
        return employee_as_list
    
    def turn_list_into_employee(employee: list):
        if len(employee) != 7:
            raise ValueError("This does not work")
        
        return Employee(*employee)
        
    def __str__(self) -> str:
        return f"[{self.employee_id}, {self.name}, {self.email}, {self.address}, {self.work_phone}, {self.personal_phone}, {self.location}]"