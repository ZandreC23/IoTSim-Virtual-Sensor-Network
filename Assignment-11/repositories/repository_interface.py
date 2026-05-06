"""
Generic Repository Interface
Defines standard CRUD operations for all repositories.
"""

from abc import ABC, abstractmethod
from typing import Optional, List, Generic, TypeVar

T = TypeVar('T')
ID = TypeVar('ID')


class Repository(ABC, Generic[T, ID]):
    """Generic repository interface for CRUD operations."""
    
    @abstractmethod
    def save(self, entity: T) -> None:
        """Save an entity (creates or updates)."""
        pass
    
    @abstractmethod
    def find_by_id(self, id: ID) -> Optional[T]:
        """Find an entity by its ID."""
        pass
    
    @abstractmethod
    def find_all(self) -> List[T]:
        """Find all entities."""
        pass
    
    @abstractmethod
    def delete(self, id: ID) -> None:
        """Delete an entity by its ID."""
        pass
    
    @abstractmethod
    def exists(self, id: ID) -> bool:
        """Check if an entity exists."""
        pass
    
    @abstractmethod
    def count(self) -> int:
        """Get the total number of entities."""
        pass