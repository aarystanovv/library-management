from typing import Optional

class Book:
    def __init__(self, id: int, title: str, author: str, year: int, status: str = "available"):
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Book":
        return cls(data["id"], data["title"], data["author"], data["year"], data["status"])
