from typing import List, Optional
from app.domain.entities.comic import Comic
from app.domain.repositories.comic_repository import ComicRepository
from app.infrastructure.db.models.comic_document import ComicDocument

def _map_to_entity(doc: ComicDocument) -> Comic:
    return Comic(
        title=doc.title,
        isbn=doc.isbn,
        publisher=doc.publisher,
        description=doc.description,
        is_deleted=doc.is_deleted
    )

class MongoComicRepository(ComicRepository):
    def add(self, comic: Comic) -> Comic:
        ComicDocument(**comic.__dict__).save()
        return comic

    def get_by_isbn(self, isbn: str) -> Optional[Comic]:
        comic = ComicDocument.objects(isbn=isbn, is_deleted=False).first()
        if comic:
            return _map_to_entity(comic)
        return None

    def update(self, isbn: str, comic: Comic) -> Optional[Comic]:
        doc = ComicDocument.objects(isbn=isbn).first()
        if not doc:
            return None

        doc.title = comic.title
        doc.publisher = comic.publisher
        doc.description = comic.description
        doc.is_deleted = comic.is_deleted
        doc.save()

        return comic

    def delete(self, isbn: str) -> bool:
        result = ComicDocument.objects(isbn=isbn).first()
        if not result:
            return False
        result.is_deleted = True
        result.save()
        return True

    def list_all(self) -> List[Comic]:
        comics = []
        for doc in ComicDocument.objects(is_deleted=False):
            comics.append(_map_to_entity(doc))
        return comics
