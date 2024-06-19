class Person:
    def __init__(self,name,person_id):
        self.name = name
        self.person_id = person_id
    
    def __str__(self):
        return f"name : {self.name} , id : {self.person_id}"

