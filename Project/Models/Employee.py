class Employee:
    def __init__(self , employee_id, name, social_security_number, email, address, work_phone, personal_phone, location):
        self.employee_id = employee_id
        self.name = name
        self.social_security_number = social_security_number
        self.email = email
        self.address = address
        self.work_phone = work_phone
        self.personal_phone = personal_phone
        self.location = location


    def turn_employee_into_list(self):
        return [self.employee_id, self.name, self.social_security_number, self.email, self.address,
                self.work_phone, self.personal_phone, self.location]
   
    def turn_list_into_employee(employee: list):
        if len(employee) != 7:
            raise ValueError("This does not work")
       
        return Employee(*employee)
       
    def __str__(self) -> str:
        return f"[{self.employee_id}, {self.name}, {self.email}, {self.address}, {self.work_phone}, {self.personal_phone}, {self.location}]"

