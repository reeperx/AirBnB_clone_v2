#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'  # Path to the JSON file
    __objects = {}  # Dictionary to store objects
    def delete(self, obj=None):
        """ 
        Deletes an object from the __objects dictionary if it exists.
        
        Args:
            obj (object, optional): The object to be deleted. If None, no action is taken.
        """
        if obj is not None:
            obj = f'{obj.__class__.__name__}.{obj.id}'  # Create a key for the object
            del (self.__class__.__objects[obj])  # Delete the object from the dictionary
            self.save()  # Save the updated dictionary to the JSON file
    def all(self, cls=None):
        """
        Returns a dictionary of models currently in storage.

        Args:
            cls (class, optional): If provided, only instances of this class will be returned.

        Returns:
            dict: A dictionary of model instances, or a filtered dictionary if cls is provided.
        """
        if cls is not None:
            filtered = {}
            for k, v in FileStorage.__objects.items():
                if cls.__name__ == v.__class__.__name__:
                    filtered[k] = v
            return filtered
        return FileStorage.__objects

    def new(self, obj):
        """
        Adds a new object to the storage dictionary.

        Args:
            obj (object): The object to be added.
        """
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})
    def save(self):
        """
        Serializes the __objects dictionary to the JSON file.
        """
        temp = {}
        for key, val in self.__objects.items():
            temp[key] = val.to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(temp, f)

    def reload(self):
        """
        Deserializes the JSON file to the __objects dictionary.
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        classes = {"BaseModel": BaseModel, "User": User, "Place": Place, "State": State, "City": City}
        try:
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except Exception:
            pass
