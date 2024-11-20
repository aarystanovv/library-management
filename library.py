import json
from typing import List, Optional
from book import Book

class Library:
    def __init__(self, data_file: str = "data.json"):
        self.data_file = data_file
        self.books = self.load_books()

    def load_books(self) -> List[Book]:
        try:
            with open(self.data_file, "r", encoding="utf-8") as file:
                return [Book.from_dict(item) for item in json.load(file)]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_books(self):
        with open(self.data_file, "w", encoding="utf-8") as file:
            json.dump([book.to_dict() for book in self.books], file, ensure_ascii=False, indent=4)

    def add_book(self, title: str, author: str, year: int):
        new_id = max((book.id for book in self.books), default=0) + 1
        book = Book(new_id, title, author, year)
        self.books.append(book)
        self.save_books()
        print(f"Book '{title}' successfully added with ID {new_id}.")

    def remove_book(self, book_id: int):
        self.books = [book for book in self.books if book.id != book_id]
        self.save_books()
        print(f"Book with ID {book_id} deleted.")

    def search_books(self, keyword: str) -> List[Book]:
        result = [
            book for book in self.books
            if keyword.lower() in book.title.lower() or
               keyword.lower() in book.author.lower() or
               keyword == str(book.year)
        ]
        if result:
            for book in result:
                print(
                    f"ID: {book.id}, Title: {book.title}, Author: {book.author}, Year: {book.year}, Status: {book.status}")
        else:
            print("No books were found.")
        return result

    def list_books(self):
        if not self.books:
            print("The library is empty.")
        for book in self.books:
            print(f"ID: {book.id}, Title: {book.title}, Author: {book.author}, Year: {book.year}, Status: {book.status}")

    def update_status(self, book_id: int, new_status: str):
        for book in self.books:
            if book.id == book_id:
                book.status = new_status
                self.save_books()
                print(f"The status of the book with ID {book_id} updated to '{new_status}'.")
                return
        print(f"Book with ID {book_id} not found.")
