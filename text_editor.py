# class Employee:
#     raise_amount = 0

#     # we use instanse methods when we are dealing with the instanses of the class
#     # `self` is like we put the instance name in its position
#     # مكانها object هادي زي كأنه بنحط ال `self` ال
#     def __init__(self, name, age, email):
#         self.name = name
#         self.age = age
#         self.email = email

#     # make manipulating to the class
#     # مكانها `class` هادي زي كأنه بنحط اسم ال `cls` ال
#     @classmethod
#     def set_raise_amount(cls, raise_amount):
#         cls.raise_amount = raise_amount

#     # we use @classmethod to deal with the class it self or as an alternative constructor ==> "__init__" for special types of inputs
#     @classmethod
#     def from_string(cls, string):
#         name, age, email = string.split("-")
#         return cls(name, age, email)

#     # when we don't have to use `self` or `cls` we use @staticmethod
#     @staticmethod
#     def is_workday(date):
#         if date.weekday() == 0 or date.weekday() == 1:
#             return False
#         else:
#             return True


# Employee.set_raise_amount(1.05)
# print(Employee.raise_amount)
# string1 = "zaher-18-zaherabuamro@gmail.com"
# emp1 = Employee.from_string(string1)
# # print(emp1.name)
# # print(emp1.age)
# # print(emp1.email)
# date = datetime.date(2021, 1, 19)
# print(Employee.is_workday(date))

import sqlite3
# db = sqlite3.connect("system.db")
# cr = db.cursor()
# cr.execute("CREATE TABLE IF NOT EXISTS `users`(Username TEXT, Age INTEGER, Email TEXT, Password TEXT)")
# cr.execute("CREATE TABLE IF NOT EXISTS `products`(Departnemt TEXT, ID INTEGER, Name TEXT, Quantity INTEGER)")


def sign_up_call():
    # prompting the user for his info
    print("Please Follow The Next Steps To Get Access To The System:-\n")
    username = input("Username: ").title().strip()
    age = int(input("Age: ").strip())
    email = input("Email: ").lower().strip()
    password = input("Password: ").strip()

    # write user data to the database
    cr.execute("INSERT INTO `users` Values(?, ?, ?, ?)", (username, age, email, password))

    # prompt the user for how mane products would he like to purchase
    purchase_quantity = int(input("How Many Product Would You Like To Purchase: ").strip())

    for i in range(purchase_quantity):
        print(f"Product {i + 1}:-\n")
        # prompt the user for the product info
        departnment = input("Departnment: ").title().strip()
        ID = int(input("ID: ").strip())
        name = input("Product Name: ").title()
        quantity = input("Quantity: ").title()
    
        # writing products data to the database
        cr.execute("INSERT INTO `products` Values(?, ?, ?, ?)", (departnment, ID, name, quantity))


def log_in_call():
    # prompt the user for his email an password
    u_email_prompt = input("Email: ").lower().strip()
    u_pass_prompt = input("Password: ").strip()

    # check if the given info is right or not
    cr.execute("SELECT Email, Password FROM users")
    needed_data = cr.fetchall()
    for row in needed_data:
        if row[0] == u_email_prompt and row[1] == u_pass_prompt:
            # prompt the user for how mane products would he like to purchase
            purchase_quantity = int(input("How Many Product Would You Like To Purchase: "))

            for i in range(purchase_quantity):
                print(f"\nProduct {i + 1}:-\n")
                # prompt the user for the product info
                departnment = input("Departnment: ").title().strip()
                ID = int(input("ID: ").strip())
                name = input("Name: ").title().strip()
                quantity = input("Quantity: ").title().strip()
          
                # writing products data to the database
                cr.execute("INSERT INTO `products` Values(?, ?, ?, ?)", (departnment, ID, name, quantity))    


if __name__ == '__main__':
    try:
        db = sqlite3.connect("system.db")
        cr = db.cursor()
        user_case = input("Log In ==> 'l'\nSign Up ==> 's'\n> ").lower().strip()
        u_email_prompt = ""
        u_pass_prompt = ""
        if user_case == 's':
            sign_up_call()
        elif user_case == 'l':
            log_in_call()
    except sqlite3.Error as e:
        print(f"Something Went Wrong ==> {e}")
    else:
        print("Database Has Updated.")
    finally:
        if db:
            db.commit()
            db.close()
            print("Database Successfuly Closed.")
