import os
from tinydb import TinyDB, Query
from serializer import serializer

class Device():
    # Database connection
    db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'database.json')
    db_connector = TinyDB(db_path, encoding='utf-8', ensure_ascii=False).table('devices')

    # Constructor
    def __init__(self, device_name: str, managed_by_user_id: str, description: str, image_url: str, category: str):
        self.device_name = device_name
        self.managed_by_user_id = managed_by_user_id
        self.is_active = True
        self.image_url = image_url
        self.description = description
        self.category = category

    # String representation of the class
    def __str__(self):
        return f'Device (Object) {self.device_name} ({self.managed_by_user_id}, {self.description}, {self.category})'

    # String representation of the class
    def __repr__(self):
        return self.__str__()

    def store_data(self):
        print("Storing data...")
        DeviceQuery = Query()
        result = self.db_connector.search(DeviceQuery.device_name == self.device_name)
        if result:
            self.db_connector.update({
                "device_name": self.device_name,
                "managed_by_user_id": self.managed_by_user_id,
                "is_active": self.is_active,
                "image_url": self.image_url,
                "description": self.description,
                "category": self.category
            }, doc_ids=[result[0].doc_id])
            print("Data updated.")
        else:
            self.db_connector.insert({
                "device_name": self.device_name,
                "managed_by_user_id": self.managed_by_user_id,
                "is_active": self.is_active,
                "image_url": self.image_url,
                "description": self.description,
                "category": self.category
            })
            print("Data inserted.")

    def delete(self):
        print("Deleting data...")
        DeviceQuery = Query()
        result = self.db_connector.search(DeviceQuery.device_name == self.device_name)
        if result:
            self.db_connector.remove(doc_ids=[result[0].doc_id])
            print(f"Device '{self.device_name}' deleted.")
        else:
            print(f"Device '{self.device_name}' not found.")

    def set_managed_by_user_id(self, managed_by_user_id: str):
        self.managed_by_user_id = managed_by_user_id

    @classmethod
    def find_by_attribute(cls, by_attribute: str, attribute_value: str, num_to_return=1):
        DeviceQuery = Query()
        result = cls.db_connector.search(DeviceQuery[by_attribute] == attribute_value)
        if result:
            data = result[:num_to_return]
            return [cls(d['device_name'], d['managed_by_user_id'], d['description'], d['image_url'], d['category']) for d in data]
        return []

    @classmethod
    def find_all(cls) -> list:
        results = cls.db_connector.all()
        return [cls(d['device_name'], d['managed_by_user_id'], d['description'], d['image_url'], d['category']) for d in results]