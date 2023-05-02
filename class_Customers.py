import json
from constant import FILE_CUSTOMER


class Customers:
    def __init__(self, id, name, city, age):
        self.id = id
        self.name = name
        self.city = city
        self.age = age

    def __str__(self):
        return f"Customer name is:{self.name}, is id:{self.id}, is age:{self.age}, live in:{self.city}"


class CustomerList:
    all_customers = []

    def add_customer(self, customer):
        self.all_customers.append(customer)

    @staticmethod
    def load_all_customer(fillename):
        # reading the file
        with open(fillename) as f:
            all_file_json = json.load(f)

        # turn into objects
        for single_json in all_file_json:
            customer = Customers(**single_json)
            CustomerList.all_customers.append(customer)

    @staticmethod
    def save_all_customer(fillename):
        new_list = []
        for customer in CustomerList.all_customers:
            new_list.append(customer.__dict__)
        with open(fillename, "w") as f:
            json.dump(new_list, f)

#  The function add_new_customer adds customers, and checks at the beginning that a 
# customer whose ID already exists in the system has not been entered to the fille.

    def add_new_customer(self, customerdata):
        new_list_id = []
        for customer in CustomerList.all_customers:
            new_list_id.append(customer.id)
        new_id = input("Enter customer id:")
        while True:
            if new_id not in new_list_id:
                break
            else:
                new_id = input("The id is already taken please enter new id:")
        name = input("Enter customer first and last name:")
        city = input("Enter customer city:")
        age = input("Enter customer age:")
        customer = Customers(id=new_id, name=name, city=city, age=age)
        customerdata.add_customer(customer)
        customerdata.save_all_customer(FILE_CUSTOMER)
        print("---Customer added successfully.---")

    def remove_customer(self):
        name_remove = input("Enter customer full name you want to remove:")
        found = False
        for customer in self.all_customers:
            if customer.name.lower() == name_remove.lower():
                self.all_customers.remove(customer)
                CustomerList.save_all_customer(FILE_CUSTOMER)
                print("---Customer removed successfully.---")
                found = True
                break
        if not found:
            print(f"---Customer with name {name_remove} not found.---")

    def search_customer(self):
        name_search = input("Enter customer full name you want to search:")
        found = False
        for member in self.all_customers:
            if member.name.lower() == name_search.lower():
                print(member)
                found = True
                break
        if not found:
            print(f"---Customer with name {name_search} not found.---")

    def __str__(self):
        ret_str = ""
        for customer in self.all_customers:
            ret_str += str(customer) + "\n"
        return ret_str
