from logic_wrapper import Manager

class Manager_UI:
    def __init__(self):
        self.manager_logic = manager_logic()

    def mananger_menu(self):
        print("\n=== Employee Management ===")
        print("1. Create manager")
        print("2. List managers")
        print("3. change managers")
        print("E. Go back")
