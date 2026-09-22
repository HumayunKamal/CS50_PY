from .data import books

def add_book(title, author, isbn):
    book = {
        "id": len(books) + 1,
        "title": title,
        "author": author,
        "isbn": isbn,
        "available": True,
    }

    book.append(book)
    return book

def get_books():
    return books


def find_book(book_id):
    for book in books:
        if book["id"] == book_id:
            return book
    return None

def delete_book(book_id):
    book = find_book(book_id)
    if book is None:
        return False

    books.remove(book)
    return True

def calculate_available_books():
    return sum(book["available"] for book in books)
