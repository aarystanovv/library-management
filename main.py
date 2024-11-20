from library import Library

def main():
    library = Library()

    while True:
        print("\nMenu:")
        print("1. Add a book")
        print("2. Delete a book")
        print("3. Search a book")
        print("4. Show all books")
        print("5. Change the status of the book")
        print("6. Exit")

        choice = input("Select an action: ")
        if choice == "1":
            title = input("Enter the name of the book: ")
            author = input("Enter the author of the book: ")
            year = int(input("Enter the year of publication of the book: "))
            library.add_book(title, author, year)
        elif choice == "2":
            book_id = int(input("Enter the book ID: "))
            library.remove_book(book_id)
        elif choice == "3":
            keyword = input("Enter the title, author, or year of publication of the book: ")
            library.search_books(keyword)
        elif choice == "4":
            library.list_books()
        elif choice == "5":
            book_id = int(input("Enter the book ID: "))
            new_status = input("Enter the new status (available/issued): ")
            library.update_status(book_id, new_status)
        elif choice == "6":
            print("Exiting the program.")
            break
        else:
            print("Wrong choice. Try again.")

if __name__ == "__main__":
    main()
