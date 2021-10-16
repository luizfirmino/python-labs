#!/usr/bin/env python3

# Assignment 3 - Q3
# Author: Luiz Firmino

# Scope
# The Python list stores a collection of objects in an ordered sequence. 
# In contrast, the dictionary stores objects in an unordered collection. 
# Give three examples of real-world objects that can be stored in a dictionary.

print("UPDATE: As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.")


userData = {
'account': ["Name", "E-mail", "Phone", "Password"],
'addresses': ["address1", "addressComp", "city" , "state"],
'creditCards': [["card1","expiration", "type"], ["card2","expiration", "type"]]
}

orderData = {
'order': ["user", "orderNumber", "date"],
'products': [["product1", "qtd", "price" , "total"], ["product2", "qtd", "price" , "total"]]
}

bidData = {
'lot': ["user", "number", "date"],
'bid': ["amount", "date", "type"]
}
