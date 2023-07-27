from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar

from sqlalchemy.orm import declarative_base

T = TypeVar('T')

import typing
if typing.TYPE_CHECKING:
    from lsst.db.table_handler import TableHandler

class TableDefinition(Generic[T], ABC):

    @staticmethod
    def get_base() -> Any:
        return declarative_base()

    @abstractmethod
    def get_table(self) -> Any:
        raise NotImplemented()

    @abstractmethod
    def get_helper(self, table_handler: 'TableHandler') -> T:
        raise NotImplemented()
