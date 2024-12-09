class Contractor:

    def __init__(self, id: int, name: str, location: str, gsm: int, address: str, opening_hours: str):
        self.id = id
        self.name = name
        self.location = location
        self.gsm = gsm
        self.address = address
        self.opening_hours = opening_hours

    def get_contractor_list() -> list:
        return dw_contractors.get_contractors()

    def add_contractor(contractor: list):
        # Get list of all the contractors
        list_of_contractors = dw_contractors.write_contractor(contractor)

        # Check if the id or the name already exists in the db, if so raise a runtime error
        for existing_contractor in list_of_contractors:
            if contractor[0] == existing_contractor[0]:
                raise RuntimeError("A contractor with this ID already exists")
            elif contractor[1] == existing_contractor[1]:
                raise RuntimeError("A contractor with this name already exists")
            
            # If no error is raised return the contractor and send to data_layer
            else:
                return contractor

    def update_contractor(id: int, updated_data, what_data: int):
        contractor = dw_contractors.search_contractor_by_id()

        if contractor[0] == id:
            contractor[what_data] = updated_data
            dw_contractors.update_contractor(contractor)
            return f"Contractor with ID {id} was updated successfully"
        else:
            return f"Contractor with ID {id} not found"
        


    def get_contractor_review() -> list:
        return dw_contractors.get_contractor_review()

    def add_contractor_review(id: int, review: str):
        dw_contractors.write_contractor_review(id, review)


    def get_contractor_review(id):
        return dw_contractors.get_contractor_review(id)

    def search_contractor_maintainance_history(id) -> list:
        return dw_contractors.get_contractor_maintainance_history(id)



from data_wrapper import * 