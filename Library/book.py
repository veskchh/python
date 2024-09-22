class Book:
    def __init__(self, title, genre, page_count):
        if page_count < 0: #checks if page count is valid
            raise ValueError("Page count must be a non-negative integer.")
        self.title = title
        self.genre = genre
        self.page_count = page_count
    
    def __str__(self): 
        return f"{self.title} - Genre: {self.genre} - Page count: {self.page_count}"
    
    def __repr__(self):
        return f"Book(title='{self.title}', genre='{self.genre}', page_count={self.page_count})"