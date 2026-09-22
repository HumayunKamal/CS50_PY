from .data import loans
from .books import find_book
from .members import find_member

def borrow_book(book_id, member_id):
    book = find_book(book_id)
    member = find_member(member_id)

    if book is None:
        return None, "Book not found"
    if member is None:
        return None, "Member not found"
    if not book["available"]:
        return None, "Book is not available for borrowing"

    book["available"] = False

    loan = {
        "id": len(loans) + 1,
        "book_id": book_id,
        "member_id": member_id,
        "returned": False,
    }

    loans.append(loan)

    return loan

def return_book(book_id):
    book = find_book(book_id)

    if book is None:
        return None, "Book not found"
    for loan in loans:
        if loan["book_id"] == book_id and not loan["returned"]:
            loan["returned"] = True
            book["available"] = True
            return loan
    return None, "No active loan found for this book"

def get_loans():
    return loans
