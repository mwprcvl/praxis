#!/usr/bin/env/python3

"""
Abstraction helps with the design of code by defining necessary behaviors to be implemented within a class structure.

The abstractmethod decorator forces child classes to have the method that has been decorated.
"""


from abc import ABC, abstractmethod


class AbstractEmployee(ABC):
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


class Employee(AbstractEmployee):
    """ """

    def say_id(self):
        """ """
        print(self.id)


e1 = Employee()
e1.say_id()