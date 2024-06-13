from __init__ import CURSOR, CONN

from owner import Owner

class Property:
    
    def __init__(self,address,owner_id, id= None):
        self.id = id 
        self.adress = address
        self.owner_id = owner_id
        
    @property
    def address(self):
        return self._address
    
    @address.setter
    def address(self,address):
        if isinstance(address,str) and len(address):
            self._address = address
            
        else: 
            raise ValueError(
                "Address must be a non-empty string"
            )
            
    @property
    def owner_id(self):
        return self._owner_id 
    
    @owner_id.setter
    def owner_id(self, owner_id):
        if type(owner_id) is int and Owner.find_by_id(owner_id):
            self._owner_id = owner_id
            
        else:
            raise ValueError(
                " owner_id must reference a owner in the database"
            )
    
    @