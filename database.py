import pymongo
from pymongo import MongoClient

class Database:

    client = pymongo.MongoClient("mongodb://localhost:27017/")

    def login(self, username, password):
        collection = self.client.users.collection
        result = collection.find( {"username": username, "password": password} )
        users = list(result)
        if not users :
            return None
        else :
            return users[0]
            
    def get_users_by_admin(self, admin_username, search_criteria=None):
        collection = self.client.users.collection
        if not search_criteria :
            result = collection.find( {"managed_by": admin_username},  {"_id": 0 } )
        else:
            result = collection.find( {"managed_by": admin_username, "username": search_criteria},  {"_id": 0 } )
        users = list(result)
        if not users :
            return None
        else :
            return users

