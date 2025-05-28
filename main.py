import sqlite3
import re

conn = sqlite3.connect('contacts.db')
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS contacts (
    first_name TEXT,
    last_name TEXT,
    phone_number INT,
    email TEXT)""")

class Contacts:
    def __init__(self, first_name, last_name, phone_number, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
        
    # first name 
    @property
    def first_name(self):
        return self._first_name
    
    @first_name.setter
    def first_name(self, value):
            if not isinstance(value, str) or len(value) < 1:
                raise ValueError ("First name must consist of letters and not be less than 1 letter")
            else:
                self._first_name = value
                
    # last_name
    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self, value):
            if not isinstance(value, str) or len(value) < 1:
                raise ValueError ("Last name must consist of letters and not be less than 1 letter")
            else:
                self._last_name = value            
                
    # phone_number
    @property
    def phone_number(self):
        return self._phone_number
    
    @phone_number.setter
    def phone_number(self, value):
            if not isinstance(value, int) or len(value) < 1:
                raise ValueError ("Invalid format. Please try again.")
            else:
                self._phone_number = value       
               
    #  email           
    @property
    def email(self):
        return self._email 
    
    @email.setter
    def last_name(self, value):
            if not isinstance(value, str) or len(value) < 1:
                raise ValueError ("Email must consist of letters and not be less than 1 letter")
            else:
                self._last_name = value 