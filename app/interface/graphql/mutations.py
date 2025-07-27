from typing import Optional
import strawberry

from app.application.use_cases.create_comic import CreateComicUseCase
from app.application.use_cases.update_comic import UpdateComicUseCase
from app.domain.repositories.comic_repository import ComicRepository
from app.interface.graphql.types.comic_type import ComicType
from app.infrastructure.db.mongo_comic_repository import MongoComicRepository

@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_comic(self, title: str, isbn: str, publisher: str, description: str = "", is_deleted: bool = False) -> ComicType:
        repository = MongoComicRepository()
        use_case = CreateComicUseCase(repository)
        comic = use_case.execute(title, isbn, publisher, description, is_deleted)
        return ComicType(
            title=comic.title,
            isbn=comic.isbn,
            publisher=comic.publisher,
            description=comic.description
        )

    @strawberry.mutation
    def update_comic(self,
                     isbn: str,
                     title: Optional[str] = None,
                     publisher: Optional[str] = None,
                     description: Optional[str] = None) -> Optional[ComicType]:
        repository = MongoComicRepository()
        use_case = UpdateComicUseCase(repository)
        updated = use_case.execute(isbn, title, publisher, description)
        return ComicType(
            title=updated.title,
            isbn=updated.isbn,
            publisher=updated.publisher,
            description=updated.description
        ) if updated else None

    @strawberry.mutation
    def delete_comic(self, isbn: str) -> bool:
        repository = MongoComicRepository()
        return repository.delete(isbn)
