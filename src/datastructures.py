
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

#class definition, FamilyStructure is the class name
class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [{
                "first_name": "John",
                "last_name": self.last_name,
                "id": 1,
                "age": 33,
                "lucky_numbers": [7, 13, 22]
            },
            {
                "first_name": "Jane",
                "last_name": self.last_name,
                "id": self._generateId(),
                "age": 35,
                "lucky_numbers": [10, 14, 3]
            },
            {
                "first_name": "Jimmy",
                "last_name": self.last_name,
                "id": self._generateId(),
                "age": 5,
                "lucky_numbers": [1]
            }]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # fill this method and update the return
        member["id"] = member.get("id", self._generateId())            
        member["last_name"] = self.last_name
        self._members.append(member)
        return member
        pass

    def delete_member(self, id):
        # fill this method and update the return
        for member in self._members:
            if id == member["id"]:
                self._members.remove(member)
                return True
        return False
        pass

    def get_member(self, id):
        # fill this method and update the return
        for member in self._members:
            if member["id"] == id:
                return member
        return None
        pass

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
