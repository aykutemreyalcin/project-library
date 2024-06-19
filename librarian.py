from main import Person

class Librarian(Person):
    def __init__(self,name,librarian_id):
        super().__init__(name,librarian_id)

    def __str__(self):
        return f"librarian name : {self.name} , librarian id : {self.librarian_id}"
    
    def add_book(self,library,book):
        print(f"{self.name} added {book.title} to the library")
        library.add_book(book)

    def remove_book(self,library,book):
        library.remove_book(book)
        print(f"{self.name} removed {book.title} from the library")

    def add_patron(self,library,python):
        library.add_patron(patron)
        print(f"{self.name} added patron {patron.name} to the library")

    def remove_patron(self,library,patron):
        library.remove_patron(patron)
        print(f"{self.name} removed patron {patron.name} from the library")
        
    