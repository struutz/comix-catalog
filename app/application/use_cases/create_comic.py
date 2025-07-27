from app.domain.entities.comic import Comic
from app.domain.repositories.comic_repository import ComicRepository

class CreateComicUseCase:
    def __init__(self, repository: ComicRepository):
        self.repository = repository

    def execute(self, title: str, isbn: str, publisher: str, description: str = "", is_deleted: bool = False) -> Comic:
        comic = Comic(title, isbn, publisher, description, is_deleted)
        return self.repository.add(comic)
