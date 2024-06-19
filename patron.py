from main import Person
from book import *

class Patron(Person):
    def __init__(self,name,patron_id):
        super().__init__(name,patron_id)
        self.borrowed_books = []

    def __str__(self):
        borrowed_book_titles = ", ".join([i for i in self.borrowed_books])
        return f"patron name : {self.name} , patron id : {self.patron_id} borrowed books : {borrowed_book_titles}"

    def borrow_book(self,library,book):
        if book.available:
            self.borrowed_books.append(book)
            book.available = False
            print(f"{self.name} borrowed {book.title}")
        else:
            print(f"book {book.name} is not available")

    def return_book(self,book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.available = True
            print(f"{self.name} returned {book.title}")
        else:
            print(f"{book.title} is not at {self.name}")


