
import os
from tinydb import TinyDB, Query
from serializer import serializer



class Device():
    # Class variable that is shared between all instances of the class
    db_connector = TinyDB(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'database.json'), storage=serializer).table('devices')

    # Constructor
    def __init__(self, device_name : str, managed_by_user_id : str, description : str, image_url : str, category: str):
        self.device_name = device_name
        # The user id of the user that manages the device
        # We don't store the user object itself, but only the id (as a key)
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
        # Check if the device already exists in the database
        DeviceQuery = Query()
        result = self.db_connector.search(DeviceQuery.device_name == self.device_name)
        if result:
            # Aktualisiere das Gerät in der Datenbank
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
            # Gerät existiert nicht, füge es hinzu
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
        # Check if the device exists in the database
        DeviceQuery = Query()
        result = self.db_connector.search(DeviceQuery.device_name == self.device_name)
        if result:
            # Gerät löschen
            self.db_connector.remove(doc_ids=[result[0].doc_id])
            print(f"Device '{self.device_name}' deleted.")
        else:
            print(f"Device '{self.device_name}' not found.")

    def set_managed_by_user_id(self, managed_by_user_id: str):
        """Expects `managed_by_user_id` to be a valid user id that exists in the database."""
        self.managed_by_user_id = managed_by_user_id

    # Class method that can be called without an instance of the class to construct an instance of the class
    @classmethod
    def find_by_attribute(cls, by_attribute: str, attribute_value: str, num_to_return=1):
        # Load data from the database and create an instance of the Device class
        DeviceQuery = Query()
        result = cls.db_connector.search(DeviceQuery[by_attribute] == attribute_value)

        if result:
            data = result[:num_to_return]
            device_results = [cls(d['device_name'], d['managed_by_user_id'], d['description'], d['image_url'], d['category']) for d in data]
            return device_results if num_to_return > 1 else device_results[0]
        else:
            return None

    @classmethod
    def find_all(cls) -> list:
        # Load all data from the database and create instances of the Device class
        devices = []
        for device_data in Device.db_connector.all():
            devices.append(Device(device_data['device_name'], device_data['managed_by_user_id'], device_data['description'], device_data['image_url'], device_data['category']))
        return devices
