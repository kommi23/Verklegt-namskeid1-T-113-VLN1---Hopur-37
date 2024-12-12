import os
from logic.logic_wrapper import *
from Models.Location import *


class Manage_Locations:

    def display_Locations(): #virkar
            locations = []
            locations = LL_location.list_all_locations()
                
            if not locations:
                print("No locations found.")

            else:
                for i in locations:
                    print(i)