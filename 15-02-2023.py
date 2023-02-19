class Book:
    def __init__(self, title,author,copiesAvailable,copiesBorroed,loanPeriod):
        self.title = title
        self.author = author
        self.copiesAvailable = copiesAvailable
        self.copiesBorroed = copiesBorroed
        self.loanPeriod = loanPeriod

class User:
    def __init__(self, name,id, bookBorrowed,email ):
        self.name = name
        self.id = id
        self.bookBorrowed = bookBorrowed
        self.email = email
    def borrowBook (self, book):
        print (f"{self.name} has booroed the book {book.title}")

    def returnBook (self, book):
        print(f"{self.name} has booroed the book {book.title}")

    def searchBook(self,booktitle):

        print(f"this Book {booktitle} is not found")
        print(f"this Book {booktitle} is  found")
        return None









