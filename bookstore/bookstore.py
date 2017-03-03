class Bookstore(object):
    def __init__(self, name):
        self.name = name #bookstore name 
        self.books =[]
        
    def get_books(self):
        return self.books
        
    def add_book(self, book):
        self.books.append(book)
        return book
    
    def search_books(self, title = None, author = None):
        search_result =[]
        for this_book in self.books:
            if title is not None and title.lower() in this_book.title.lower(): 
                search_result.append(this_book)
            if author is not None and author == this_book.author:
                search_result.append(this_book)
        return search_result
            
class Author(object):
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality
        self.books =[]
        
    def add_book(self, book):
        self.books.append(book)
        
    def get_books(self):
        return self.books
        
class Book(object):
    def __init__(self, title, author):
        self.title = title
        self.author = author
        author.add_book(self)
    