from abc import ABC, abstractmethod
from typing import List, Optional
from app.domain.entities.comic import Comic

class ComicRepository(ABC):
    @abstractmethod
    def add(self, comic: Comic) -> Comic:
        pass

    @abstractmethod
    def list_all(self) -> List[Comic]:
        pass

    @abstractmethod
    def update(self, isbn: str, comic: Comic) -> Optional[Comic]:
        pass

    @abstractmethod
    def delete(self, isbn: str) -> bool:
        pass

    @abstractmethod
    def get_by_isbn(self, isbn: str) -> Optional[Comic]:
        pass
