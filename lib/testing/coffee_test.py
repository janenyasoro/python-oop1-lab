import io
import sys
from coffee import Coffee

class TestCoffee:
    '''Coffee in coffee.py'''

    def test_has_size_and_price(self):
        '''has the size and price passed into __init__, and values can be set to new instance.'''
        coffee = Coffee("Large", 4.50)
        assert(coffee.size == "Large")
        assert(coffee.price == 4.50)

    def test_requires_valid_size(self):
        '''prints "size must be Small, Medium, or Large" if size is not Small, Medium, or Large.'''
        coffee = Coffee("Medium", 3.75)
        captured_out = io.StringIO()
        sys.stdout = captured_out
        coffee.size = "Extra Large"
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == "size must be Small, Medium, or Large\n"

    def test_can_tip(self):
        '''increases price by 1 when method tip() is called'''
        coffee = Coffee("Small", 3.00)
        coffee.tip()
        assert(coffee.price == 4.00)

    def test_tip_output(self):
        '''outputs "This coffee is great, here's a tip!" when method tip() is called'''
        coffee = Coffee("Large", 5.00)
        captured_out = io.StringIO()
        sys.stdout = captured_out
        coffee.tip()
        sys.stdout = sys.__stdout__
        assert(captured_out.getvalue() == "This coffee is great, here's a tip!\n")