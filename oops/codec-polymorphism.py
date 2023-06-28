#!/usr/bin/env/python3

"""
Polymorphism is the ability to apply an identical operation onto different types of objects.
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


class User:
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


class Meeting:
    """ """
    
    def __init__(self):
        """ """
        self.attendees = []
  
    def __add__(self, employee):
        """ """
        print("ID {} added.".format(employee.id))
        self.attendees.append(employee)

    def __len__(self):
        """ """
        return len(self.attendees)


e1 = Employee()
e2 = Employee()
e3 = Admin()
e3.say_user_info()
e4 = Manager()
e4.say_id()

m1 = Meeting()
m1 + e1
m1 + e2
m1 + e3
print(len(m1))
