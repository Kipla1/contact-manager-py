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
            if not isinstance(value, int):
                raise ValueError ("Invalid format. Please try again.")
            else:
                self._phone_number = value       
               
    #  email           
    @property
    def email(self):
        return self._email 
    
    @email.setter
    def email(self, value):
        # Simple regex for email validation
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not isinstance(value, str) or not re.match(pattern, value):
            raise ValueError("Invalid email format. Please use the format xxxx@xxx.com")
        self._email = value
     
    @classmethod    
    def add_contact(cls, first_name, last_name, phone_number, email):
        contact = cls(first_name, last_name, phone_number, email)
        conn = sqlite3.connect('contacts.db')
        c = conn.cursor()
        with conn:
            c.execute("INSERT INTO contacts values(?, ?, ?, ?)", (contact.first_name, contact.last_name, contact.phone_number, contact.email))   
            print(f"{first_name} {last_name} has been added succesfully.")
        conn.commit()
        conn.close()     
        
    # delete conatct by first name(fn) 
    @classmethod   
    def delete_contact_by_fn(cls, first_name):
        conn = sqlite3.connect('contacts.db')
        c = conn.cursor()
        with conn:
            c.execute("DELETE FROM contacts WHERE first_name = ?", (first_name,))
            print(f"{first_name} has been deleted from contacts successfully.")
        conn.commit()
        conn.close() 
        
    # delete contacts by last name(ln)
    @classmethod   
    def delete_contact_by_ln(cls, last_name):
        conn = sqlite3.connect('contacts.db')
        c = conn.cursor()
        with conn:
            c.execute("DELETE FROM contacts WHERE last_name = ?", (last_name,))
            print(f"{last_name} has been deleted from contacts successfully.")
        conn.commit()
        conn.close()    
        
    # delete conatct by phone number(pn)
    @classmethod   
    def delete_contact_by_pn(cls, phone_number):
        conn = sqlite3.connect('contacts.db')
        c = conn.cursor()
        with conn:
            c.execute("DELETE FROM contacts WHERE phone_number = ?", (phone_number,))
            print(f"{phone_number} has been deleted from contacts successfully.")
        conn.commit()
        conn.close()      
        
        
    # delete contact by email
    @classmethod   
    def delete_contact_by_email(cls, email):
        conn = sqlite3.connect('contacts.db')
        c = conn.cursor()
        with conn:
            c.execute("DELETE FROM contacts WHERE email = ?", (email,))
            print(f"{email} has been deleted from contacts successfully.")
        conn.commit()
        conn.close()        
     
    # filter contacts by name    
    @classmethod
    def filter_contacts_by_name(cls, first=None, last=None):
        conn = sqlite3.connect('contacts.db')
        c = conn.cursor()
        results = []
        if first and not last:
            c.execute("SELECT * FROM contacts WHERE first_name = ?", (first,))
            results = c.fetchall()
            if results:
                for row in results:
                    print(row)
            else:
                print(f"No contacts found with first name '{first}'.")
        elif last and not first:
            c.execute("SELECT * FROM contacts WHERE last_name = ?", (last,))
            results = c.fetchall()
            if results:
                for row in results:
                    print(row)
            else:
                print(f"No contacts found with last name '{last}'.")
        elif first and last:
            c.execute("SELECT * FROM contacts WHERE first_name = ? AND last_name = ?", (first, last))
            results = c.fetchall()
            if results:
                for row in results:
                    print(row)
            else:
                print(f"No contacts found with first name '{first}' and last name '{last}'.")
        else:
            print("Please provide at least a first name or last name.")
        if results:
            if len(results) == 1:
                print(f"Showing {len(results)} result.")
            else:
                print(f"Showing {len(results)} results.")
        conn.close()
    
    # filter contacts by email     
    @classmethod
    def filter_contacts_by_email(cls, email):
        conn = sqlite3.connect('contacts.db')
        c = conn.cursor()
        with conn:
            c.execute("SELECT * FROM contacts WHERE email = ?", (email,))
            result = c.fetchall()
        for row in result:
            if len(result) == 1:
             print(f"Showing {len(result)} result.")    
            else:
                print(f"Showing {len(result)} results.")
                
        conn.close()        
# Contacts.add_contact("a", "b", 254721974408, "jawmes@gmail.com")  
Contacts.add_contact("ddg", "carezon", 254721974408, "jawmes@gmail.com")  
   
# Contacts.delete_contact_by_fn("a")
# Contacts.delete_contact_by_ln("b")
# Contacts.filter_contacts_by_name("a")

# Contacts.filter_contacts_by_email("jawmes@gmail.com")