from membership import Membership
class Library :

    def __init__(self):
        self.books =[]
        self.members=[]


    def add_book(self , book ):
        self.books.append(book)
        print("book has been added successfully")

    def remove_book (self , index ):
        if 0<= index <len(self.books):
            del self.books[index]

    def view_books(self):
        for i , book in enumerate(self.books):
            print(f"{i}-{book}")

    def add_member(self , member ):
        self.members.append(member)
        print("member has been added successfully")

    def remove_member (self , index ):
        if 0<=index <len(self.members):
            del self.members[index]

    def view_member(self):
        for i , member in enumerate(self.members):
            print(f"{i}-{member}")



    def borrow_book(self , member_index , book_index):
        if 0<= member_index<len(self.members) and 0<= book_index<len(self.members):
            member= self.members[member_index]
            book = self.books[book_index]
            member.borrow_book(book)
        else:
            print("invalid index ")

    def return_book(self , member_index , book_index):
        if 0<= member_index<len(self.members) and 0<= book_index<len(self.members):
            member= self.members[member_index]
            book = self.books[book_index]
            member.return_book(book)
        else:
            print("invalid index ")









