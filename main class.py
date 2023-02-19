class Book:
    def __init__(self, title,author,copiesAvailable,copiesBorroed,loanPeriod):

        #Initalization
        self.title = title
        self.author = author
        self.copiesAvailable = copiesAvailable
        self.copiesBorroed = copiesBorroed
        self.loanPeriod = loanPeriod

    # Getters
    def getTitle(self):
        return self.title

    # Setters
    def setTitle(self,value):
        self.title = value

class User:
    def __init__(self, name,id, bookBorrowed,email ):
        self.name = name
        self.id = id
        self.bookBorrowed = bookBorrowed
        self.email = email


# common
    def searchBook(self,booktitle):

        print(f"this Book {booktitle} is not found")
        print(f"this Book {booktitle} is  found")
        return None


class NormalUser:
    def __init__(self,noraml_user_name, normal email):
        super().__init__(noraml_user_name, id, email, )

    def borrowBook (self, book):
        print (f"{self.name} has booroed the book {book.title}")

    def returnBook (self, book):
        print(f"{self.name} has booroed the book {book.title}")


class Librarian(User):
   def __init__(self,name,id, bookBorrowed, email):
       super().__init__(name,id, bookBorrowed)
       self.email = email
        #pass






m.print_class()






