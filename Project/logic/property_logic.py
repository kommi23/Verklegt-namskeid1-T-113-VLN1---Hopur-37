class Property_logic():
    def add_property(property):
        all_properties = DW_properties.get_all_properties_dw()

        for existing_property in all_properties:
            if existing_property.property_number == property.property_number:
                raise RuntimeError("Property with ID {property.id} already exists")
        
        DW_properties.add_property_dw(property)

    def get_all_proberties_logic():
        return DW_properties.get_all_properties_dw()

from data.data_wrapper import *