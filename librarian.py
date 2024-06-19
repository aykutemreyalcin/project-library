from main import Person

class Librarian(Person):
    def __init__(self,name,librarian_id):
        self.name = name
        self.librarian_id = librarian_id
    
    def __str__(self):
        return f"librarian name : {self.name} , librarian id : {self.librarian_id}"
    
    def add_book(self,library,book):
        pass

    def remove_book(self,library,book):
        pass

    def add_patron(self,library,python):
        pass

    def remove_patron(self,library,patron):
        pass
    