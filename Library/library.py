class Library:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.books = []

    def num(self): #shows the number of books currently in the library
        return f"{len(self.books)} books in {self.name}"

    def add(self, book): #adds a book to the library and shows how much space is left
        if len(self.books) < self.capacity:
            self.books.append(book)
            print(f"Added {book} to {self.name}")
            space_left = self.capacity - len(self.books)
            print(f"Space left in {self.name}: {space_left}")
        else:
            print(f"{self.name} is full!")

    def list_books(self): #list all book currently in the library
        print(f"Books in {self.name}:\n")
        for index, book in enumerate(self.books, start=1):
            print(f"{index}. {book}")

    def remove(self, book): #remove book from library
        if book in self.books:
            removed_book = book
            self.books.remove(book)
            print(f"Removed {removed_book.title} from {self.name}")
        else:
            print(f"{book.title} is not in {self.name}")
    
    def clear(self):
        num_books = len(self.books)
        self.books.clear()
        print(f"{num_books} book(s) removed from {self.name}")