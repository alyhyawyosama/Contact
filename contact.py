# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 15:08:00 2023

@author: Asama
"""


    
class Contact:
    def __init__(self,name,phone,email):
        self.name= name
        self.phone = phone
        self.email = email 
        
    def __str__(self):
        return ("Name : {} - Phone:{} - Email:{}".format(self.name,self.phone,self.email))
    



class ContactManager:
    def __init__(self):
        self.contacts = []
    
    def add(self,contact):
        self.contacts.append(contact)
    
    
    def search(self,name):

        if len(self.contacts)<1 :
            print("You dont have any contact")
            return     
        
        for contact in self.contacts :
            if contact.name == name :  
                return contact
        print("Not found")
        return None
    
    def print(self):
        if len(self.contacts)<1 :
            print("You don't have any contact")
            return    
        for contact in self.contacts:
            print(contact)
            
    def remove(self,name):
        if len(self.contacts)<1 :
            print("You dont have any contact")
            return  
        
        #if self.contacts[name1] == self.contacts[name1]:
        i = 0
        for contact in self.contacts :
            if contact.name == name :
                self.contacts.pop(i) 
                return  True
            i+=1            
        return False

    




contact = ContactManager()
while True:
    choice =  input("Enter # to stop\n1-Add contact\n2-Search contact\n3-Print contacts \n4-Delete contact\n5-Exit\nEnter:")
    if choice == "#":
        break
    if choice == "1":
        name = input("Name:")
        phone = input("Number:")
        email = input("Email:")
        newContact =  Contact(name,phone,email)
        contact.add(newContact)

    elif choice == "2":
        name = input("Name:")
        con = contact.search(name)
        if con != None:
            print(con)
        
    elif choice == "3":
        contact.print()
        
    elif choice == "4":
        name = input("Name:")
        status = contact.remove(name)
        if status :
            print("Deleted successfully")
        else :
            print("Not found")
            
        
    elif choice == "5":
        break
    else :
        print("Error try again")



