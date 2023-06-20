#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """CRUD operations for Animal collections in MongoDB"""
    
    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the
        # animals collections, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        USER = 'aacuser'
        PASS = 'aacuser'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 31781
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
        
# Complete this create method to implement the C in CRUD.
    def create(self, data):
        # create an object if data exists
        if data is not None:
            self.database.animals.insert_one(data) # data should be in dictionary
            return True
        else:
            raise Exception('Nothing to save, because data parameter is empty')
            
# Create method to implement the R in CRUD. 
    def read(self, search):
        try:
            if search is not None:
                results = list(self.database.animals.find(search, {"_id": False}))
                return results
            else:
                raise Exception ("Nothing to search. Parameter empty")
                return False
        except Exception as e:
            print("An exception has occurred: ", e)
        
# Create method to implement the U in CRUD.
    def update(self, searchData, updateData):
        # update an object if object exists
        if searchData is not None:
            result = self.database.animals.update_many(searchData, {"$set": updateData})
        else:
            raise Exception('Nothing to update, because data parameter is empty')
        return result
    
# Create method to implement the D in CRUD.
    def delete(self, deleteData):
        # delete an object if object exists
        if deleteData is not None:
            result = self.database.animals.delete_many(deleteData)
        else:
            raise Exception('Nothing to delete, because data parameter is empty')
        return result


# In[ ]:




