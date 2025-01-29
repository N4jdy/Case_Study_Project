import os
from tinydb import TinyDB, Query
from serializer import serializer

class User:
    db = TinyDB(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'database.json'), storage=serializer, encoding='utf-8', ensure_ascii=False)
    db_connector = db.table('user')

    def __init__(self, id, username, email, role, password) -> None:
        """Create a new user based on the given name and id"""
        self.username = username
        self.id = id
        self.email = email
        self.role = role
        self.password = password

    def store_data(self)-> None:
        print("Storing data...")
        """Save the user to the database"""
        DeviceQuery = Query()
        result = self.db_connector.search(DeviceQuery.id == self.id)
        if result:
            self.db_connector.update({
                "username": self.username,
                "id": self.id,
                "email": self.email,
                "role": self.role,
                "password": self.password
            }, doc_ids=[result[0].doc_id])
            print("Data updated.")
        else:
            if not self.id:
                self.id = len(self.db_connector) + 1
            
            self.db_connector.insert({
                "username": self.username,
                "id": self.id,
                "email": self.email,
                "role": self.role,
                "password": self.password
            })
            print("Data inserted.")

    def delete(self) -> None:
        """Delete the user from the database"""
        pass
    
    def __str__(self):
        return f"User {self.id} - {self.username} - {self.email} - {self.role} - {self.password}"
    
    def __repr__(self):
        return self.__str__()
    
    @staticmethod
    def find_all() -> list:
        users_data = User.db_connector.all()
        users = []
        for data in users_data:
            user = User(data['id'], data['username'], data['email'], data['role'], data['password'])
            users.append(user)
        return users

    @classmethod
    def find_by_attribute(cls, by_attribute : str, attribute_value : str) -> 'User':
        """From the matches in the database, select the user with the given attribute value"""
        pass

    '''@classmethod     
    def find_by_attribute(cls, by_attribute : str, attribute_value : str, num_to_return=1) -> 'User':         
        DeviceQuery = Query()         
        result = cls.db_connector.search(DeviceQuery[by_attribute] == attribute_value)          
        if result:             
            data = result[:num_to_return]             
            user_results = [cls(d['username'], d['id'], d['email'], d['role'], d['password']) for d in data]             
            return user_results if num_to_return > 1 else user_results[0]         
        else:             
            return None 
    '''
