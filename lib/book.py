#!/usr/bin/env python3

class Book:
    # Represents a book with a title and page count
    
    def __init__(self, title, page_count):
        # Initialize with title and page count
        self.title = title
        self.page_count = page_count

    @property
    def page_count(self):
        # Get the page count
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        # Validate page_count is an integer
        if not isinstance(value, int):
            print("page_count must be an integer")
        self._page_count = value

    def turn_page(self):
        # Simulate turning a page
        print("Flipping the page...wow, you read fast!")
