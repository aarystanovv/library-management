# Library Management System

This is a simple **console-based library management system** built in Python. The application allows users to manage books in a library, including adding, deleting, searching, viewing, and updating the status of books.

---

## Features

1. **Add a Book**:  
   Users can add a new book by providing its title, author, and publication year. A unique ID and default status ("available") will be automatically assigned to the book.

2. **Delete a Book**:  
   Users can remove a book from the library by providing its unique ID.

3. **Search for Books**:  
   Search functionality allows users to find books by title, author, or publication year.

4. **View All Books**:  
   Display all books in the library, including their ID, title, author, publication year, and status.

5. **Update Book Status**:  
   Users can change the status of a book (e.g., "available" or "issued") by providing its unique ID and the new status.

6. **Data Persistence**:  
   Book data is stored in a JSON file (`data.json`) for persistence across program runs.

---

## Getting Started

### Prerequisites
- Python 3.8 or higher.

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repository/library-management.git
   cd library-management
2. If not present, create an empty file named data.json:
   ```bash
   echo "[]" > data.json

## Running the Application
1. Run the application using:

    ```bash
    python main.py

2. You will see the following menu:
    ```bash
    Menu:
   1. Add a book
   2. Delete a book
   3. Search a book
   4. Show all books
   5. Change the status of the book
   6. Exit

3. Select an option by entering the corresponding number and following the prompts.

## Example Usage
### Adding a Book
    Menu:
    1. Add a book
    2. Delete a book
    3. Search a book
    4. Show all books
    5. Change the status of the book
    6. Exit

    Select an action: 1
    Enter the name of the book: Crime and Punishment
    Enter the author of the book: Fyodor Dostoevsky
    Enter the year of publication of the book: 1866
    Book 'Crime and Punishment' successfully added with ID 1.

### Viewing All Books
    Menu:
    4. Show all books

    ID: 1, Title: Crime and Punishment, Author: Fyodor Dostoevsky, Year: 1866, Status: available

### Updating Book Status
    Menu:
    5. Change the status of the book

    Enter the book ID: 1
    Enter the new status (available/issued): issued
    The status of the book with ID 1 updated to 'issued'.

### Testing
Unit tests are provided in test_library.py. To run the tests, execute:

    python -m unittest test_library.py

### Future Enhancements
1. Add a graphical user interface (GUI) for better user experience.
2. Enhance search functionality to support partial matches and multiple filters.
3. Implement user roles for library staff and patrons.




