#!/usr/bin/env python3

class Coffee:
    """Represents a coffee beverage with size and price.
    
    This class models a coffee object with attributes for tracking
    the size and price, and supports adding tips to the total price.
    """
    
    def __init__(self, size, price):
        """Initialize a Coffee instance.
        
        Args:
            size (str): The size of the coffee (Small, Medium, or Large)
            price (float): The base price of the coffee
        """
        self.size = size
        self.price = price

    @property
    def size(self):
        """Get the size of the coffee.
        
        Returns:
            str: The size of the coffee
        """
        return self._size

    @size.setter
    def size(self, value):
        """Set the size with validation.
        
        Ensures that size is one of the allowed values: Small, Medium, or Large.
        If an invalid size is provided, prints an error message.
        
        Args:
            value (str): The size value to set
        """
        if value not in {"Small", "Medium", "Large"}:
            print("size must be Small, Medium, or Large")
        self._size = value

    def tip(self):
        """Add a tip to the coffee price.
        
        Prints a message expressing gratitude and adds $1.00 to the price.
        """
        print("This coffee is great, here's a tip!")
        self.price += 1
