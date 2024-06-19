from book import *
from librarian import *
from library import *
from patron import *
from person import *

library = Library("City Library")
book1 = Book("1984", "George Orwell", "123456789")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "987654321")
patron1 = Patron("Emre", "P001")
patron2 = Patron("Yalçın", "P002")
librarian = Librarian("Aykut", "L001")
librarian.add_book(library, book1)
librarian.add_book(library, book2)
librarian.add_patron(library, patron1)
librarian.add_patron(library, patron2)
print("Books in library:")
library.list_books()
print("\nPatrons in library:")
library.list_patrons()
patron1.borrow_book(book1)
print("\nBooks in library after borrowing:")
library.list_books()
print("\nPatrons in library after borrowing:")
library.list_patrons()
patron1.return_book(book1)
print("\nBooks in library after returning:")
library.list_books()
print("\nPatrons in library after returning:")
library.list_patrons()