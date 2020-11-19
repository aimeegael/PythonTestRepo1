class main_chef():

    def __init__(self, name, age, speciality):
        self.name = name
        self.age = age
        self.speciality = speciality

    def print_details(self):
        print(f"I'm a chef and my name is {self.name}. My Speciality is {self.speciality}.")

    def change_speciality(self, speciality):
        self.speciality = speciality
        print(f"I'm a chef and my name is {self.name}. My new Speciality is {self.speciality}.")
        
chef1 = main_chef("Alex", 35, "Chicken Noodles")

chef1.print_details()

chef2 = main_chef("Zander", 25, "Pizza and Lasagna")

chef2.print_details()

chef1.change_speciality("Orange Chicken Noodles")
chef2.change_speciality("Beef Stew and Carrot Cake")