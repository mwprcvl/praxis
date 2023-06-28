#!/usr/bin/env/python3

"""
Inheritance is getting properties from similar types in a hierarchy
"""


class Employee():
    """ """
    new_id = 1

    def __init__(self):
        """ """
        self.id = Employee.new_id
        Employee.new_id += 1

    def say_id(self):
        """ """
        print("My id is {}.".format(self.id))


class User():
    """ """

    def __init__(self, username, role="Customer"):
        """ """
        self.username = username
        self.role = role

    def say_user_info(self):
        """ """
        print("My username is {}".format(self.username))
        print("My role is {}".format(self.role))


class Admin(Employee, User):
    """ """
    
    def __init__(self):
        """ """
        super().__init__()
        User.__init__(self, self.id, "Admin")

    def say_id(self):
        """ """
        super().say_id()
        print("I am an admin.")


class Manager(Admin):
    """ """

    def say_id(self):
        """ """
        print("I am in charge.")
        super().say_id()


e1 = Employee()
e2 = Employee()
e3 = Admin()
e3.say_user_info()
e4 = Manager()
e4.say_id()
