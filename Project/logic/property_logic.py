class Property():

    def get_all_properties() -> list:
        return dw_properties.get_all_properties()
    
    def get_property_by_id(id: int) -> list:
            property = dw_properties.get_property_by_id(id) 

            if property is None:
                raise RuntimeError("Property with id {id} not found")
            
            return property
    
    def get_property_by_location(location: str) -> list:
        all_properties = dw_properties.get_property_by_location(location)


    def add_property(property):
        return dw_properties.add_property(property)
    
    def delete_property(property_id: int):
         return dw_properties.delete_property(property_id)
        





from data.data_wrapper import *