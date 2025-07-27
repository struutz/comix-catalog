from app.domain.repositories.comic_repository import ComicRepository
from app.domain.entities.comic import Comic
from typing import Optional

class UpdateComicUseCase:
    def __init__(self, repository: ComicRepository):
        self.repository = repository

    def execute(self, isbn: str, title: Optional[str], publisher: Optional[str], description: Optional[str]) -> Optional[Comic]:
        comic = self.repository.get_by_isbn(isbn)
        if not comic:
            return None

        comic.title = title or comic.title
        comic.publisher = publisher or comic.publisher
        comic.description = description or comic.description

        return self.repository.update(isbn, comic)
