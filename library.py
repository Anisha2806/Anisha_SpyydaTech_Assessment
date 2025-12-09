library={}

def add():
    title=input("enter book title: ")
    author=input("enter book author: ")
    library[title]={"author": author, "available": True}
    print("book added")

def search():
    title=input("enter book title to search: ")
    if title in library:
        book=library[title]
        if book["available"]:
            print("book is available")
        else:
            print("book is not available")
        print(f"Title: {title}, Author: {book['author']}")
    else:
        print("book not found")

def borrow():
    title=input("enter book title to borrow: ")
    if title in library:
        if library[title]["available"]:
            library[title]["available"]=False
            print("you have borrowed the book")
        else:
            print("book is not available")
    else:
        print("Book not found")

def return_book():
    title=input("enter book title to return: ")
    if title in library:
        library[title]["available"]=True
        print("you have returned the book")
    else:
        print("book not found")

def menu():
    while True:
        print("\nLibrary Menu:")
        print("1. Add book")
        print("2. Search book")
        print("3. Borrow book")
        print("4. Return book")
        print("5. exit")
        choice=input("enter your choice: ")
        if choice=="1":
            add()
        elif choice=="2":
            search()
        elif choice=="3":
            borrow()
        elif choice=="4":
            return_book()
        elif choice=="5":
            print("exiting the library system.")
            break
        else:
            print("invalid choice, please try again.")


if __name__=="__main__":
    menu()