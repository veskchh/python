from book import Book
from library import Library
import time

while True:
    lib_name = input("What is the name of the library?: ").strip()
    if not lib_name:
        print("\nLibrary name cannot be empty!")
        continue

    try:
        lib_capcacity = int(input(f"What is the capacity of {lib_name}?: "))
    except:
        print("Capacity must be a number!")
        continue

    if lib_name.strip() and 0 < lib_capcacity:
        library = Library(lib_name, lib_capcacity)
        break
    else:
        print("\nEnter valid arguments for name and capacity!")
        time.sleep(1)

print(f"Created library with name: {lib_name} and capacity: {lib_capcacity}")
time.sleep(1)

while True:
    print("\nLibrary Menu:")
    print("1. Add Book")
    print("2. List Books")
    print("3. Remove Book")
    print("4. Check Number of Books")
    print("5. Clear Library")
    print("6. Exit")

    choice = int(input("Choose an option: "))
    if not 1 <= choice <= 6:
        print("Choose valid option(1-6)")
        time.sleep(1)
    
    if choice == 1:
        title = input("Enter book title: ") #name of book to add
        genre = input("Enter book genre: ") #genre of book
        page_count = int(input("Enter page count: ")) #number of pages
        book = Book(title, genre, page_count)
        library.add(book)
    elif choice == 2:
        library.list_books() #list all books
    elif choice == 3:
        title = input("Enter the title of the book to remove: ") #enter the title of the book to remove
        book_to_remove = next((book for book in library.books if book.title == title), None) #generator with next() to check if there is a book with said title
        if book_to_remove: #remove if book is found
            library.remove(book_to_remove)
        else:
            print(f"Book titled '{title}' not found.")
    elif choice == 4:
        library.num()
    elif choice == 5:
        library.clear()
    elif choice == 6:
        print("Exiting ...")
        time.sleep(1)
        break