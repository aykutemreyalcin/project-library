from main import Person

class Patron:
    def __init__(self,name,patron_id):
        self.name = name
        self.patron_id = patron_id

    def __str__(self):
        return f"patron name : {self.name} , patron id : {self.patron_id}"

    def borrow_book(self,library,book):
        pass

    def return_book(self,book):
        pass

