from data.data_wrapper import * 

class Location_logic:

    def get_location_list():
        return DW_Location.get_all_locations()
    