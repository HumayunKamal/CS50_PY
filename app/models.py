from pydantic import BaseModel


class BookCreate(BaseModel):
    title: str
    author: str
    isbn: str

class MemberCreate(BaseModel):
    name: str
    email: str

class LoanCreate(BaseModel):
    book_id: int
    member_id: int