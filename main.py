from book import Book
from membership import Membership
from library import Library
from register import save_data , load_data



def main():
    filename = "library.pkl"
    library = load_data(filename) or Library()

    while True:
        print("welcome to library code ")
        print('press 1 for books and 2 for members and 3 for exit')
        choice1 = int(input("(1/2): "))
        if choice1 == 1:
            print("welcome to the book side")
            choice =int(input("1 for add / 2 for remove / 3 fr view books : "))
            if choice==1:
                name = input("please enter name of the book: ")
                code= int(input("please enter book code: "))
                author= input("please enter author name : ")
                book = Book(name , code , author)
                library.add_book(book)
            elif choice==2:
                library.view_books()
                index= int(input("enter the index of book u wanna delete: "))
                library.remove_book(index)
            elif choice == 3 :
                library.view_books()

        elif choice1 == 2:
            print("welcome to the member side")
            choice =int(input("1 for add / 2 for remove / 3 for view members/ 4 for borrowing a book /"
                              " 5 for returning book  : "))
            if choice==1:
                member_name = input("please enter name of the member: ")
                member_ID= int(input("please enter member id: "))
                member = Membership(member_name , member_ID )
                library.add_member(member)
            elif choice==2:
                library.view_member()
                index= int(input("enter the index of book u wanna delete: "))
                library.remove_member(index)
            elif choice == 3 :
                library.view_member()
            elif choice == 4 :
                library.view_books()
                index_book=int(input("please enter the index of book u wanna borrow:  "))
                index_member=int(input("please enter the index of member who wanna borrow:  "))
                library.borrow_book(index_book,index_member)
            elif choice == 5 :
                library.view_books()
                library.view_member()
                index_book = int(input("please enter the index of book u wanna return:  "))
                index_member = int(input("please enter the index of member who wanna return:  "))
                library.return_book(index_book, index_member)
            else:
                print('wrong input')




if __name__ == "__main__":
    main()



