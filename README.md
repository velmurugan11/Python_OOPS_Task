# Python_OOPS_Task

OOPS_TASK1

Task: Build a Simple Library Management System
Objective:
Apply OOP concepts such as classes, objects, inheritance, encapsulation, polymorphism, and abstraction.

Requirements:
Classes to Implement:

Book:
  Attributes: 
    title, author, isbn, availability (boolean).
  Methods:
    __init__(...): Initialize book details.
    __str__(...): Return a string representation of the book details.
Member:
  Attributes: 
    name, member_id, borrowed_books (list of books).
  Methods:
    borrow_book(book): Borrow a book if available.
    return_book(book): Return a book.
Library:
  Attributes: 
    books (list of all books), members (list of all members).
  Methods:
    add_book(book): Add a book to the library.
    add_member(member): Add a member to the library.
    search_book(title): Search for a book by title.
    list_books(): List all books in the library.
    lend_book(member_id, book_title): Allow a member to borrow a book.
    accept_return(member_id, book_title): Allow a member to return a book.
Additional Details:

  Use encapsulation to make attributes private and provide getter/setter methods where necessary.
  Use inheritance to create a specialized class, e.g., PremiumMember (inherits from Member) that allows borrowing more books.
  Implement polymorphism using method overriding, e.g., __str__ for different classes.

Example Scenario to Implement:

  Add books like "Python Programming" by John Zelle and "Artificial Intelligence" by Peter Norvig.
  Add members and allow them to borrow or return books.
  Handle edge cases like borrowing an unavailable book or returning a book not borrowed.



OOPS_TASK2

👉🏻Create a class called Person with attributes name and age. Add a method introduce that prints a message introducing the person.

👉🏻Define a class called Car with attributes brand and color. Add a method start that prints a message saying the car has started.

👉🏻Create a class Student with attributes name and grades (a list of numbers). Add a method average_grade that calculates and returns the average of the grades.

👉🏻Define a class Rectangle with attributes length and width. Add methods area and perimeter to calculate the area and perimeter of the rectangle.

👉🏻Implement a class BankAccount with attributes account_number and balance. Add methods deposit and withdraw to update the balance.

👉🏻Create a class Animal with a method speak that prints "Animal sound". Create two subclasses, Dog and Cat, that override the speak method with specific sounds.

👉🏻Define a class Employee with attributes name, position, and salary. Add a method display_info that prints all the employee details.

👉🏻Implement a class Circle with an attribute radius. Add methods to calculate the circle's area and circumference.

👉🏻Create a class Book with attributes title, author, and price. Add a method apply_discount that reduces the price by a given percentage.

👉🏻Define a class Shape with a method description that prints "This is a shape." Create subclasses Square and Triangle that override the description method with their specific names.
