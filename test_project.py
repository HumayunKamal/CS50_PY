from project import search_books, count_borrowed_books, get_statistics

from app.data import books, members, loans


def setup_function():
    books.clear()
    members.clear()
    loans.clear()


def test_search_books():
    books.append(
        {
            "id": 1,
            "title": "CS50 python",
            "author": "David Malan",
            "isbn": "123",
            "available": True,
        }
    )

    result = search_books("python")
    assert len(result) == 1
    assert result[0]["title"] == "CS50 python"


def test_count_borrowed_books():
    books.extend(
        [
            {
                "id": 1,
                "title": "CS50 python",
                "author": "David Malan",
                "isbn": "123",
                "available": False,
            },
            {
                "id": 2,
                "title": "CS50 C",
                "author": "David Malan",
                "isbn": "456",
                "available": True,
            },
        ]
    )

    assert count_borrowed_books() == 1


def test_get_statistics():
    books.append(
        {
            "id": 1,
            "title": "CS50 python",
            "author": "David Malan",
            "isbn": "123",
            "available": True,
        },
    )

    members.append(
        {"id": 1, "name": "Humayun Kamal", "email": "humayunKamal@gmail.com"}
    )

    result = get_statistics()

    assert result["total_books"] == 1
    assert result["available_books"] == 1
    assert result["borrowed_books"] == 0
    assert result["total_members"] == 1
