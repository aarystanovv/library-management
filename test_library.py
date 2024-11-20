import unittest
from library import Library

class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_data.json"
        self.library = Library(data_file=self.test_file)
        self.library.books = []
        self.library.save_books()

    def tearDown(self):
        self.library.books = []
        self.library.save_books()

    def test_add_book(self):
        self.library.add_book("Test Book", "Test Author", 2023)
        self.assertEqual(len(self.library.books), 1)
        self.assertEqual(self.library.books[0].title, "Test Book")

    def test_remove_book(self):
        self.library.add_book("Test Book", "Test Author", 2023)
        self.library.add_book("Another Book", "Another Author", 2022)
        self.library.remove_book(1)
        self.assertEqual(len(self.library.books), 1)
        self.assertEqual(self.library.books[0].title, "Another Book")

    def test_search_books_by_title(self):
        self.library.add_book("Searchable Title", "Author", 2021)
        self.library.add_book("Unrelated Title", "Author", 2021)
        results = [book.title for book in self.library.search_books("Searchable")]
        self.assertIn("Searchable Title", results)
        self.assertNotIn("Unrelated Title", results)

    def test_search_books_by_author(self):
        self.library.add_book("Book One", "Special Author", 2020)
        self.library.add_book("Book Two", "General Author", 2020)
        results = [book.author for book in self.library.search_books("Special")]
        self.assertIn("Special Author", results)
        self.assertNotIn("General Author", results)

    def test_search_books_by_year(self):
        self.library.add_book("Book One", "Author", 2020)
        self.library.add_book("Book Two", "Author", 2021)
        results = [book.year for book in self.library.search_books("2020")]
        self.assertIn(2020, results)
        self.assertNotIn(2021, results)

    def test_update_status(self):
        self.library.add_book("Book to Update", "Author", 2023)
        self.library.update_status(1, "issued")
        self.assertEqual(self.library.books[0].status, "issued")

    def test_list_books(self):
        self.library.add_book("Book One", "Author One", 2023)
        self.library.add_book("Book Two", "Author Two", 2022)
        books = [book.title for book in self.library.books]
        self.assertIn("Book One", books)
        self.assertIn("Book Two", books)

if __name__ == "__main__":
    unittest.main()
