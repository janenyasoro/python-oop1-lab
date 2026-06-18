from lib.book import Book
from lib.coffee import Coffee

# Test Book
print("=== Testing Book ===")
book = Book("The Great Gatsby", 180)
print(f"Book title: {book.title}")
print(f"Book pages: {book.page_count}")
book.turn_page()
print()

# Test invalid page count
print("Testing invalid page count:")
book.page_count = "not a number"

print("\n=== Testing Coffee ===")
coffee = Coffee("Medium", 3.50)
print(f"Coffee size: {coffee.size}")
print(f"Coffee price: ${coffee.price:.2f}")
coffee.tip()
print(f"New price with tip: ${coffee.price:.2f}")
print()

# Test invalid size
print("Testing invalid size:")
coffee.size = "Extra Large"