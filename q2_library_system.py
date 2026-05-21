def add_book(catalog, book_id, title, author, year):
    """Adds a new book to the catalog dictionary using an immutable tuple."""
    catalog[book_id] = (title, author, year)
    print(f"Added book: '{title}' [ID: {book_id}]")


def borrow_book(catalog, borrowed_books, book_id):
    """Borrows a book if it exists in the catalog and isn't already borrowed."""
    if book_id not in catalog:
        print(f"Error: Book ID {book_id} does not exist in the catalog.")
    elif book_id in borrowed_books:
        print(f"Error: Book ID {book_id} ('{catalog[book_id][0]}') is already borrowed.")
    else:
        borrowed_books.append(book_id)
        print(f"Successfully borrowed: '{catalog[book_id][0]}'")


def return_book(borrowed_books, book_id):
    """Returns a book by removing its ID from the borrowed list."""
    if book_id in borrowed_books:
        borrowed_books.remove(book_id)
        print(f"Successfully returned Book ID: {book_id}")
    else:
        print(f"Error: Book ID {book_id} was not marked as borrowed.")


def register_member(members, member_id):
    """Registers a unique member ID using a set (silently ignores duplicates)."""
    members.add(member_id)


def show_available(catalog, borrowed_books):
    """Prints all books that are currently available in the library."""
    print("\n--- Available Books ---")
    available_found = False
    
    for book_id, details in catalog.items():
        if book_id not in borrowed_books:
            title, author, year = details
            print(f"📚 [ID: {book_id}] {title} by {author} ({year})")
            available_found = True
            
    if not available_found:
        print("No books are currently available.")
    print("------------------------")
def main():
    catalog = {}          
    borrowed_books = []    
    members = set()        

    print("--- 1. Adding 4 Books ---")
    add_book(catalog, 101, "The Hobbit", "J.R.R. Tolkien", 1937)
    add_book(catalog, 102, "To Kill a Mockingbird", "Harper Lee", 1960)
    add_book(catalog, 103, "1984", "George Orwell", 1949)
    add_book(catalog, 104, "The Great Gatsby", "F. Scott Fitzgerald", 1925)

    print("\n--- 2. Registering Members (with duplicate attempt) ---")
    register_member(members, "M01")
    register_member(members, "M02")
    register_member(members, "M03")
    register_member(members, "M01") 
    print(f"Registered Members Set: {members} (Notice no duplicates!)")

    print("\n--- 3. Borrowing 2 Books ---")
    borrow_book(catalog, borrowed_books, 101)  
    borrow_book(catalog, borrowed_books, 103)  
    borrow_book(catalog, borrowed_books, 101) 

    print("\n--- 4. Returning 1 Book ---")
    return_book(borrowed_books, 101) 

    print("\n--- 5. Displaying Available Books ---")
    show_available(catalog, borrowed_books)


if __name__ == "__main__":
    main()
