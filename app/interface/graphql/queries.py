import strawberry
from typing import List
from app.domain.repositories.comic_repository import ComicRepository
from app.interface.graphql.types.comic_type import ComicType
from app.infrastructure.db.mongo_comic_repository import MongoComicRepository

@strawberry.type
class Query:
    @strawberry.field
    def comics(self) -> List[ComicType]:
        repository: ComicRepository = MongoComicRepository()
        comics = repository.list_all()
