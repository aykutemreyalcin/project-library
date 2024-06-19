class Book:
    def __init__(self,title,author,isbn,available):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available

    def __str__(self):
        return f"title : {self.title} , author : {self.author} , isbn : {self.isbn} , availability : {self.available}"
    
    

