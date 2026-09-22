from fastapi import FastAPI, HTTPException

# Imports
from app.models import BookCreate, MemberCreate, LoanCreate

from app.books import (
    add_book,
    get_books,
    find_book,
    delete_book,
    calculate_available_books,
)

from app.members import add_member, get_members, find_member
from app.loan import borrow_book, return_book, get_loans

# App initialization
app = FastAPI(
    title="Library Management System",
)


# Query Functions
def search_books(query: str):
    results = []

    query = query.lower()

    for book in get_books():
        if query in book["title"].lower() or query in book["author"].lower():
            results.append(book)
    return results


def count_borrowed_books():
    return len(get_books()) - calculate_available_books()


def get_statistics():
    return {
        "total_books": len(get_books()),
        "available_books": calculate_available_books(),
        "borrowed_books": count_borrowed_books(),
        "total_members": len(get_members()),
        "total_loans": len(get_loans()),
    }


# Book Routing
@app.get("/")
def home():
    return {"message": "Welcome to the Library Management System!"}


@app.get("/books")
def books():
    return get_books()


@app.post("/books")
def create_book(book: BookCreate):
    return add_book(book.title, book.author, book.year)


@app.get("/books/{book_id}")
def get_single_book(book_id: int):
    book = find_book(book_id)

    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@app.delete("/books/{book_id}")
def remove_book(book_id: int):
    if not delete_book(book_id):
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": "Book deleted successfully"}


@app.get("/books/search")
def search(query: str):
    return search_books(query)


# Member Routing
@app.get("/members")
def members():
    return get_members()


@app.post("/members")
def create_member(member: MemberCreate):
    return add_member(member.name, member.email)


@app.get("/members/{member_id}")
def get_single_member(member_id: int):
    member = find_member(member_id)

    if member is None:
        raise HTTPException(status_code=404, detail="Member not found")
    return member


# Loan Routing
@app.get("/loans")
def loans():
    return get_loans()


@app.post("/loans/borrow")
def borrow(loan: LoanCreate):
    result = borrow_book(loan.book_id, loan.member_id)

    if result is None:
        raise HTTPException(status_code=400, detail="Unable to borrow book")

    return result


@app.post("/loans/return/{book_id}")
def return_book_route(book_id: int):
    result = return_book(book_id)

    if result is None:
        raise HTTPException(status_code=400, detail="Unable to return book")

    return result


# Statistics Routing
@app.get("/statistics")
def statistics():
    return get_statistics()


# Main
def main():
    print("Starting the Library Management System...")


if __name__ == "__main__":
    main()
