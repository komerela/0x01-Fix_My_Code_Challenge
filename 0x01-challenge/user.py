#!/usr/bin/python3
"""
User class
"""


class User:
    """ Function that prints the User class"""

    def __init__(self):
        """ Initializes email"""
        self.__email = None

    @property
    def email(self):
        """ Getter for function  """
        return self.__email

    @email.setter
    def email(self, email):
        """ Setter for function """
        if type(email) is not str:
            raise TypeError("email must be a string")
        self.__email = email


if __name__ == "__main__":

    u = User()
    u.email = "john@snow.com"
    print(u.email)
