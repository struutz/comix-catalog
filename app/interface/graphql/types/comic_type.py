import strawberry

@strawberry.type
class ComicType:
    title: str
    isbn: str
    publisher: str
    description: str
