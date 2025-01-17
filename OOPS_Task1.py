# Build a simple library management system.
# class,objects,inheritance,encapsulation,abstraction,polymorphism.
class Book:
    def __init__(self,title,author,isbn):
        self.__title=title
        self.__author=author
        self.__isbn=isbn
        self.__availability=True
    
    @property
    def title(self):
        return self.__title
    
    @property
    def author(self):
        return self.__author
    
    @property
    def isbn(self):
        return self.__isbn

    @property
    def availability(self):
        return self.__availability
    
    @availability.setter
    def availability(self,status):
        self.__availability=status
     
    def __str__(self):
        availability_status = "Available" if self.__availability else "Not Available"
        return f"Book_Title: {self.__title}\nAuthor: {self.__author}\nISBN: {self.__isbn}\nAvailability: {availability_status}"

# Creating the Member class
class Member():
    def __init__(self,name,member_id):
        self.__name=name
        self.__member_id=member_id
        self.__borrowed_books=[]

    # Method for borrowing the books
    def borrow_book(self,book):
        if Book.availability:
            self.__borrowed_books.append(Book)
            Book.availability=False
            print(f"{self.__name} has successfully borrowed books '{book.title}'")
        else:
            print(f"Sorry, '{book.title}' is currently unavailable.")
    
    def return_book(self,book):
        if book in self.__borrowed_books:
            self.__borrowed_books.remove(book)
            book.availability=True
            print(f"{self.__name} has returned '{book.title}'.")
        else:
            print(f"{self.__name} cannot return '{book.title}'as it was not borrewed.")

    def get_borrowed_books(self):
        return [book.title for book in self.__borrowed_books]
    
    def __str__(self):
        borrowed_books = ", ".join(self.get_borrowed_books()) if self.__borrowed_books else "None"
        return f"Member Name: {self.__name}\nMember ID: {self.__member_id}\nBorrowed Books: {borrowed_books}"
    
    @property
    def name(self):
        return self.__name
    
    @property
    def member_id(self):
        return self.__member_id
    
class Library:
    def __init__(self):
        self.books=[]
        self.members=[]

    def add_book(self,book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library")

    def add_member(self,member):
        self.members.append(member)
        print(f"Member '{member.name}' added to the library")

    def search_book(self,title):
        for book in self.books:
            if book.title.lower()==title.lower():
                return book
        return None
    
    def list_books(self):
        print("\n Books in the library:")
        for book in self.books:
            print(book)
            print("-"*30)

    def lend_book(self,member_id,book_title):
        member = next((m for m in self.members if m.member_id==member_id),None)
        if not member:
            print(f"No member found with ID {member_id}.")
            return
        book = self.search_book(book_title)
        if not book:
            print(f"No book found with the title '{book_title}'.")
            return
        member.borrow_book(book)

    def accept_return(self,member_id,book_title):
        member = next((m for m in self.members if m.member_id==member_id),None)
        if not member:
            print(f"No member found with ID {member_id}.")
            return
        book = self.search_book(book_title)
        if not book:
            print(f"No book found with the title '{book_title}'.")
            return
        member.return_book(book)

library=Library()

# Add Books to the library
B1=Book("The Monk Who sold his ferrari","Robin Sharma","B1235")
B2=Book("The Psychology of Money","Morgan Housel","B1236")
B3=Book("The Alchemist","Paulo chaleo","B1237")
B4=Book("The Magic of Thinking Big","Someone","B1238")
B5=Book("Ikigai","Japanese","B1239")
library.add_book(B1)
library.add_book(B2)
library.add_book(B3)
library.add_book(B4)
library.add_book(B5)

# Add members to the library
member1 = Member("Vel","S001")
member2 = Member("Murugan","S002")
library.add_member(member1)
library.add_member(member2)

# List all the books from the library
library.list_books()

# Borrow Books
print("\n---Borrowing Books---")
library.lend_book("S001","The Monk Who sold his ferrari")
library.lend_book("S002","The Alchemist")
library.lend_book("S002","The Monk Who sold his ferrari")

# Returning Books
library.accept_return("S001","The Monk Who sold his ferrari")

# List all the books after borrowing and returning
library.list_books()