#!/usr/bin/env python3

class Book:
    """Represents a book with a title and page count.
    
    This class models a book object with attributes for tracking
    the title and the total number of pages.
    """
    
    def __init__(self, title, page_count):
        """Initialize a Book instance.
        
        Args:
            title (str): The title of the book
            page_count (int): The total number of pages in the book
        """
        self.title = title
        self.page_count = page_count

    @property
    def page_count(self):
        """Get the page count of the book.
        
        Returns:
            int: The total number of pages
        """
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        """Set the page count with validation.
        
        Ensures that page_count is an integer. If a non-integer value
        is provided, prints an error message.
        
        Args:
            value: The value to set as page_count
        """
        if not isinstance(value, int):
            print("page_count must be an integer")
        self._page_count = value

    def turn_page(self):
        """Simulate turning a page in the book.
        
        Prints a message to indicate the user is reading quickly.
        """
        print("Flipping the page...wow, you read fast!")
