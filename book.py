class Book:
    def __init__(self,title,author,isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

    def __str__(self):
        availability = "available" if self.available else "not available"
        return f"title : {self.title} , author : {self.author} , isbn : {self.isbn} , availability : {availability}"