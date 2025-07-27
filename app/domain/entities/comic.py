from dataclasses import dataclass

@dataclass
class Comic:
    title: str
    isbn: str
    publisher: str
    description: str
    is_deleted: bool = False
