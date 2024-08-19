from book import Book
class Membership:

    def __init__(self , member_name , member_ID ):
        self.member_name=member_name
        self.member_ID =member_ID
        self.borrow =[]

    def borrow_book(self,book):
        if not book.borrowed:
            self.borrow.append(book)
            book.borrowed = True
            print(f"book :{book.name} , is borrowed to : {self.member_name} succesfully ")
        else:
            print("sorry book is not available")

    def return_book(self,book):
        if book in self.borrow:
            self.borrow.remove(book)
            book.borrowed = False
            print(f"book:{book.name} , is returned ")
        else:
            print("book is not in record")

    def __str__(self):
        return f"The member: {self.member_name}, holder id : {self.member_ID} , book borrowed : {self.borrow}  "







