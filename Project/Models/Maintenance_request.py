class Maintenance_request:
    def __init__(self,id,property_number,description,priority,date,budget,recurring_task,employee_id = "None", report = "Empty", status = "Open"):
        self.id = id
        self.property_number = property_number
        self.description = description
        self.priority = priority
        self.date = date
        self.budget = budget
        self.recurring_task = recurring_task
        self.employee_id = employee_id
        self.report = report
        self.status = status
    
    def turn_maintenance_request_into_list(self):
        return [self.id, self.property_number, self.description, self.priority, self.date, self.budget, self.recurring_task, self.employee_id, self.report, self.status]
    
    def __str__(self) -> str:
        return f"{self.id}, {self.property_number}, {self.description}, {self.priority}, {self.date}, {self.budget}, {self.recurring_task}, {self.employee_id}, {self.report}, {self.status}"