class Property_logic():
    def add_property(property):
        all_properties = DW_properties.get_all_properties_dw()

        for existing_property in all_properties:
            if existing_property.property_number == property.property_number:
                raise RuntimeError("Property with ID {property.id} already exists")
        
        DW_properties.add_property_dw(property)

    def change_property(id, info_change, what_info):
        all_properties = DW_properties.get_all_properties_dw()

        for property in all_properties:
            if property.id == id:
                pass
                
                
        raise RuntimeError("A property with this id does not exist")

from data.data_wrapper import *