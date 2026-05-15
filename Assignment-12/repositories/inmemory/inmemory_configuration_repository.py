from typing import List, Optional
from models import Configuration


class InMemoryConfigurationRepository:

    def __init__(self):
        self._storage: dict[str, Configuration] = {}
        self._current_config = None

    def save(self, entity: Configuration) -> None:
        self._current_config = entity
        self._storage["singleton"] = entity

    def find_by_id(self, id: str) -> Optional[Configuration]:
        return self._storage.get(id)

    def find_all(self) -> List[Configuration]:
        return [self._current_config] if self._current_config else []

    def delete(self, id: str) -> None:
        if id in self._storage:
            del self._storage[id]
            self._current_config = None

    def exists(self, id: str) -> bool:
        return id in self._storage

    def count(self) -> int:
        return len(self._storage)

    def get_config(self) -> Optional[Configuration]:
        return self._current_config

    def clear(self) -> None:
        self._storage.clear()
        self._current_config = None