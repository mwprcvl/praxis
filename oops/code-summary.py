#!/usr/bin/env/python3

"""
OOP in Python summary
"""


from abc import ABC, abstractmethod


class AbstractEmployee(ABC): # abstraction
    """ """
    new_id = 1
  
    def __init__(self):
        """ """
        self.id = AbstractEmployee.new_id
        AbstractEmployee.new_id += 1

    @abstractmethod
    def say_id(self):
        """ """
        pass


class User:
    """ """

    def __init__(self):
        """ """
        self._username = None # encapsulation

    @property
    def username(self):
        """ """
        return self._username

    @username.setter
    def username(self, new_name):
        """ """
        self._username = new_name

    @username.deleter
    def username(self):
        del self._username


class Meeting:
    """ """

    def __init__(self):
        """ """
        self.attendees = []
  
    def __add__(self, employee):
        """ """
        self.attendees.append(employee.username)
        print("{} added.".format(employee.username))

    def __len__(self): # polymorphism
        """ """
        return len(self.attendees)


class Employee(AbstractEmployee, User): # inheritance
    """ """

    def __init__(self, username):
        """ """
        super().__init__()
        User.__init__(self)
        self.username = username

    def say_id(self):
        """ """
        print("My id is {}".format(self.id))
 
    def say_username(self):
        """ """
        print("My username is {}".format(self.username))


u1 = User()
u1.username = 'Adam'
u1.username
del u1.username

