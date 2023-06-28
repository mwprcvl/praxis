#!/usr/bin/env/python3

"""
Encapsulation is the process of making methods and data hidden inside the object they relate to.

Public methods have no leading underscores.

Protected methods have a single leading underscore in Python.

Private methods have two leading underscores and lead to name mangling
"""


class Employee():
    """ """

    def __init__(self):
        """ """
        self.id = None
        self._id = 23
        self.__id = 10


e = Employee()
print(dir(e))
