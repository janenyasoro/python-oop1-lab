#!/usr/bin/env python3

class Coffee:
    def __init__(self, size, price):
        """Initialize a Coffee object with size and price"""
        self.size = size
        self.price = price
    
    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, value):
        """Ensure size is Small, Medium, or Large"""
        valid_sizes = ["Small", "Medium", "Large"]
        if value not in valid_sizes:
            print("size must be Small, Medium, or Large")
        else:
            self._size = value
    
    def tip(self):
        """Add a tip to the coffee price"""
        print("This coffee is great, here's a tip!")
        self.price += 1