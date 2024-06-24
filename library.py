class Library:
    def __init__(self,name):
        self.name = name
        self.books = []
        self.patrons = []

    def add_book(self,book):
        self.books.append(book)

    def remove_book(self,book):
        self.books.remove(book)

    def add_patron(self,patron):
        self.patrons.append(patron)
    
    def remove_patron(self,patron):
        self.patrons.remove(patron)
    
    def list_books(self):
        for i in self.books:
            print(i)

    def list_patrons(self):
        for i in self.books:
            print(i)