# Example Python Code to Insert a Document 

from pymongo import MongoClient 
from bson.objectid import ObjectId 

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self, username, password): 
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # You must edit the password below for your environment. 
        # 
        # Connection Variables 
        
        
        USER = username
        PASS = password
        # USER = 'aacuser' 
        # PASS = 'ynrec1yahs2!' 
        HOST = 'localhost' 
        PORT = 27017 
        DB = 'aac' 
        COL = 'animals' 
        # 
        # Initialize Connection 
        # 
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT)) 
        self.database = self.client['%s' % (DB)] 
        self.collection = self.database['%s' % (COL)] 

    # Create a method to return the next available record number for use in the create method 
    def get_next_rec_num(self):
        return self.database.animals.count_documents({}) + 1
            
    # Complete this create method to implement the C in CRUD. 
    def create(self, data):
        if data is not None: 
            data["rec_num"] = self.get_next_rec_num()
            try:self.database.animals.insert_one(data)  # data should be dictionary
            except e:
                raise e
                
            print("Record added successfully")
        else: 
            raise Exception("Nothing to save, because data parameter is empty") 

    # Create method to implement the R in CRUD.
    def read(self, filter):
        return list(self.database.animals.find(filter)) #filter should be a dictionary of filters
    
    def update(self, filter, data): # Filter should be a dictionary to filter the collection, Data is a dictionary of key:value pairs to be updated
        if not data is None: # if there is data to be updated
            value = self.database.animals.update_many(filter, {"$set":data})
            return value.modified_count # return the number of items updated
        else:
            raise Exception("Nothing to update, because data parameter is empty")
    
    def delete(self, filter): # filter should be a dictionary to filter the collection
        value = self.database.animals.delete_many(filter)
        return value.deleted_count # return the number of items deleted
        