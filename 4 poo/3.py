from typing import List

class Book:
    def __init__(self, tittle: str, author: str):
        self.tittle = tittle
        self.author = author
        self.available = True
        
    def borrow(self):
        if not self.available:
            print(f"El libro {self.tittle} no esta disponible")
            return 
            
        self.available = False
        print(f"El libro {self.tittle} ha sido prestado")
        
    def return_book(self):
        self.available = True
        print(f"El libro {self.tittle} ha sido debuelto")
        
class User:
    def __init__(self, name: str, user_id: int):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []
        
    def borrow_book(self, book: Book):
        if not book.available:
            print(f"El libro {book.tittle} no esta disponible")
            return
            
        book.borrow()
        self.borrowed_books.append(book)
        
    def return_book(self, book: Book):
        if not book in self.borrowed_books:
            print(f"El libro {book.tittle} no esta en la lista de guardados")
            return
            
        book.return_book()
        self.borrowed_books.remove(book)
        
class Library:
    def __init__(self):
        self.books: List[Book] = [] 
        self.users: List[User] = []
        
    def add_book(self, book: Book):
        self.books.append(book)
        print(f"El libro {book.tittle} ha sido agregado")
        
    def add_user(self, user: User):
        self.users.append(user)
        print(f"El usuario {user.name} ha sido registradp")
        
    def show_available_books(self):
        print('Libros disponibles:')
        for book in self.books:
            if(book.available):
                print(f"  {book.tittle} por {book.author}")

# Crear los libros
book1 = Book("El principito", "Antoine de Saint-Exupéry")
book2 = Book("1984", "George Orwell")

# Crear usuario
user1 = User("Carli", "001")

# Crear Biblioteca
library = Library()

library.add_book(book1)
library.add_book(book2)
library.add_user(user1)

# Mostrar libros
library.show_available_books()

# Realizar prestamo
user1.borrow_book(book1)

# Mostrar libros
library.show_available_books()

# devolver libro
user1.return_book(book1)

# Mostrar libros
library.show_available_books()