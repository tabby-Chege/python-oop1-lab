#!/usr/bin/env python3

class Coffee:
    # Represents a coffee beverage with size and price
    
    def __init__(self, size, price):
        # Initialize with size and price
        self.size = size
        self.price = price

    @property
    def size(self):
        # Get the size of the coffee
        return self._size

    @size.setter
    def size(self, value):
        # Validate size is one of: Small, Medium, Large
        if value not in {"Small", "Medium", "Large"}:
            print("size must be Small, Medium, or Large")
        self._size = value

    def tip(self):
        # Add $1 to price and print thank you message
        print("This coffee is great, here's a tip!")
        self.price += 1
